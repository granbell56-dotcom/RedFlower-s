
import os as o
import sys as s
import subprocess

from colorama import Fore, Style, init
init(autoreset=True)

versp = Fore.MAGENTA + "->" + Fore.RESET
texte = Fore.CYAN + "Liste des commandes" + Fore.RESET


def crow():
    from PONT import pont_espa

    print()
    print(Fore.LIGHTBLACK_EX + "Crow ; Version 2 [ RedFlower's Edition ] | Developed by LUUXO"  + Fore.RESET)
    print()


    while True:
        print()
        print("help- para ver la lista de comandos")
        print()

        try:
            command = input(">>> ").lower()
        
        except KeyboardInterrupt:
            print("Ctrl c Detectado.")
            continue

        if command == "help-":

            print()
            print(f"┌──────/[  {texte}  ]/─>")
            print("│")
            print("│", Fore.LIGHTYELLOW_EX + " pr; " + Fore.RESET, f"{versp}  ", Fore.LIGHTGREEN_EX + "Para mostrar texto" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " Is*  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Para listar los archivos en la carpeta actual" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cd -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Para cambiar de directorio" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cwd*   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra el directorio actual" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " cls   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Limpia la pantalla" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " run -   " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Ejecuta comandos del sistema" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tree  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra la estructura del directorio de forma gráfica" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " tl-  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra todas las tareas en ejecución, incluyendo los servicios" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vrfy  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Pide a Windows verificar si los archivos se escribieron correctamente en el disco" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " vol  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra el nombre y número de serie de un volumen de disco" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " DIR  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra la lista de archivos y subdirectorios de un directorio" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " VER  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra la versión de Windows" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " SYSINFO  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra la configuración y propiedades del sistema" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " sysdm  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Propiedades del sistema de Windows" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " appwiz  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Panel de control de Windows" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " MyIp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Muestra la información de tu IP" + Fore.RESET)
            print("│", Fore.LIGHTYELLOW_EX + " ScNp  " + Fore.RESET, f"{versp} ", Fore.LIGHTGREEN_EX + "Escanea los puertos 21, 22, 80, 443" + Fore.RESET)
            print("│")
            print("└────────────────[", Fore.LIGHTGREEN_EX + "SUCESS", Fore.WHITE + "]" + Fore.RESET)

        elif command == "exit":
            pont_espa()
        
        elif command.startswith("pr;"):
            mensaje = command[3:]
            print(mensaje)

        elif command.startswith("is*"):
            mensaje = command[3:]
            for archivo in o.listdir():
                print(Fore.CYAN + archivo)
        
        elif command.startswith("cd -"):
            ruta = command[4:].strip()
            try:
                o.chdir(ruta)
                print(Fore.GREEN + f"Directorio cambiado: {o.getcwd()}")

            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        elif command.startswith("cwd*"):
            print(Fore.YELLOW + f"Directorio actual: {o.getcwd()}")
        
        elif command.startswith("cls"):
            mensaje = command[3:]
            o.system('cls')
        
        elif command.startswith("run -"):
            cmd = command[5:].strip()
            
            try:
                salida = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                print(Fore.GREEN + salida)

            except subprocess.CalledProcessError as e:
                print(Fore.RED + "Error al ejecutar:", e.output)
        
        elif command.startswith("tree"):
            mensaje = command[4:]
            try:
                o.system('tree')

            except Exception as e:
                pass
              
        elif command.startswith("color"): # comando secreto
            mensaje = command[5:]
            if command == "a":
                o.system('color a')
            else:
                pass
        
        elif command.startswith("tl-"):
            try:
                mensaje = command[3:]
                o.system('tasklist')

            except Exception as e:
                print(f"{e}")

        elif command.startswith("vrfy"):
            mensaje = command[4:]
            try:
                o.system('verify')
                        
            except Exception as e:
                print(f"{e}")
        
        elif command.startswith("vol"):
            try:
                mensaje = command[3:]
                o.system('vol')

            except Exception as e:
                print(f"{e}")

        elif command.startswith("dir"):
            try:
                mensaje = command[3:]
                o.system('dir')
                    
            except Exception as e:
                print(f"{e}")
            
        elif command.startswith("ver"):
            mensaje = command[3:]
            o.system('ver')
        
        elif command.startswith("sysinfo"):
            mensaje = command[7:]
            o.system('systeminfo')

        elif command.startswith("sysdm"):
            mensaje = command[5:]
            o.system('sysdm.cpl')
        
        elif command.startswith("appwiz"):
            mensaje = command[6:]
            o.system('appwiz.cpl')

        elif command.startswith("myip"):
            mensaje = command[4:]

            try:
                import requests
                import socket
              
                ip = requests.get("https://api.ipify.org").text

                url = f"http://ip-api.com/json/{ip}"
                respuesta = requests.get(url)

                datos = respuesta.json()

                print("IP:", datos["query"])

                nombre_equipo = socket.gethostname()
                ip_local = socket.gethostbyname(nombre_equipo)

                print("IP local:", ip_local)

                print("País:", datos["country"])
                print("Región:", datos["regionName"])
                print("Ciudad:", datos["city"])
                print("ISP:", datos["isp"])
                print("Latitud:", datos["lat"])
                print("Longitud:", datos["lon"])
                print("-------------------------")

                datos = requests.get("https://ipwho.is/").json()
                print("IP :", datos["ip"])
                print("VPN/Proxy :", datos["connection"]["proxy"])
                print("Tor :", datos["connection"]["tor"])
                print('--------------------------')

                datos = requests.get("https://ipinfo.io/json").json()
                print("Organización:", datos["org"])
                print("ASN:", datos["asn"]["asn"] if "asn" in datos else "Desconocido")

            except Exception as e:
                print(f"{e}")
        
        elif command.startswith("scnp"):
            mensaje = command[5:]

            try:
                import socket

                ip = "scanme.nmap.org"
                puertos = [21, 22, 80, 443]

                for puerto in puertos:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    resultado = s.connect_ex((ip, puerto))
                    if resultado == 0:
                        print(f"Puerto {puerto} abierto.")
                        s.close()

            except Exception as e:
                print(f"{e}")

        else:
            print("El comando es incorrecto o no existe.")
            