
import os as o
import sys as s
import subprocess



from colorama import Fore, Style, init
init(autoreset=True)

versp = Fore.MAGENTA + "->" + Fore.RESET
texte = Fore.CYAN + "Liste des commandes" + Fore.RESET

def crow():
    from PONT import pont_fr

    print()
    print(Fore.LIGHTBLACK_EX + "Crow ; Version 2 [ RedFlower's Edition ] | Developed by LUUXO"  + Fore.RESET)
    print()
    
    while True:
        print()
        print("help- pour avoir la liste des commande")
        print()
        
        try:
              command = input(">>> ")
              
        except KeyboardInterrupt:
              print("Ctrl c Detecté.")
              continue

        if command == "help-":

            print()
            print(f"┌──────/[  {texte}  ]/─>")
            print("│")
            print("│", Fore.LIGHTYELLOW_EX + " pr; " + Fore.RESET, f"{versp}  ", Fore.LIGHTGREEN_EX + "Pour affiché du texte" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " Is*  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Pour lister les fichier du dossier courant" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cd -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Pour changer de dossier" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cwd*   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche les dossier courant" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cls   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Effacer l'écrand" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " run -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Exécuter des commande système" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tree  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche le graphisme de la structure de répertoire d'un lecteur" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tl-  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche toutes les tâches en cours d'exécution, y compris les services" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vrfy  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Demande à Windows de vérifier si vos fichiers sont correctement écrits sur le disque" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vol  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "VAffiche le nom et le numéro de série d'un volume de disque" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " DIR  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche la liste des fichiers et des sous-répertoires d'un répertoire" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " VER  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche la version de Windows." + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " SYSINFO  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche les propriétés et la configuration spécifiques de l'ordinateur" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " sysdm  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Propriétés système de Windows" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " appwiz  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Panneau de configuration de Windows" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " MyIp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Affiche des informations sur votre IP" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " ScNp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Scanme les port 21, 22, 80, 443" + Fore.RESET)
            print("│")
            print("└────────────────[", Fore.LIGHTGREEN_EX + "SUCESS", Fore.WHITE + "]" + Fore.RESET)

        elif command == "exit":
            pont_fr()
        
        elif command.startswith("pr;"):
            message = command[3:]
            print(message)

        elif command.startswith(f"Is*"):
            message = command[3:]
            for file in o.listdir():
                print(Fore.CYAN + file)
        
        elif command.startswith("cd -"):
                    path = command[4:].strip()
                    try:
                        o.chdir(path)
                        print(Fore.GREEN + f"Dossier changé : {o.getcwd()}")

                    except Exception as e:
                         print(Fore.RED + f"Erreur : {e}")

        elif command.startswith("cwd*"):
                    print(Fore.YELLOW + f"Dossier courant : {o.getcwd()}")
        
        elif command.startswith("cls"):
                    message = command[3:]
                    o.system('cls')
        
        elif command.startswith("run -"):
            cmd = command[5:].strip()
            
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                print(Fore.GREEN + output)

            except subprocess.CalledProcessError as e:
                  print(Fore.RED + "Erreur lors de l'exécution :", e.output)
        
        elif command.startswith("tree"):
              message = command[4:]
              try:
                o.system('tree')

              except Exception as e:
                   pass
              
        elif command.startswith("color"): # secret command
                    message = command[5:]
                    if command == "a":
                        o.system('color a')
                    else:
                        pass
        
        elif command.startswith("tl-"):
                    try:
                        message = command[3:]
                        o.system('tasklist')

                    except Exception as e:
                        print(f"{e}")

        elif command.startswith("vrfy"):
                    message = command[4:]
                    try:
                          o.system('verify')
                        
                    except Exception as e:
                        print(f"{e}")
        
        elif command.startswith("vol"):
                    try:
                        message = command[3:]
                        o.system('vol')

                    except Exception as e:
                        print(f"{e}")

        elif command.startswith("DIR"):
                    try:
                          message = command[3:]
                          o.system('dir')
                    
                    except Exception as e:
                          print(f"{e}")
            
        elif command.startswith("VER"):
              message = command[3:]
              o.system('ver')
        
        elif command.startswith("SYSINFO"):
              message = command[7:]
              o.system('systeminfo')

        elif command.startswith("sysdm"):
              message = command[5:]
              o.system('sysdm.cpl')
        
        elif command.startswith("appwiz"):
              message = command[6:]
              o.system('appwiz.cpl')

        elif command.startswith("MyIp"):
              message = command[4:]

              try:
                    
                    import requests

                    import socket
              
                    ip = requests.get("https://api.ipify.org").text

                    url = f"http://ip-api.com/json/{ip}"
                    response = requests.get(url)

                    data = response.json()

                    print("IP:", data["query"])

                    hostname = socket.gethostname()
                    local_ip = socket.gethostbyname(hostname)

                    print("IP locale :", local_ip)

                    print("Pays:", data["country"])

                    print("Région:", data["regionName"])

                    print("Ville:", data["city"])

                    print("FAI:", data["isp"])

                    print("Latitude:", data["lat"])

                    print("Longitude:", data["lon"])

                    print("-------------------------")

                    data = requests.get("https://ipwho.is/").json()
                    
                    print("IP :", data["ip"])
                    
                    print("VPN/Proxy :", data["connection"]["proxy"])
                    
                    print("Tor :", data["connection"]["tor"])

                    print('--------------------------')

                    data = requests.get("https://ipinfo.io/json").json()
                    
                    print("Organisation :", data["org"])
                    
                    print("ASN :", data["asn"]["asn"] if "asn" in data else "Inconnu")

              except Exception as e:
                    print(f"{e}")
        
        elif command.startswith("ScNp"):
              message = command[5:]

              try:

                import socket

                ip = "scanme.nmap.org"

                ports = [21, 22, 80, 443]

                for port in ports:
                      
                      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                      s.settimeout(1)
                      
                      result = s.connect_ex((ip, port))
                      
                      if result == 0:
                            print(f"Port {port} ouvert.")
                            s.close()

              except Exception as e:
                    print(f"{e}")

        else:
              print("La commande est incorrecte ou éxiste pas.")
              