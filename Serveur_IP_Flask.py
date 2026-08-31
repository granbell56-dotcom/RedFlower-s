
from flask import Flask, jsonify, render_template_string
from waitress import serve
import psutil
import socket
import time
import subprocess
import os
import threading
import platform

app = Flask(__name__)

# =========================
# CACHE + LOCK
# =========================
_lock = threading.Lock()
_metrics_cache = {
    "cpu": 0, "ram": 0, "ram_total": 0,
    "download_mbps": 0.0, "upload_mbps": 0.0,
    "download_total_gb": 0.0, "upload_total_gb": 0.0,
    "ping_cf": 0, "ping_google": 0, "jitter": 0,
    "processes": 0, "uptime": "",
    "ipv4": "—", "ipv6": "—", "gateway": "—",
    "interface": "—", "ethernet_ip": "Déconnecté", "wifi_ip": "Déconnecté",
    "gpu": "N/A", "os_version": platform.version()[:40],
    "hostname": socket.gethostname(),
    "internet": "Online",
}
_dl_history   = []
_ul_history   = []
_ping_history = []

# =========================
# THREAD — NET IO (200ms)
# ultra-réactif pour le débit
# =========================
def thread_net_io():
    prev = psutil.net_io_counters()
    prev_t = time.perf_counter()
    while True:
        time.sleep(0.2)
        try:
            cur   = psutil.net_io_counters()
            cur_t = time.perf_counter()
            dt    = cur_t - prev_t
            if dt > 0:
                dl = (cur.bytes_recv - prev.bytes_recv) / dt / 1e6 * 8
                ul = (cur.bytes_sent - prev.bytes_sent) / dt / 1e6 * 8
                with _lock:
                    _metrics_cache["download_mbps"]    = round(max(dl, 0), 2)
                    _metrics_cache["upload_mbps"]      = round(max(ul, 0), 2)
                    _metrics_cache["download_total_gb"]= round(cur.bytes_recv / 1e9, 2)
                    _metrics_cache["upload_total_gb"]  = round(cur.bytes_sent / 1e9, 2)
                    _dl_history.append(_metrics_cache["download_mbps"])
                    _ul_history.append(_metrics_cache["upload_mbps"])
                    if len(_dl_history) > 60: _dl_history.pop(0)
                    if len(_ul_history) > 60: _ul_history.pop(0)
            prev, prev_t = cur, cur_t
        except Exception:
            pass

# =========================
# THREAD — CPU / RAM (500ms)
# cpu_percent non-bloquant
# =========================
def thread_cpu_ram():
    # Premier appel d'initialisation (non-bloquant ensuite)
    psutil.cpu_percent(interval=None)
    while True:
        time.sleep(0.5)
        try:
            cpu = psutil.cpu_percent(interval=None)
            ram = psutil.virtual_memory()
            pids = len(psutil.pids())
            boot = psutil.boot_time()
            uptime_sec = int(time.time() - boot)
            h, m = divmod(uptime_sec // 60, 60)
            d, h = divmod(h, 24)
            uptime_str = f"{d}j {h}h {m}m"
            with _lock:
                _metrics_cache["cpu"]       = cpu
                _metrics_cache["ram"]       = ram.percent
                _metrics_cache["ram_total"] = round(ram.total / (1024**3), 1)
                _metrics_cache["processes"] = pids
                _metrics_cache["uptime"]    = uptime_str
        except Exception:
            pass

# =========================
# THREAD — GPU (1s)
# =========================
def thread_gpu():
    while True:
        time.sleep(1)
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=2
            )
            val = result.stdout.strip()
            gpu_str = f"{val}%" if val.isdigit() else "N/A"
        except Exception:
            gpu_str = "N/A"
        with _lock:
            _metrics_cache["gpu"] = gpu_str

# =========================
# THREAD — INTERFACES (10s)
# rarement change
# =========================
def thread_interfaces():
    while True:
        try:
            eth_ip = "Déconnecté"
            wifi_ip = "Déconnecté"
            ipv4 = "—"
            gateway = "—"
            active_iface = "—"
            ipv6 = "—"

            addrs = psutil.net_if_addrs()
            stats = psutil.net_if_stats()

            for iface, addr_list in addrs.items():
                if iface.lower() == "lo" or not stats.get(iface) or not stats[iface].isup:
                    continue
                for addr in addr_list:
                    if addr.family == socket.AF_INET:
                        ip = addr.address
                        il = iface.lower()
                        if any(k in il for k in ["eth", "lan", "local area"]):
                            eth_ip = ip
                        elif any(k in il for k in ["wi", "wlan", "wireless", "wifi"]):
                            wifi_ip = ip
                        if ip.startswith(("192.", "10.", "172.")):
                            ipv4 = ip
                            active_iface = iface
                    elif addr.family == socket.AF_INET6:
                        if not addr.address.startswith("fe80") and ipv6 == "—":
                            ipv6 = addr.address[:20] + "…"

            if platform.system() == "Windows":
                result = subprocess.run(["ipconfig"], capture_output=True, text=True, timeout=2)
                for line in result.stdout.split("\n"):
                    if "Default Gateway" in line or "Passerelle" in line:
                        parts = line.split(":")
                        if len(parts) > 1 and parts[-1].strip():
                            gateway = parts[-1].strip()
                            break

            with _lock:
                _metrics_cache["ethernet_ip"]  = eth_ip
                _metrics_cache["wifi_ip"]       = wifi_ip
                _metrics_cache["ipv4"]          = ipv4
                _metrics_cache["gateway"]       = gateway
                _metrics_cache["interface"]     = active_iface
                _metrics_cache["ipv6"]          = ipv6
        except Exception:
            pass
        time.sleep(10)

