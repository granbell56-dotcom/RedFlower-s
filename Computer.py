
import psutil as p
import platform
import os
from colorama import Fore, init

init()

vers = Fore.LIGHTGREEN_EX + "->" + Fore.RESET # <-- direction en vert
versp = Fore.MAGENTA + "->" + Fore.RESET # <-- direction en violet 
verspe = Fore.LIGHTBLACK_EX + "|" + Fore.RESET # <-- separation grise 
versper = Fore.LIGHTBLACK_EX + "]" + Fore.RESET # <-- fermeture grise

def Computer_Information():
        
        print()
        print()

        site = "Infortmation sur l'ordinateur"
        site = Fore.LIGHTBLUE_EX + site.capitalize() + Fore.RESET

        computer_name = platform.node()
        computer_name = Fore.LIGHTRED_EX + computer_name.capitalize() + Fore.RESET

        env = os.getenv('USERNAME')
        env = Fore.LIGHTRED_EX + env.capitalize() + Fore.RESET

        system = platform.system() + " " + platform.release()
        system = Fore.LIGHTYELLOW_EX + system + Fore.RESET

        Titre_cpu = Fore.LIGHTYELLOW_EX + " CPU"  + Fore.RESET
        Titre_ram = Fore.LIGHTYELLOW_EX + " RAM"  + Fore.RESET
        Titre_disk = Fore.LIGHTYELLOW_EX + " Disque"  + Fore.RESET
        Titre_reseau = Fore.LIGHTYELLOW_EX + " Octets Réseau"  + Fore.RESET


        # CPU
        CPU = p.cpu_percent(interval=1)

        # RAM
        ram = p.virtual_memory()
        RAM_TOTAL = round(ram.total / (1024**3), 2) # Go
        RAM_UTILISER = round(ram.used / (1024**3), 2) # Go

        # Disque
        disk = p.disk_usage('/')
        DISQUE_TOTAL = round(disk.total / (1024**3), 2) # Go
        DISQUE_UTILISER = round(disk.used / (1024**3), 2) # Go
        DISQUE_LIBRE = round(disk.free / (1024**3), 2) # Go

        # octets reseau
        net = p.net_io_counters()
        OCTETS_TELECHARGER = round(net.bytes_recv / 1024 / 1024, 2) # Mo
        OCTETS_ENVOYER = round(net.bytes_sent / 1024 / 1024, 2) # Mo
        
        print(Fore.LIGHTBLACK_EX + f"┌─/[{computer_name} {verspe} {env}{versper}", Fore.LIGHTBLACK_EX + f"/─>[~{site}", Fore.LIGHTBLACK_EX + f"~]/->[~{system}~]" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX +"│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "Utilisation CPU", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {Titre_cpu}  {versp}   ", Fore.CYAN + f"{CPU} %" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX +"│============| ", Fore.WHITE + "Mémoire RAM", Fore.LIGHTBLACK_EX + "|============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {Titre_ram}  {versp}   ", Fore.CYAN + f"Mémoire RAM utilisé {RAM_UTILISER} Go  |  Mémoire RAM total {RAM_TOTAL} Go" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "Utilisation disque", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {Titre_disk}  {versp}   ", Fore.CYAN + f"Disque utilisé {DISQUE_UTILISER} Go  |  Disque libre {DISQUE_LIBRE} Go  | Disque total {DISQUE_TOTAL}Go" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "Réseau octets envoyés / reçus", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {Titre_reseau}  {versp}   ", Fore.CYAN + f"Octets envoyé {OCTETS_ENVOYER} Mo  | Octets téléchargé {OCTETS_TELECHARGER} Mo" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "└────────────────────────────────────────────────│->[Developed by Luuxo]" + Fore.RESET)

        print()
