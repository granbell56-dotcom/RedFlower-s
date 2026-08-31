
import os as o
import sys as s
import subprocess

from colorama import Fore, Style, init
init(autoreset=True)

versp = Fore.MAGENTA + "->" + Fore.RESET
texte = Fore.CYAN + "Liste des commandes" + Fore.RESET


def crow():
    from PONT import pont_angl

    print()
    print(Fore.LIGHTBLACK_EX + "Crow ; Version 2 [ RedFlower's Edition ] | Developed by LUUXO"  + Fore.RESET)
    print()


    while True:
        print()
        print("help- for the list of commands")
        print()
        
        try:
            command = input(">>> ").lower()
        
        except KeyboardInterrupt:
           print(f"Ctrl + c Detected.")
           continue

        if command == "help-":
            
            print()
            print(f"┌──────/[  {texte}  ]/─>")
            print("│")
            print("│", Fore.LIGHTYELLOW_EX + " pr; " + Fore.RESET, f"{versp}  ", Fore.LIGHTGREEN_EX + "To display text" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " Is*  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "To list files in the current folder" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cd -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "To change directory" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cwd*   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display the current directory" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cls   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Clear the screen" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " run -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Execute system commands" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tree  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display directory structure graphically" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tl-  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + " Display all running tasks, including services" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vrfy  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Ask Windows to check if your files are written correctly on the disk" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vol  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display the name and serial number of a disk volume" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " DIR  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display the list of files and subdirectories of a directory" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " VER  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display Windows version" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " SYSINFO  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display computer-specific properties and configuration" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " sysdm  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Windows system properties" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " appwiz  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Windows system properties" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " MyIp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Display your IP information" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " ScNp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Scan ports 21, 22, 80, 443" + Fore.RESET)
            print("│")
            print("└────────────────[", Fore.LIGHTGREEN_EX + "SUCESS", Fore.WHITE + "]" + Fore.RESET)

        elif command == "exit":
            pont_angl()
        
        elif command.startswith("pr;"):
            message = command[3:]
            print(message)

        elif command.startswith("is*"):
            message = command[3:]
            for file in o.listdir():
                print(Fore.CYAN + file)
        
        elif command.startswith("cd -"):
            path = command[4:].strip()
            try:
                o.chdir(path)
                print(Fore.GREEN + f"Directory changed: {o.getcwd()}")

            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        elif command.startswith("cwd*"):
            print(Fore.YELLOW + f"Current directory: {o.getcwd()}")
        
        elif command.startswith("cls"):
            message = command[3:]
            o.system('cls')
        
        elif command.startswith("run -"):
            cmd = command[5:].strip()
            
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                print(Fore.GREEN + output)

            except subprocess.CalledProcessError as e:
                print(Fore.RED + "Error during execution:", e.output)
        
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

        elif command.startswith("dir"):
            try:
                message = command[3:]
                o.system('dir')
                    
            except Exception as e:
                print(f"{e}")
            
        elif command.startswith("ver"):
            message = command[3:]
            o.system('ver')
        
        elif command.startswith("sysinfo"):
            message = command[7:]
            o.system('systeminfo')

        elif command.startswith("sysdm"):
            message = command[5:]
            o.system('sysdm.cpl')
        
        elif command.startswith("appwiz"):
            message = command[6:]
            o.system('appwiz.cpl')

        elif command.startswith("myip"):
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

                print("Local IP:", local_ip)

                print("Country:", data["country"])
                print("Region:", data["regionName"])
                print("City:", data["city"])
                print("ISP:", data["isp"])
                print("Latitude:", data["lat"])
                print("Longitude:", data["lon"])
                print("-------------------------")

                data = requests.get("https://ipwho.is/").json()
                print("IP :", data["ip"])
                print("VPN/Proxy :", data["connection"]["proxy"])
                print("Tor :", data["connection"]["tor"])
                print('--------------------------')

                data = requests.get("https://ipinfo.io/json").json()
                print("Organisation:", data["org"])
                print("ASN:", data["asn"]["asn"] if "asn" in data else "Unknown")

            except Exception as e:
                print(f"{e}")
        
        elif command.startswith("scnp"):
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
                        print(f"Port {port} is open.")
                        s.close()

            except Exception as e:
                print(f"{e}")

        else:
            print("Command is incorrect or does not exist.")
            