# =========================
# THREAD — PING (toutes les ~3s)
# ping -c 2 au lieu de 4 → 2x plus rapide
# =========================
def thread_ping():
    while True:
        try:
            param = "-n" if platform.system() == "Windows" else "-c"

            def do_ping(host):
                try:
                    cmd = ["ping", param, "2", host]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=4)
                    times = []
                    for line in result.stdout.split("\n"):
                        ll = line.lower()
                        for kw in ["time=", "temps="]:
                            if kw in ll:
                                idx = ll.index(kw) + len(kw)
                                val = ""
                                while idx < len(line) and (line[idx].isdigit() or line[idx] == "."):
                                    val += line[idx]; idx += 1
                                if val: times.append(float(val))
                    if times:
                        return int(sum(times)/len(times)), int(max(times)-min(times))
                except Exception:
                    pass
                return 999, 0

            ping_cf,     jitter = do_ping("1.1.1.1")
            ping_google, _      = do_ping("8.8.8.8")

            with _lock:
                _metrics_cache["ping_cf"]     = ping_cf
                _metrics_cache["ping_google"] = ping_google
                _metrics_cache["jitter"]      = jitter
                _metrics_cache["internet"]    = "Online" if ping_cf < 900 else "Offline"
                _ping_history.append(ping_cf if ping_cf < 900 else 0)
                if len(_ping_history) > 60: _ping_history.pop(0)
        except Exception:
            pass
        time.sleep(3)

# Lancement des threads
threading.Thread(target=thread_net_io,    daemon=True).start()
threading.Thread(target=thread_cpu_ram,   daemon=True).start()
threading.Thread(target=thread_gpu,       daemon=True).start()
threading.Thread(target=thread_interfaces,daemon=True).start()
threading.Thread(target=thread_ping,      daemon=True).start()

# =========================
# API
# =========================
@app.route("/api/metrics")
def api_metrics():
    with _lock:
        data = {
            **_metrics_cache,
            "dl_history":   list(_dl_history),
            "ul_history":   list(_ul_history),
            "ping_history": list(_ping_history),
        }
    return jsonify(data)

# =========================
# DASHBOARD HTML
# =========================
HTML = r"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>RedFlower — Cyber Toolkit</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

:root {
  --red:    #ff1f44;
  --red2:   #c4002e;
  --bg:     #030305;
  --panel:  rgba(6, 2, 4, 0.78);
  --text:   #ffccd5;
  --muted:  #6b4450;
  --green:  #00ffc8;
  --orange: #ff8c00;
  --blue:   #00aaff;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Share Tech Mono', 'Courier New', monospace;
  background: var(--bg);
  color: var(--text);
  overflow: hidden;
  height: 100vh;
  width: 100vw;
}

#canvas3d { position: fixed; inset: 0; z-index: 1; }

#scanlines {
  position: fixed; inset: 0; z-index: 2; pointer-events: none;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.03) 2px, rgba(0,0,0,0.03) 4px
  );
}

/* ── HAMBURGER ── */
#hamburger {
  position: fixed; top: 18px; left: 18px; z-index: 200;
  cursor: pointer; pointer-events: auto;
  display: flex; flex-direction: column; gap: 5px;
  padding: 10px; border: 1px solid rgba(255,31,68,.35);
  background: rgba(5,2,4,.92); backdrop-filter: blur(8px);
  border-radius: 4px; transition: border-color .2s, box-shadow .2s;
}
#hamburger:hover { border-color: var(--red); box-shadow: 0 0 16px rgba(255,31,68,.4); }
#hamburger span {
  display: block; width: 22px; height: 2px;
  background: var(--red); border-radius: 1px;
  transition: transform .3s, opacity .3s;
  box-shadow: 0 0 6px var(--red);
}
#hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
#hamburger.open span:nth-child(2) { opacity: 0; }
#hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* ── SIDEBAR ── */
#sidebar {
  position: fixed; top: 0; left: -420px; width: 390px; height: 100vh;
  z-index: 150; background: rgba(4,1,3,0.98);
  border-right: 1px solid rgba(255,31,68,.25);
  backdrop-filter: blur(20px);
  display: flex; flex-direction: column;
  transition: left .35s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}
#sidebar.open { left: 0; }

.sidebar-header {
  padding: 20px 20px 14px;
  border-bottom: 1px solid rgba(255,31,68,.2);
  margin-top: 60px;
}
.sidebar-title {
  font-family: 'Orbitron', monospace;
  font-size: 12px; letter-spacing: 3px;
  color: var(--red); text-transform: uppercase;
  text-shadow: 0 0 16px var(--red), 0 0 32px rgba(255,31,68,.4);
}
.sidebar-sub { font-size: 10px; color: var(--muted); margin-top: 4px; letter-spacing: 1px; }

.tabs { display: flex; border-bottom: 1px solid rgba(255,31,68,.15); }
.tab-btn {
  flex: 1; padding: 10px 4px; font-size: 10px;
  letter-spacing: 1.5px; text-transform: uppercase;
  background: none; border: none; color: var(--muted);
  cursor: pointer; font-family: 'Share Tech Mono', monospace;
  border-bottom: 2px solid transparent;
  transition: color .2s, border-color .2s;
}
.tab-btn.active { color: var(--red); border-bottom-color: var(--red); }
.tab-btn:hover  { color: var(--text); }

.sidebar-body { flex: 1; overflow-y: auto; padding: 14px; }
.tab-panel { display: none; }
.tab-panel.active { display: block; }

