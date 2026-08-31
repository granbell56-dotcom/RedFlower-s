# mini_nmap.py
# Mini-Nmap pour Hackrow
# - utilise python-nmap + binaire nmap si disponibles
# - sinon fallback : TCP connect scan multithread + banner grabbing
# - écrit un log simple mini_nmap.log
#
# WARNING: N'effectuez des scans que sur des cibles que vous possédez
# ou pour lesquelles vous avez l'autorisation explicite (ex: scanme.nmap.org).

import socket
import concurrent.futures
import subprocess
import time
import datetime
import shutil
import sys
import os

# ------------- Configuration -------------
DEFAULT_PORTS = [
    # FTP / Remote
    20, 21, 22, 23,

    # Mail
    25, 110, 143, 465, 587, 993, 995,

    # DNS / Network
    53, 67, 68, 69,

    # Web
    80, 443, 8080, 8443,

    # Windows / LAN
    135, 137, 138, 139, 445,
    3389,

    # Databases
    1433,   # MSSQL
    1521,   # Oracle
    2049,   # NFS
    2082, 2083,  # cPanel
    2086, 2087,  # WHM
    3306,   # MySQL
    5432,   # PostgreSQL
    6379,   # Redis
    27017,  # MongoDB

    # Services divers
    111,    # RPCBind
    389,    # LDAP
    636,    # LDAPS
    5900,   # VNC
    9000    # Services web / debug
]

LOG_FILE = "mini_nmap.log"
MAX_THREADS = 200
SOCKET_TIMEOUT = 0.6
BANNER_TIMEOUT = 1.0
# -----------------------------------------


def is_nmap_binary_available():
    return bool(shutil.which("nmap"))


def is_python_nmap_available():
    try:
        import nmap  # python-nmap
        return True
    except Exception:
        return False


def parse_ports(ports_str):
    """
    Parse '80,443,1000-1010' -> sorted list of ints
    If ports_str is falsy -> return DEFAULT_PORTS copy
    """
    if not ports_str:
        return DEFAULT_PORTS[:]
    parts = ports_str.split(",")
    ports = set()
    for part in parts:
        p = part.strip()
        if not p:
            continue
        if "-" in p:
            try:
                a, b = map(int, p.split("-", 1))
                if a > b:
                    a, b = b, a
                ports.update(range(max(1, a), min(65535, b) + 1))
            except Exception:
                continue
        else:
            try:
                ports.add(int(p))
            except Exception:
                continue
    return sorted([x for x in ports if 1 <= x <= 65535])


def log_result(target, method, ports_tested, open_ports):
    ts = datetime.datetime.utcnow().isoformat()
    line = f"{ts} | target={target} | method={method} | tested={ports_tested} | open={open_ports}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass


# ---------------- Banner grabbing & socket scan ----------------
def try_banner(sock, timeout=BANNER_TIMEOUT):
    try:
        sock.settimeout(timeout)
        data = sock.recv(1024)
        return data.decode(errors="ignore").strip()
    except Exception:
        return ""


