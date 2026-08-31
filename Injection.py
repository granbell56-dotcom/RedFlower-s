
import time
import os as o

from PONT import pont_flower

from colorama import Fore, init

init(autoreset=True)

def Labo_A_Injection():
    o.system("cls")
    
    admin = False
    user = True
    profile = {
        "name": "guest",
        "role": "user",
        "access": "limited"
    }

    print(Fore.LIGHTBLACK_EX + "\n[ RedFlower Secure Terminal ]")
    print("Mode expérimental activé")
    print("Certaines fonctionnalités avancées sont disponibles.\n")

    print("Création du profil utilisateur...\n")
    time.sleep(1)

    print(Fore.LIGHTBLACK_EX + "Terminal débloqué.")
    print("Tape 'help' pour voir les options.\n")

    while True:
        cmd = input(Fore.LIGHTCYAN_EX + "lab@redflower > ").strip()

        if not cmd:
            continue

        if cmd == "help":
            print("\nCommandes disponibles :")
            print("  set <champ>=<valeur>     → modifier ton profil")
            print("  show profile             → afficher le profil")
            print("  connect                  → tenter une connexion avancée")
            print("  exit                     → quitter\n")

        elif cmd.startswith("set "):
            try:

                rule = cmd.replace("set ", "")
                key, value = rule.split("=")

                key = key.strip().lower()
                value = value.strip().lower()

                if key in profile:
                    profile[key] = value
                    print(Fore.LIGHTGREEN_EX + f"[OK] {key} mis à jour.")
                else:
                    print(Fore.YELLOW + "[!] Champ inconnu, mais enregistré.")

                    profile[key] = value

            except ValueError:
                print(Fore.RED + "[ERREUR] Syntaxe invalide.")

        elif cmd == "show profile":
            print("\n--- PROFIL UTILISATEUR ---")
            for k, v in profile.items():
                print(f"{k:<10} : {v}")
            print("-------------------------\n")

        elif cmd == "connect":
            print("\nConnexion au module sécurisé...")
            time.sleep(1)

            if profile.get("role") == "admin" or profile.get("access") == "all":
                admin = True

            if admin:
                print(Fore.LIGHTGREEN_EX + "\n[ACCÈS ADMINISTRATEUR ACCORDÉ]")
                print("Bienvenue, opérateur.\n")
                admin_console()
                break
            else:
                print(Fore.RED + "\n[ACCÈS REFUSÉ]")
                print("Permissions insuffisantes.\n")

        elif cmd == "exit":
            print("\nFermeture du terminal...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Commande inconnue.\n")


def admin_console():
    print(Fore.LIGHTMAGENTA_EX + "=== CONSOLE ADMIN ===")
    print("Accès total au système simulé.")
    print("Tape 'logout' pour quitter.\n")

    while True:
        cmd = input(Fore.MAGENTA + "admin@redflower # ")

        if cmd == "logout":
            print("\nDéconnexion...\n")
            pont_flower()
        else:
            print(Fore.LIGHTBLACK_EX + "[SIMULATION] Action exécutée.\n")