.s-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 9px 10px; border-bottom: 1px solid rgba(255,31,68,.07); font-size: 11px;
}
.s-row:last-child { border-bottom: none; }
.s-label { color: var(--muted); letter-spacing: 1px; text-transform: uppercase; }
.s-val { color: #fff; font-weight: bold; text-align: right; max-width: 55%; word-break: break-all; }
.s-val.green  { color: var(--green);  text-shadow: 0 0 8px var(--green); }
.s-val.red    { color: var(--red);    text-shadow: 0 0 8px var(--red); }
.s-val.orange { color: var(--orange); text-shadow: 0 0 8px var(--orange); }
.s-val.ok     { color: var(--green);  text-shadow: 0 0 8px var(--green); }
.s-val.warn   { color: var(--orange); text-shadow: 0 0 8px var(--orange); }

.bar-wrap { width: 100%; background: rgba(255,31,68,.1); border-radius: 2px; height: 4px; margin-top: 4px; overflow: hidden; }
.bar-fill { height: 100%; background: var(--red); box-shadow: 0 0 6px var(--red); border-radius: 2px; transition: width .4s ease; }

.graph-label { font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; margin: 12px 0 6px; }
.mini-canvas { width: 100%; height: 60px; border: 1px solid rgba(255,31,68,.15); background: rgba(0,0,0,.4); border-radius: 2px; display: block; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-thumb { background: var(--red); border-radius: 2px; }

/* ── HEADER ── */
header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 10;
  text-align: center; padding: 16px 20px;
  font-family: 'Orbitron', monospace;
  font-size: 20px; font-weight: 900;
  color: var(--red); letter-spacing: 8px;
  text-shadow: 0 0 24px var(--red), 0 0 48px rgba(255,31,68,.3);
  border-bottom: 1px solid rgba(255,31,68,.18);
  background: linear-gradient(180deg, rgba(255,31,68,.06) 0%, transparent 100%);
  pointer-events: none;
}

/* ── UI LAYER ── */
.ui-layer { position: fixed; inset: 0; z-index: 10; pointer-events: none; }

/* ── PANELS ── */
.panel {
  position: absolute;
  background: var(--panel);
  border: 1px solid rgba(255,31,68,.2);
  box-shadow: 0 0 40px rgba(0,0,0,.9), inset 0 0 30px rgba(255,31,68,.02);
  backdrop-filter: blur(14px);
  border-radius: 4px; padding: 16px;
  pointer-events: auto;
  max-height: calc(100vh - 120px);
  overflow-y: auto;
  min-width: 260px;
}
.panel-title {
  font-family: 'Orbitron', monospace;
  font-size: 10px; text-transform: uppercase;
  color: var(--red); margin-bottom: 12px;
  border-bottom: 1px dashed rgba(255,31,68,.3);
  padding-bottom: 6px; letter-spacing: 2px; font-weight: 700;
  text-shadow: 0 0 10px var(--red);
}
.info-card {
  background: rgba(0,0,0,.55);
  border-left: 2px solid var(--red);
  padding: 9px 12px; margin-bottom: 10px;
  transition: border-color .3s;
}
.info-card:hover { border-color: var(--green); }
.info-label { font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
.info-value {
  font-size: 17px; font-weight: bold; color: #fff;
  margin-top: 3px; text-shadow: 0 0 5px var(--red);
  font-family: 'Orbitron', monospace;
}
.net-active { color: var(--green) !important; text-shadow: 0 0 8px var(--green) !important; }

.status-pill {
  display: inline-block; padding: 3px 12px;
  border-radius: 20px; font-size: 10px; font-weight: bold;
  letter-spacing: 2px; text-transform: uppercase; margin-top: 4px;
  font-family: 'Orbitron', monospace;
}
.pill-online  { background: rgba(0,255,200,.1); color: var(--green); border: 1px solid var(--green); box-shadow: 0 0 10px rgba(0,255,200,.3); }
.pill-offline { background: rgba(255,31,68,.15); color: var(--red);  border: 1px solid var(--red);  box-shadow: 0 0 10px rgba(255,31,68,.3); }

.traffic-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 0; border-bottom: 1px solid rgba(255,31,68,.08); font-size: 11px;
}
.traffic-row:last-child { border-bottom: none; }
.traf-key { color: var(--muted); }
.traf-val { color: #fff; font-weight: bold; }
.traf-val.up   { color: var(--red);   text-shadow: 0 0 6px var(--red); }
.traf-val.down { color: var(--green); text-shadow: 0 0 6px var(--green); }
.traf-val.ok   { color: var(--green); }
.traf-val.warn { color: var(--orange); }

/* ── POSITIONS PANELS ── */
#panel-interfaces {
  top: 76px; left: 16px;
  transition: opacity .3s, transform .3s;
}
#panel-interfaces.hidden { opacity: 0; pointer-events: none; transform: translateX(-20px); }
#panel-health { top: 76px; right: 16px; }

/* ── SPEEDOMETERS ── */
#speedo-net { position: absolute; bottom: 20px; left: 16px; pointer-events: auto; width: 220px; }
#speedo-hw  { position: absolute; bottom: 20px; right: 16px; pointer-events: auto; width: 220px; }

.speedo-box {
  background: rgba(4,1,3,.88);
  border: 1px solid rgba(255,31,68,.25);
  border-radius: 6px; backdrop-filter: blur(14px); padding: 12px 14px;
  box-shadow: 0 0 30px rgba(0,0,0,.8), 0 0 20px rgba(255,31,68,.05);
}
.speedo-title {
  font-family: 'Orbitron', monospace;
  font-size: 9px; letter-spacing: 2px;
  color: var(--red); text-transform: uppercase;
  text-shadow: 0 0 8px var(--red); margin-bottom: 10px; text-align: center;
}
.gauge-wrap { display: flex; justify-content: center; margin-bottom: 8px; }
canvas.gauge { display: block; }

.speedo-values { display: flex; justify-content: space-between; gap: 8px; }
.sv-item {
  flex: 1; text-align: center;
  background: rgba(0,0,0,.45);
  border: 1px solid rgba(255,31,68,.12);
  border-radius: 3px; padding: 6px 4px;
}
.sv-label { font-size: 9px; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
.sv-num {
  font-family: 'Orbitron', monospace;
  font-size: 13px; font-weight: 700; margin-top: 2px;
}
.sv-num.green  { color: var(--green); text-shadow: 0 0 8px var(--green); }
.sv-num.red    { color: var(--red);   text-shadow: 0 0 8px var(--red); }
.sv-num.orange { color: var(--orange);text-shadow: 0 0 8px var(--orange); }
.sv-num.blue   { color: var(--blue);  text-shadow: 0 0 8px var(--blue); }
.sv-num.white  { color: #fff; }
</style>
</head>
<body>

<div id="canvas3d"></div>
<div id="scanlines"></div>
<header>_REDFLOWER_CYBER_NODE_</header>

<div id="hamburger" onclick="toggleSidebar()">
  <span></span><span></span><span></span>
</div>

<!-- ══ SIDEBAR ══ -->
<div id="sidebar">
  <div class="sidebar-header">
    <div class="sidebar-title">☰ RedFlower Core</div>
    <div class="sidebar-sub">System Intelligence Panel</div>
  </div>
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('system',event)">System</button>
    <button class="tab-btn" onclick="switchTab('network',event)">Network</button>
    <button class="tab-btn" onclick="switchTab('latency',event)">Latency</button>
    <button class="tab-btn" onclick="switchTab('monitor',event)">Monitor</button>
  </div>
  <div class="sidebar-body">

    <div class="tab-panel active" id="tab-system">
      <div class="s-row"><span class="s-label">CPU Usage</span><span class="s-val" id="s-cpu">—</span></div>
      <div style="padding:0 10px 8px"><div class="bar-wrap"><div class="bar-fill" id="bar-cpu" style="width:0%"></div></div></div>
      <div class="s-row"><span class="s-label">RAM Usage</span><span class="s-val" id="s-ram">—</span></div>
      <div style="padding:0 10px 8px"><div class="bar-wrap"><div class="bar-fill" id="bar-ram" style="width:0%;background:var(--green);box-shadow:0 0 6px var(--green)"></div></div></div>
      <div class="s-row"><span class="s-label">RAM Total</span><span class="s-val" id="s-ram-total">—</span></div>
      <div class="s-row"><span class="s-label">GPU</span><span class="s-val" id="s-gpu">—</span></div>
      <div class="s-row"><span class="s-label">Processes</span><span class="s-val" id="s-proc">—</span></div>
      <div class="s-row"><span class="s-label">Uptime</span><span class="s-val" id="s-uptime">—</span></div>
      <div class="s-row"><span class="s-label">Hostname</span><span class="s-val" id="s-host">—</span></div>
      <div class="s-row"><span class="s-label">OS</span><span class="s-val" id="s-os" style="font-size:9px">—</span></div>
    </div>

    <div class="tab-panel" id="tab-network">
      <div class="s-row"><span class="s-label">IPv4</span><span class="s-val green" id="n-ipv4">—</span></div>
      <div class="s-row"><span class="s-label">IPv6</span><span class="s-val" id="n-ipv6" style="font-size:9px">—</span></div>
      <div class="s-row"><span class="s-label">Gateway</span><span class="s-val" id="n-gateway">—</span></div>
      <div class="s-row"><span class="s-label">Interface</span><span class="s-val" id="n-iface">—</span></div>
      <div class="s-row"><span class="s-label">Ethernet IP</span><span class="s-val" id="n-eth">—</span></div>
      <div class="s-row"><span class="s-label">Wi-Fi IP</span><span class="s-val" id="n-wifi">—</span></div>
      <div class="s-row"><span class="s-label">Download</span><span class="s-val down" id="n-dl">—</span></div>
      <div class="s-row"><span class="s-label">Upload</span><span class="s-val up" id="n-ul">—</span></div>
      <div class="s-row"><span class="s-label">Total DL</span><span class="s-val" id="n-dl-total">—</span></div>
      <div class="s-row"><span class="s-label">Total UL</span><span class="s-val" id="n-ul-total">—</span></div>
    </div>

    <div class="tab-panel" id="tab-latency">
      <div class="s-row"><span class="s-label">Internet</span><span class="s-val" id="l-status">—</span></div>
      <div class="s-row"><span class="s-label">Ping Cloudflare</span><span class="s-val" id="l-cf">—</span></div>
      <div class="s-row"><span class="s-label">Ping Google</span><span class="s-val" id="l-google">—</span></div>
      <div class="s-row"><span class="s-label">Jitter</span><span class="s-val" id="l-jitter">—</span></div>
      <div style="padding:8px 0;font-size:9px;color:var(--muted);text-align:center;">Mise à jour toutes les ~3 secondes</div>
    </div>

    <div class="tab-panel" id="tab-monitor">
      <div class="graph-label">▼ Download (Mbps) — 60s</div>
      <canvas class="mini-canvas" id="graph-dl"></canvas>
      <div class="graph-label">▲ Upload (Mbps) — 60s</div>
      <canvas class="mini-canvas" id="graph-ul"></canvas>
      <div class="graph-label">◈ Ping ms — 60s</div>
      <canvas class="mini-canvas" id="graph-ping"></canvas>
    </div>

  </div>
</div>

<!-- ══ DASHBOARD ══ -->
<div class="ui-layer">

  <!-- Haut gauche -->
  <div class="panel" id="panel-interfaces">
    <div class="panel-title">Network Interfaces</div>
    <div class="info-card">
      <div class="info-label">Ethernet / LAN IP</div>
      <div id="net-ethernet" class="info-value">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">Wi-Fi / WLAN IP</div>
      <div id="net-wifi" class="info-value">—</div>
    </div>
    <div class="panel-title" style="margin-top:14px">Live Traffic</div>
    <div class="info-card">
      <div class="info-label">Download</div>
      <div id="d-dl" class="info-value" style="color:var(--green);text-shadow:0 0 8px var(--green)">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">Upload</div>
      <div id="d-ul" class="info-value" style="color:var(--red);text-shadow:0 0 8px var(--red)">—</div>
    </div>
    <div class="info-card">
      <div class="info-label">Ping</div>
      <div id="d-ping" class="info-value">—</div>
    </div>
  </div>

  <!-- Haut droit -->
  <div class="panel" id="panel-health">
    <div class="panel-title">Network Health</div>
    <div style="text-align:center;margin-bottom:12px;">
      <span id="d-internet-pill" class="status-pill pill-online">Online</span>
    </div>
    <div class="traffic-row"><span class="traf-key">CPU</span><span class="traf-val" id="d-cpu">—</span></div>
    <div class="traffic-row"><span class="traf-key">RAM</span><span class="traf-val" id="d-ram">—</span></div>
    <div class="traffic-row"><span class="traf-key">GPU</span><span class="traf-val" id="d-gpu">—</span></div>
    <div class="traffic-row"><span class="traf-key">Processus</span><span class="traf-val" id="d-proc">—</span></div>
    <div class="traffic-row"><span class="traf-key">Uptime</span><span class="traf-val" id="d-uptime">—</span></div>
    <div class="traffic-row"><span class="traf-key">Total DL</span><span class="traf-val down" id="d-dl-total">—</span></div>
    <div class="traffic-row"><span class="traf-key">Total UL</span><span class="traf-val up" id="d-ul-total">—</span></div>
    <div class="traffic-row"><span class="traf-key">IPv4</span><span class="traf-val ok" id="d-ipv4">—</span></div>
  </div>

  <!-- Bas gauche : speedometer réseau -->
  <div id="speedo-net">
    <div class="speedo-box">
      <div class="speedo-title">⬡ Network Throughput</div>
      <div class="gauge-wrap"><canvas class="gauge" id="gauge-net" width="190" height="110"></canvas></div>
      <div class="speedo-values">
        <div class="sv-item"><div class="sv-label">▼ DL</div><div class="sv-num green" id="sv-dl">0</div><div class="sv-label" style="font-size:8px">Mbps</div></div>
        <div class="sv-item"><div class="sv-label">▲ UL</div><div class="sv-num red" id="sv-ul">0</div><div class="sv-label" style="font-size:8px">Mbps</div></div>
        <div class="sv-item"><div class="sv-label">Ping</div><div class="sv-num orange" id="sv-ping">—</div><div class="sv-label" style="font-size:8px">ms</div></div>
      </div>
    </div>
  </div>

  <!-- Bas droit : speedometer hardware -->
  <div id="speedo-hw">
    <div class="speedo-box">
      <div class="speedo-title">⬡ Hardware Performance</div>
      <div class="gauge-wrap"><canvas class="gauge" id="gauge-hw" width="190" height="110"></canvas></div>
      <div class="speedo-values">
        <div class="sv-item"><div class="sv-label">CPU</div><div class="sv-num white" id="sv-cpu">0</div><div class="sv-label" style="font-size:8px">%</div></div>
        <div class="sv-item"><div class="sv-label">RAM</div><div class="sv-num blue" id="sv-ram">0</div><div class="sv-label" style="font-size:8px">%</div></div>
        <div class="sv-item"><div class="sv-label">GPU</div><div class="sv-num orange" id="sv-gpu">—</div><div class="sv-label" style="font-size:8px">%</div></div>
      </div>
    </div>
  </div>

</div>

<script>
// ══════════════════════════════════════════════
// THREE.JS — fleur rouge
// ══════════════════════════════════════════════
const scene    = new THREE.Scene();
const camera   = new THREE.PerspectiveCamera(60, innerWidth/innerHeight, 0.1, 1000);
camera.position.z = 40;
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setSize(innerWidth, innerHeight);
document.getElementById('canvas3d').appendChild(renderer.domElement);

const flowerGroup = new THREE.Group();
scene.add(flowerGroup);

const petalMats = [];
for (let i = 0; i < 12; i++) {
  const shape = new THREE.Shape();
  shape.moveTo(0,0);
  shape.quadraticCurveTo(3,8,0,15);
  shape.quadraticCurveTo(-3,8,0,0);
  const geo = new THREE.ExtrudeGeometry(shape, { depth:1, bevelEnabled:true, bevelSegments:2, bevelSize:.2, bevelThickness:.2 });
  const mat = new THREE.MeshPhongMaterial({ color:0xff002b, emissive:0x3a0008, specular:0xffffff, shininess:100, wireframe:true, side:THREE.DoubleSide });
  const mesh = new THREE.Mesh(geo, mat);
  const angle = (i/12)*Math.PI*2;
  mesh.rotation.z = angle - Math.PI/2;
  mesh.rotation.x = 0.5;
  flowerGroup.add(mesh);
  petalMats.push(mat);
}
flowerGroup.add(new THREE.Mesh(new THREE.SphereGeometry(2,16,16), new THREE.MeshBasicMaterial({ color:0xffffff, wireframe:true })));

const rings = [];
for (let i = 0; i < 3; i++) {
  const ring = new THREE.Mesh(
    new THREE.RingGeometry(18+(i*4), 18.2+(i*4), 32),
    new THREE.MeshBasicMaterial({ color:0xff1f44, side:THREE.DoubleSide, opacity:.3, transparent:true })
  );
  ring.rotation.x = Math.random()*Math.PI;
  ring.rotation.y = Math.random()*Math.PI;
  scene.add(ring);
  rings.push(ring);
}
scene.add(new THREE.AmbientLight(0x222222));
const pLight = new THREE.PointLight(0xff0033, 2, 100);
pLight.position.set(0,0,10);
scene.add(pLight);

// Cibles fleur (mises à jour par les données)
let flowerTargetScale = 1, flowerTargetSpeed = 0.3;
let flowerTargetColor = new THREE.Color(0xff002b);
let flowerCurScale    = 1, flowerCurSpeed    = 0.3;
const clock = new THREE.Clock();

// ══════════════════════════════════════════════
// INTERPOLATION — état courant des valeurs
// Toutes les valeurs numériques ont un "cur" et un "target"
// Le lerp les fait glisser à chaque frame → fluidité 60fps
// ══════════════════════════════════════════════
const V = {
  cpu:    { cur: 0,  target: 0 },
  ram:    { cur: 0,  target: 0 },
  gpu:    { cur: 0,  target: 0 },
  dl:     { cur: 0,  target: 0 },
  ul:     { cur: 0,  target: 0 },
  ping:   { cur: 0,  target: 0 },
};

// Facteur de lissage : plus proche de 1 = plus rapide
// 0.08 par frame à 60fps = ~80% de la cible atteinte en ~25 frames (~400ms)
const LERP = 0.08;

function lerp(a, b, t) { return a + (b - a) * t; }

// max DL vu pour calibrer la jauge réseau
let maxDlSeen = 10;

// ══════════════════════════════════════════════
// DESSIN DES GAUGES (appelé à 60fps via rAF)
// ══════════════════════════════════════════════
function drawNetGauge(dl, ul, maxDl) {
  const canvas = document.getElementById('gauge-net');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  ctx.clearRect(0, 0, W, H);
  const cx = W/2, cy = H-10;
  const rO = 52, rI = 36;
  const pDl = Math.min(dl / Math.max(maxDl, 1), 1);
  const pUl = Math.min(ul / Math.max(maxDl * 0.5, 1), 1);

  [rO, rI].forEach(r => {
    ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI, 2*Math.PI);
    ctx.strokeStyle = 'rgba(255,31,68,0.1)'; ctx.lineWidth = 8; ctx.stroke();
  });
  ctx.beginPath(); ctx.arc(cx, cy, rO, Math.PI, Math.PI + pDl * Math.PI);
  ctx.strokeStyle = '#00ffc8'; ctx.lineWidth = 8; ctx.lineCap = 'round';
  ctx.shadowColor = '#00ffc8'; ctx.shadowBlur = 14; ctx.stroke();
  ctx.beginPath(); ctx.arc(cx, cy, rI, Math.PI, Math.PI + pUl * Math.PI);
  ctx.strokeStyle = '#ff1f44'; ctx.shadowColor = '#ff1f44'; ctx.stroke();
  ctx.shadowBlur = 0;

  ctx.fillStyle = '#00ffc8'; ctx.font = 'bold 14px Orbitron, monospace';
  ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
  ctx.shadowColor = '#00ffc8'; ctx.shadowBlur = 8;
  ctx.fillText(dl >= 100 ? Math.round(dl) : dl.toFixed(1), cx, cy - 4);
  ctx.shadowBlur = 0;
  ctx.fillStyle = 'rgba(107,68,80,0.8)'; ctx.font = '8px Share Tech Mono';
  ctx.fillText('Mbps', cx, cy + 10);
}

function drawHwGauge(cpu, ram, gpuPct) {
  const canvas = document.getElementById('gauge-hw');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  ctx.clearRect(0, 0, W, H);
  const cx = W/2, cy = H-10;
  const radii  = [52, 39, 26];
  const values = [cpu/100, ram/100, gpuPct/100];
  const colors = ['#ffffff', '#00aaff', '#ff8c00'];
  const glows  = ['rgba(255,255,255,.6)', 'rgba(0,170,255,.6)', 'rgba(255,140,0,.6)'];

  radii.forEach((r, i) => {
    ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI, 2*Math.PI);
    ctx.strokeStyle = 'rgba(255,31,68,0.1)'; ctx.lineWidth = 7; ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI, Math.PI + values[i] * Math.PI);
    ctx.strokeStyle = colors[i]; ctx.lineWidth = 7; ctx.lineCap = 'round';
    ctx.shadowColor = glows[i]; ctx.shadowBlur = 12; ctx.stroke(); ctx.shadowBlur = 0;
  });

  ctx.fillStyle = '#ffffff'; ctx.font = 'bold 14px Orbitron, monospace';
  ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
  ctx.shadowColor = 'rgba(255,255,255,.6)'; ctx.shadowBlur = 8;
  ctx.fillText(Math.round(cpu) + '%', cx, cy - 4);
  ctx.shadowBlur = 0;
  ctx.fillStyle = 'rgba(107,68,80,0.8)'; ctx.font = '8px Share Tech Mono';
  ctx.fillText('CPU', cx, cy + 10);
}