def scan_port_connect(host, port, timeout=SOCKET_TIMEOUT, banner=True):
    """
    Try a TCP connect on host:port.
    Return tuple (port, is_open (bool), banner (str or "")).
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        rc = s.connect_ex((host, port))
        if rc == 0:
            b = ""
            if banner:
                try:
                    # minimal probe for HTTP-like ports
                    if port in (80, 8080):
                        try:
                            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                        except Exception:
                            pass
                    b = try_banner(s)
                except Exception:
                    b = ""
            try:
                s.close()
            except Exception:
                pass
            return (port, True, b)
        try:
            s.close()
        except Exception:
            pass
        return (port, False, "")
    except Exception:
        try:
            s.close()
        except Exception:
            pass
        return (port, False, "")


def threaded_connect_scan(host, ports, max_workers=MAX_THREADS, banner=True):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(ports) or 1)) as ex:
        futures = {ex.submit(scan_port_connect, host, p, SOCKET_TIMEOUT, banner): p for p in ports}
        for fut in concurrent.futures.as_completed(futures):
            try:
                res = fut.result()
                results.append(res)
            except Exception:
                pass
    return sorted(results, key=lambda x: x[0])


# ---------------- Nmap integrations ----------------
def nmap_scan_with_python_nmap(host, ports, arguments='-sS -Pn -T4'):
    """Use python-nmap (wrapper) if available. Returns list of open ports or None on failure."""
    try:
        import nmap as _nmap  # python-nmap
        nm = _nmap.PortScanner()
        port_str = ",".join(str(p) for p in ports) if isinstance(ports, (list, tuple)) else str(ports)
        nm.scan(hosts=host, ports=port_str, arguments=arguments)
        found = []
        if host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                for p in nm[host][proto].keys():
                    if nm[host][proto][p]['state'] == "open":
                        found.append(int(p))
        return sorted(found)
    except Exception:
        return None


def nmap_scan_with_subprocess(host, ports):
    """Call nmap binary via subprocess and parse output. Returns list or None."""
    try:
        port_str = ",".join(str(p) for p in ports) if isinstance(ports, (list, tuple)) else str(ports)
        proc = subprocess.run(["nmap", "-p", port_str, host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
        out = (proc.stdout or "") + (proc.stderr or "")
        found = []
        for line in out.splitlines():
            line = line.strip()
            # lines like: "80/tcp open  http"
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 3 and "/" in parts[0] and ("open" in line):
                try:
                    p = int(parts[0].split("/")[0])
                    if "open" in line:
                        found.append(p)
                except Exception:
                    continue
        return sorted(found)
    except Exception:
        return None


# ---------------- Public API ----------------
def scan_host(target, ports=None, use_banner=True):
    """
    Main API:
    - target: hostname or IP
    - ports: list of ints (if None -> DEFAULT_PORTS)
    - returns dict: {target, method, tested (list), open: [(port,banner)...], elapsed}
    """
    start = time.time()
    ports = ports if ports is not None else DEFAULT_PORTS[:]
    tested = ports[:]
    method_used = "socket"
    open_ports = []

    # prefer python-nmap if it is available and nmap binary exists
    if is_python_nmap_available() and is_nmap_binary_available():
        try:
            nn = nmap_scan_with_python_nmap(target, ports)
            if nn is not None:
                method_used = "python-nmap"
                open_ports = [(p, "") for p in nn]
                elapsed = time.time() - start
                log_result(target, method_used, tested, [p for p,_ in open_ports])
                return {"target": target, "method": method_used, "tested": tested, "open": open_ports, "elapsed": elapsed}
        except Exception:
            pass

    # next, try nmap binary if available
    if is_nmap_binary_available():
        try:
            nn = nmap_scan_with_subprocess(target, ports)
            if nn is not None:
                method_used = "nmap-binary"
                open_ports = [(p, "") for p in nn]
                elapsed = time.time() - start
                log_result(target, method_used, tested, [p for p,_ in open_ports])
                return {"target": target, "method": method_used, "tested": tested, "open": open_ports, "elapsed": elapsed}
        except Exception:
            pass

    # fallback: socket connect scan
    res = threaded_connect_scan(target, ports, max_workers=min(MAX_THREADS, len(ports) or 1), banner=use_banner)
    for p, is_open, banner in res:
        if is_open:
            open_ports.append((p, banner))
    elapsed = time.time() - start
    log_result(target, "socket", tested, [p for p,_ in open_ports])
    return {"target": target, "method": "socket", "tested": tested, "open": open_ports, "elapsed": elapsed}


# ---------------- CLI / demo helper ----------------
def prompt_and_run(lang="fr"):
    texts = {
        "fr": {
            "warn": "Attention : scanner un hôte sans autorisation peut être illégal. Continuer ? (o/n) ",
            "host": "Hôte à scanner (ex: scanme.nmap.org ou 192.168.1.1) : ",
            "ports": "Ports (ex: 80,443 ou 1-1024) [entrée = ports par défaut] : ",
            "abort": "Scan annulé.",
        },
        "en": {
            "warn": "Warning: scanning a host without authorization may be illegal. Continue? (y/n) ",
            "host": "Host to scan (e.g. scanme.nmap.org or 192.168.1.1): ",
            "ports": "Ports (e.g. 80,443 or 1-1024) [enter = default ports]: ",
            "abort": "Scan aborted.",
        },
        "es": {
            "warn": "Atención: escanear un host sin autorización puede ser ilegal. ¿Continuar? (s/n) ",
            "host": "Host a escanear (ej: scanme.nmap.org o 192.168.1.1): ",
            "ports": "Puertos (ej: 80,443 o 1-1024) [enter = puertos por defecto]: ",
            "abort": "Escaneo cancelado.",
        }
    }
    t = texts.get(lang, texts["fr"])
    try:
        yn = input(t["warn"]).strip().lower()
        if yn not in ("y","yes","o","oui","s","si"):
            print(t["abort"])
            return None
        host = input(t["host"]).strip()
        if not host:
            print(t["abort"])
            return None
        ports_str = input(t["ports"]).strip()
        ports = parse_ports(ports_str) if ports_str else None

        print(f"Scanning {host} ... (this may take a few seconds)")
        out = scan_host(host, ports=ports, use_banner=True)
        if not out:
            print("No result (error or aborted).")
            return None
        if out["open"]:
            print("Open ports:")
            for p,b in out["open"]:
                if b:
                    print(f" - {p}  |  banner: {b}")
                else:
                    print(f" - {p}")
        else:
            print("No open ports found (within tested list).")
        print(f"Method: {out['method']} — elapsed {out['elapsed']:.2f}s")
        print(f"Logged to {LOG_FILE}")
        return out
    except KeyboardInterrupt:
        print("\nAborted by user.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


# If run directly, demo
if __name__ == "__main__":
    lang = "fr"
    if len(sys.argv) >= 2 and sys.argv[1] in ("fr","en","es"):
        lang = sys.argv[1]
    prompt_and_run(lang=lang)
