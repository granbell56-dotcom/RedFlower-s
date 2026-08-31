
import psutil as p
import os as o
import time as t
from colorama import Fore, init

init()

auteur = Fore.LIGHTBLACK_EX + "Developed by Luuxo" + Fore.RESET
texte = Fore.LIGHTBLACK_EX + "Ctrl + C : pour quitter" + Fore.RESET

verspe = Fore.LIGHTBLACK_EX + "|" + Fore.RESET # <-- separation grise
verspet = Fore.LIGHTBLACK_EX + "/" + Fore.RESET # <-- separation grise

def Download_upload():

    print(auteur)
    t.sleep(1)

    old = p.net_io_counters()

    try:
        while True:
            t.sleep(0.5)
            o.system("cls" if o.name == "nt" else "clear")

            new = p.net_io_counters()

            download_mbps = (new.bytes_recv - old.bytes_recv) * 8 / 1_000_000
            upload_mbps = (new.bytes_sent - old.bytes_sent) * 8 / 1_000_000

            print("\n" + texte + "\n")

            print(
                f"↓ {Fore.LIGHTRED_EX}{download_mbps:.2f}{Fore.RESET} Mbp{verspet}s {verspe} "
                f"↑ {Fore.LIGHTGREEN_EX}{upload_mbps:.2f}{Fore.RESET} Mbp{verspet}s"
            )

            old = new

    except KeyboardInterrupt:
        o.system("cls")
        print(Fore.LIGHTRED_EX + "Net-Speed arrété. Redirection en cours.." + Fore.RESET) 

        t.sleep(1) 
        o.system("cls")

        return
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)