function drawGraph(id, data, color, maxVal) {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.offsetWidth, H = canvas.offsetHeight;
  canvas.width = W; canvas.height = H;
  ctx.clearRect(0,0,W,H);
  if (!data || data.length < 2) return;
  const max = maxVal || Math.max(...data, 1);
  ctx.beginPath(); ctx.strokeStyle = color; ctx.lineWidth = 1.5;
  ctx.shadowColor = color; ctx.shadowBlur = 6;
  data.forEach((v, i) => {
    const x = (i/(data.length-1))*W, y = H-(v/max)*H*0.9;
    i === 0 ? ctx.moveTo(x,y) : ctx.lineTo(x,y);
  });
  ctx.stroke();
  ctx.lineTo(W,H); ctx.lineTo(0,H); ctx.closePath();
  ctx.fillStyle = color.replace(')',',.1)').replace('rgb','rgba'); ctx.fill();
}

// ══════════════════════════════════════════════
// BOUCLE RAF — 60fps
// Fait le lerp + redessine les gauges + anime la fleur
// ══════════════════════════════════════════════
function rafLoop() {
  requestAnimationFrame(rafLoop);
  const t = clock.getElapsedTime();

  // ── Lerp toutes les valeurs
  for (const key in V) {
    V[key].cur = lerp(V[key].cur, V[key].target, LERP);
  }

  // ── Redessiner les gauges avec valeurs interpolées
  drawNetGauge(V.dl.cur, V.ul.cur, Math.max(maxDlSeen, 10));
  drawHwGauge(V.cpu.cur, V.ram.cur, V.gpu.cur);

  // ── Mettre à jour les valeurs texte des speedometers
  setText('sv-dl',  V.dl.cur  >= 100 ? Math.round(V.dl.cur)  : V.dl.cur.toFixed(1));
  setText('sv-ul',  V.ul.cur  >= 100 ? Math.round(V.ul.cur)  : V.ul.cur.toFixed(1));
  setText('sv-ping', Math.round(V.ping.cur));
  setText('sv-cpu', Math.round(V.cpu.cur) + '%');
  setText('sv-ram', Math.round(V.ram.cur) + '%');
  const gpuDisp = V.gpu.target >= 0 ? Math.round(V.gpu.cur) + '%' : 'N/A';
  setText('sv-gpu', gpuDisp);

  // ── Fleur 3D
  flowerCurScale += (flowerTargetScale - flowerCurScale) * 0.04;
  flowerCurSpeed += (flowerTargetSpeed - flowerCurSpeed) * 0.04;
  flowerGroup.rotation.y = t * flowerCurSpeed;
  flowerGroup.rotation.z = t * 0.1;
  const pulse = 1 + Math.sin(t*3)*0.08;
  flowerGroup.scale.set(flowerCurScale*pulse, flowerCurScale*pulse, flowerCurScale*pulse);
  petalMats.forEach(m => m.color.lerp(flowerTargetColor, 0.05));
  rings.forEach((r,i) => { r.rotation.z += 0.005*(i+1); r.rotation.x += 0.002; });
  renderer.render(scene, camera);
}
rafLoop();

