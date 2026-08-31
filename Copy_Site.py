
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, init

init(autoreset=True)

# =========================
# CONFIG
# =========================
OUTPUT_DIR = "Site_Web"
visited = set()


# =========================
# UTILS
# =========================
def safe_path(path: str) -> str:
    path = path.split("?")[0]
    if path.endswith("/") or path == "":
        path += "index.html"
    return path


def is_same_domain(url: str, base_url: str) -> bool:
    return urlparse(url).netloc == urlparse(base_url).netloc


def save_file(url: str, content: bytes):
    parsed = urlparse(url)
    path = safe_path(parsed.path)

    local_path = os.path.join(OUTPUT_DIR, path.lstrip("/"))
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    with open(local_path, "wb") as f:
        f.write(content)


# =========================
# DOWNLOAD FILES
# =========================
def download_file(url: str):
    if url in visited:
        return

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            print(Fore.LIGHTYELLOW_EX + f"[!] Skip (HTTP {r.status_code}) : {url}" + Fore.RESET)
            return

        save_file(url, r.content)
        print(Fore.GREEN + f"[+] Fichier : {url}" + Fore.RESET)

    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[ERREUR FILE] {url} -> {e}" + Fore.RESET)


# =========================
# CRAWLER
# =========================
def crawl(url: str, base_url: str):
    try:
        if url in visited:
            return

        visited.add(url)

        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            print(Fore.LIGHTRED_EX + f"[!] Page inaccessible : {url}" + Fore.RESET)
            return

        soup = BeautifulSoup(r.text, "html.parser")

        # sauvegarde HTML
        parsed = urlparse(url)
        path = safe_path(parsed.path)

        local_html = os.path.join(OUTPUT_DIR, path.lstrip("/"))
        os.makedirs(os.path.dirname(local_html), exist_ok=True)

        with open(local_html, "w", encoding="utf-8") as f:
            f.write(r.text)
        
        print()

        print(f"[HTML] {url}")

        print()

        # ressources
        tags = {
            "img": "src",
            "script": "src",
            "link": "href"
        }

        for tag, attr in tags.items():
            for element in soup.find_all(tag):
                link = element.get(attr)
                if not link:
                    continue

                full_url = urljoin(url, link)

                if not is_same_domain(full_url, base_url):
                    continue

                download_file(full_url)

        # liens internes
        for a in soup.find_all("a", href=True):
            next_url = urljoin(url, a["href"])

            if not is_same_domain(next_url, base_url):
                continue

            if next_url not in visited:
                crawl(next_url, base_url)

    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[ERREUR PAGE] {url} -> {e}" + Fore.RESET)


# =========================
# ENTRY POINT (IMPORTANT)
# =========================
def Copy_Site():
    os.system("cls")
    
    print(Fore.LIGHTBLACK_EX + "developed by Luuxo")

    base_url = input("Entre l'URL du site à copier : ").strip()

    if not base_url.startswith("http"):
        print(Fore.LIGHTRED_EX + "[!] URL invalide" + Fore.RESET)
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    crawl(base_url, base_url)

    print(Fore.GREEN + "\n[TÉLÉCHARGEMENT TERMINÉ]" + Fore.RESET)