window.addEventListener('resize', () => {
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

// ══════════════════════════════════════════════
// HELPERS DOM
// ══════════════════════════════════════════════
function setText(id, val) {
  const el = document.getElementById(id);
  if (el && el.textContent !== String(val)) el.textContent = val;
}
function setClass(id, cls) {
  const el = document.getElementById(id);
  if (el && el.className !== cls) el.className = cls;
}
function pingClass(ms) {
  return ms < 50 ? 'ok' : ms < 150 ? 'warn' : 'red';
}

// ══════════════════════════════════════════════
// SIDEBAR
// ══════════════════════════════════════════════
function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  const hb = document.getElementById('hamburger');
  const pi = document.getElementById('panel-interfaces');
  sb.classList.toggle('open');
  hb.classList.toggle('open');
  pi.classList.toggle('hidden', sb.classList.contains('open'));
}
function switchTab(name, event) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-'+name).classList.add('active');
  if (event && event.target) event.target.classList.add('active');
}

// ══════════════════════════════════════════════
// FETCH API — toutes les 500ms
// Met uniquement à jour les "target" du lerp
// + les textes statiques (IP, hostname, etc.)
// ══════════════════════════════════════════════
let _histCache = { dl: [], ul: [], ping: [] };

async function fetchMetrics() {
  try {
    const res = await fetch('/api/metrics');
    const d   = await res.json();

    // ── Mise à jour des cibles lerp (valeurs numériques)
    V.cpu.target  = d.cpu;
    V.ram.target  = d.ram;
    V.dl.target   = d.download_mbps;
    V.ul.target   = d.upload_mbps;
    V.ping.target = d.ping_cf;
    const gpuNum  = parseFloat(d.gpu);
    V.gpu.target  = isNaN(gpuNum) ? -1 : gpuNum;

    if (d.download_mbps > maxDlSeen) maxDlSeen = d.download_mbps;

    // ── Fleur réactive
    flowerTargetScale = 1 + Math.min(d.download_mbps / 200, 0.5);
    flowerTargetSpeed = 0.25 + Math.min(d.upload_mbps  / 100, 0.5);
    const p = d.ping_cf;
    flowerTargetColor = new THREE.Color(p < 50 ? 0xff002b : p < 150 ? 0xff6600 : p < 500 ? 0xffaa00 : 0x441122);

    // ── Textes statiques / semi-statiques (mis à jour seulement si changement)
    // Dashboard principal
    const ethEl  = document.getElementById('net-ethernet');
    const wifiEl = document.getElementById('net-wifi');
    if (ethEl.textContent  !== d.ethernet_ip) { ethEl.textContent  = d.ethernet_ip;  ethEl.className  = d.ethernet_ip  !== 'Déconnecté' ? 'info-value net-active' : 'info-value'; }
    if (wifiEl.textContent !== d.wifi_ip)     { wifiEl.textContent = d.wifi_ip;       wifiEl.className = d.wifi_ip      !== 'Déconnecté' ? 'info-value net-active' : 'info-value'; }

    setText('d-dl',       d.download_mbps + ' Mbps');
    setText('d-ul',       d.upload_mbps   + ' Mbps');
    setText('d-ping',     d.ping_cf       + ' ms');
    setText('d-cpu',      d.cpu           + '%');
    setText('d-ram',      d.ram           + '%');
    setText('d-gpu',      d.gpu);
    setText('d-proc',     d.processes);
    setText('d-uptime',   d.uptime);
    setText('d-dl-total', d.download_total_gb + ' GB');
    setText('d-ul-total', d.upload_total_gb   + ' GB');
    setText('d-ipv4',     d.ipv4);

    const pill = document.getElementById('d-internet-pill');
    const pillClass = 'status-pill ' + (d.internet === 'Online' ? 'pill-online' : 'pill-offline');
    if (pill.textContent !== d.internet) pill.textContent = d.internet;
    if (pill.className   !== pillClass)  pill.className   = pillClass;

    // Volet System
    setText('s-cpu',      d.cpu      + '%');
    setText('s-ram',      d.ram      + '%');
    setText('s-ram-total',d.ram_total + ' GB');
    setText('s-gpu',      d.gpu);
    setText('s-proc',     d.processes);
    setText('s-uptime',   d.uptime);
    setText('s-host',     d.hostname);
    setText('s-os',       d.os_version);
    document.getElementById('bar-cpu').style.width = d.cpu + '%';
    document.getElementById('bar-ram').style.width = d.ram + '%';

    // Volet Network
    setText('n-ipv4',    d.ipv4);
    setText('n-ipv6',    d.ipv6 || '—');
    setText('n-gateway', d.gateway);
    setText('n-iface',   d.interface);
    setText('n-eth',     d.ethernet_ip);
    setText('n-wifi',    d.wifi_ip);
    setText('n-dl',      d.download_mbps + ' Mbps');
    setText('n-ul',      d.upload_mbps   + ' Mbps');
    setText('n-dl-total',d.download_total_gb + ' GB');
    setText('n-ul-total',d.upload_total_gb   + ' GB');

    // Volet Latency
    const lStatus = document.getElementById('l-status');
    lStatus.textContent = d.internet;
    lStatus.className   = 's-val ' + (d.internet === 'Online' ? 'green' : 'red');
    const cfEl = document.getElementById('l-cf');
    cfEl.textContent = d.ping_cf + ' ms';
    cfEl.className   = 's-val ' + pingClass(d.ping_cf);
    const ggEl = document.getElementById('l-google');
    ggEl.textContent = d.ping_google + ' ms';
    ggEl.className   = 's-val ' + pingClass(d.ping_google);
    setText('l-jitter', d.jitter + ' ms');

    // Couleurs speedometer valeurs texte
    setClass('sv-ping', 'sv-num ' + pingClass(d.ping_cf));
    setClass('sv-cpu',  'sv-num ' + (d.cpu > 85 ? 'red' : d.cpu > 60 ? 'orange' : 'white'));
    setClass('sv-ram',  'sv-num ' + (d.ram > 85 ? 'red' : d.ram > 70 ? 'orange' : 'blue'));
    setClass('sv-gpu',  'sv-num ' + (isNaN(gpuNum) ? 'orange' : gpuNum > 85 ? 'red' : 'orange'));

    // Graphiques (seulement si données changées)
    const dlStr = JSON.stringify(d.dl_history);
    const ulStr = JSON.stringify(d.ul_history);
    const pgStr = JSON.stringify(d.ping_history);
    if (dlStr !== JSON.stringify(_histCache.dl)) { drawGraph('graph-dl',   d.dl_history,   'rgb(0,255,200)');       _histCache.dl   = d.dl_history; }
    if (ulStr !== JSON.stringify(_histCache.ul)) { drawGraph('graph-ul',   d.ul_history,   'rgb(255,31,68)');       _histCache.ul   = d.ul_history; }
    if (pgStr !== JSON.stringify(_histCache.ping)){ drawGraph('graph-ping',d.ping_history, 'rgb(255,140,0)', 200); _histCache.ping = d.ping_history; }

  } catch(e) {
    console.warn("RedFlower fetch error:", e);
  }
}

// Fetch toutes les 500ms — les gauges sont déjà fluides via rAF
setInterval(fetchMetrics, 500);
fetchMetrics();
</script>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(HTML)

def Serveur_Dashboard():
    
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "═"*60)
        print("  REDFLOWER CYBER-NODE  —  SERVER ACTIVE  —  Ctrl + c pour quitter")
        print("═"*60)
        print(" -> Dashboard : http://127.0.0.1:5000  | Developed by Luuxo")
        print("═"*60 + "\n")
        serve(app, host="0.0.0.0", port=5000)
    
    except KeyboardInterrupt:
        print("Status : STOP")