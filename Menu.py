
from colorama import Fore, init
from Hackrow_RedFlowers import HackrowFlowers
from Banner_Grabbing import Banner_Grabbing_
from Serveur_IP_Flask import Serveur_Dashboard
from Copy_Site import Copy_Site
from Computer import Computer_Information
from Net_Speed import Download_upload

import os as o
import sys as s
import subprocess as sub
import time as t

import ipaddress

import socket

import whois

import pyshark

import asyncio

import nmap

from Injection import Labo_A_Injection


# ====== LOG ========

logger_invalide = []

logger_valide = []

logger_error = []

logger_autre = []

logger_name = []

# ===================


init()

ico = Fore.LIGHTRED_EX +"RedFlower's" + Fore.RESET # <-- met le texte en rouge
vers = Fore.LIGHTGREEN_EX + "->" + Fore.RESET # <-- direction en vert
versp = Fore.MAGENTA + "->" + Fore.RESET # <-- direction en violet


print(Fore.LIGHTBLACK_EX + "developed by Luuxo" + Fore.RESET)

print()

print(Fore.LIGHTBLACK_EX + "┌───────────────[LIST OF BETA TESTERS]──────────────────/─>" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│  User name ( Discord ): luuxo2455_17235 | .luuxosozen. " + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│  User name ( Instagram ) : levraitwisty ( Twisty ) | luuxo43 ( Luuxo La ) " + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│  [Message from the developer ( LUUXO ) ] Thanks to the beta tester :) " + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "└────────────────────────────────────────────────────────/─>" + Fore.RESET)

print()
print()

name = input("Entre ton nom : ").lower() # <-- Met la sorti tout en miniscule
name = Fore.LIGHTBLUE_EX + name.capitalize() + Fore.RESET # <-- Applique la couleur bleu et met la premierre lettre en Majuscule puis met fin a la coleur

logger_name.append(f" User Name : {name}")

def menu():

    sym = Fore.LIGHTBLACK_EX + "@" + Fore.RESET

    o.system("cls")

    while True:
        
        try:
            
            print()
            
            print(f"┌───({ico}{sym}{name})-[~]") # <-- Header du terminal 
            print(Fore.WHITE + "│" + Fore.RESET) # <-- Assemblage
            command = input(Fore.WHITE + "└$ " + Fore.RESET).lower() # <-- Capture l'entrée avec un design

            

            if command in commands:
                logger_valide.append(f" Commande : {command}")
                commands[command]()


            elif command == "get-networkinfo":
                logger_valide.append(f" Commande : get-networkinfo")
                asyncio.run(Information_Sur_Le_Reseau())
            
            elif command == "-scan":
                logger_valide.append(f" Commande : -scan")
                asyncio.run(Scanne_De_Port())

            elif command == "-banner_grabbing":
                logger_valide.append(f" Commande : -banner_grabbing")
                asyncio.run(Banner_Grabbing_())

            else:
                logger_invalide.append(f" Commande invalide : {command}")
                print(Fore.LIGHTRED_EX + "Votre entrée ne semble pas éxister. Utilisez la commande [ Get-Help ] pour afficher la liste des commandes." + Fore.RESET)

        except KeyboardInterrupt as e:
            logger_error.append(" Ctrl + C : KeyboardInterrupt()")
            print(Fore.LIGHTRED_EX + f"Ctrl + C détécter" + Fore.RESET)
            

        except Exception as e:
            logger_autre.append(f" Autre erreur : {e}")
            print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)



def Effacer_Terminal():

    o.system('cls')


def Sortie_De_Programme():
    
    print("Merci d'avoir utilisé RedFlower's")
    t.sleep(1)

    print("Fin de programme dans 3 secondes.")
    t.sleep(3)

    s.exit()



def Liste_Des_Commands():
    
    print(f"""
                      
┌─/[Liste des commandes]/─>
│
│============| Commandes de base |============│
│
│ Get-Help             {vers}      Affiche la liste des commandes disponibles
│ Clear                {vers}      Efface l'écran du terminal
│ Get-Log              {vers}      Affiche les Logs
│
│============| Hackrow-Terminal ( RedFlower's Edition ) |============│
│
│ Run-Hackrow.exe      {vers}      Terminal inspiré de Linux et C, développé par LUUXO 
│
│============| Ordinateur |============│
│
│ Get-ComputerType     {vers}      Affiche des informations détaillées du système
│ Get-ComputerInfo     {vers}      Affiche des informations détaillées sur la capacité du système
│ -HostInfo            {vers}      Tente de crée une identité à partir d'une adresse IP
│ run-dashboard        {vers}      Crée un serveur en HTTP pour afficher un dashboard ( RedFlower's dois redémaré pour démaré le serveur une secondes fois )
│ 
│============| Réseau / Scanne |============│
│
│ Get-NetworkInfo      {vers}      Affiche toutes les informations réseau
│ Get-Hop              {vers}      Affiche les routeurs traversés pour atteindre une destination
│ Get-Helper           {vers}      Liste les outils d'assistance disponibles
│ Net-Speed            {vers}      Surveille en temps réel le débit réseau (upload / download) en Mo/s dans le terminal
│
│ -Interface -Add      {vers}      Affiche la configuration des adresses de l'interface
│ -Interface -Ip       {vers}      Affiche la configuration IP et DNS de l'interface
│ -Interface           {vers}      Affiche les informations de l'interface réseau
│
│ -Scan                {vers}      Scan des ports d'une IP cible (NMAP)
│ -Shark               {vers}      Analyse passive du trafic réseau (Wireshark)
│ -Reverse /DNS        {vers}      Lance un reverse DNS pour tenté de récupérer le Hostname de l'IP cible
│ -PortCheck           {vers}      Teste rapidement si un port spécifique est ouvert sur une adresse IP cible
│ -Whois               {vers}      Récupère les informations d'un domaine (registrar, dates, propriétaire, etc.)
│ -Banner_Grabbing     {vers}      Lance un Banner Grabbing sur l'IP cible (NMAP)
│
│============| Service utilisé |============│
│
│ -Tools               {vers}      Affiche les outils utilisés par RedFlower's et leurs sites officiels
│
│============| Site Web |============│
│
│ -Copy_Site           {vers}      Permet de copier un site Web à partir d'une URL
│
│============| Teste d'Injection |============│
│
│ -Inject              {vers}      Lance le laboratoire de test d'injection
│
└───────────────────────────────────────────│
""")


def Address_Et_Interface():

    print()
    
    try:
        
        cmd = ["netsh", "interface", "ip", "show", "addresses"]
        
        result = sub.run(
            cmd,
            capture_output=True
        )
        
        if result.stdout:
            output = result.stdout.decode("cp850", errors="ignore")
            print(Fore.LIGHTYELLOW_EX + output + Fore.RESET)
            
        if result.stderr:
            error = result.stderr.decode("cp850", errors="ignore")
            print(Fore.LIGHTRED_EX + error + Fore.RESET)
        
        input()
        
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + C détecté" + Fore.RESET)
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)


def Configuration_Ip_Et_Dns_Interface():

    print()
    
    try:
        
        cmd = ["netsh", "interface", "ip", "show", "dns"]
        
        result = sub.run(
            cmd,
            capture_output=True
        )
        
        if result.stdout:
            output = result.stdout.decode("cp850", errors="ignore")
            print(Fore.LIGHTYELLOW_EX + output + Fore.RESET)
            
        if result.stderr:
            error = result.stderr.decode("cp850", errors="ignore")
            print(Fore.LIGHTRED_EX + error + Fore.RESET)
        
        input()
        
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + C détecté" + Fore.RESET)
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)



def  Outils_Et_Assistance():

    print()
    
    try:
        
        cmd = ["netsh", "show", "helper"]
        
        result = sub.run(
            cmd,
            capture_output=True
        )
        
        if result.stdout:
            output = result.stdout.decode("cp850", errors="ignore")
            print(Fore.LIGHTYELLOW_EX + output + Fore.RESET)
            
        if result.stderr:
            error = result.stderr.decode("cp850", errors="ignore")
            print(Fore.LIGHTRED_EX + error + Fore.RESET)
        
        input()
        
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + C détecté" + Fore.RESET)
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)



def Information_Interface_Reseau():

    print()
    
    try:
        
        cmd = ["netsh", "interface", "show", "interface"]
        
        result = sub.run(
            cmd,
            capture_output=True
        )
        
        if result.stdout:
            output = result.stdout.decode("cp850", errors="ignore")
            print(Fore.LIGHTYELLOW_EX + output + Fore.RESET)
            
        if result.stderr:
            error = result.stderr.decode("cp850", errors="ignore")
            print(Fore.LIGHTRED_EX + error + Fore.RESET)
        
        input()
        
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + C détecté" + Fore.RESET)
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)



def Hackrow_Terminal():

    print()

    o.system("cls")

    HackrowFlowers()



def Outils_Utiliser():
        
        site = "site"
        site = Fore.LIGHTBLUE_EX + site.capitalize() + Fore.RESET

        liste = "liste des services"
        liste = Fore.LIGHTRED_EX + liste.capitalize() + Fore.RESET

        sit = Fore.LIGHTYELLOW_EX + " Site"  + Fore.RESET

        print(Fore.LIGHTBLACK_EX + f"┌─/[{liste}", Fore.LIGHTBLACK_EX + f"]/─>[~{site}", Fore.LIGHTBLACK_EX +"~]" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX +"│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "Python 3.14 (64-bit)", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX +"│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│ ", Fore.WHITE + f"Description   {vers}   ", Fore.WHITE +"Python est un langage de programmation simple et puissant, utilisé pour automatiser des tâches, analyser des données, développer des applications et faire de la cybersécurité." + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {sit}  {versp}   ", Fore.CYAN + "https://www.python.org/" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX +"│============| ", Fore.WHITE + "VSCode-x64-1.108.0", Fore.LIGHTBLACK_EX + "|============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│", Fore.WHITE + f" Description   {vers}  ", Fore.WHITE + "Visual Studio Code (VS Code) est un éditeur de code léger et puissant qui permet d'écrire, exécuter et déboguer des programmes dans de nombreux langages, dont Python." + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {sit}  {versp}   ", Fore.CYAN + "https://code.visualstudio.com/" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "Nmap-7.98", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│ ", Fore.WHITE + f"Description   {vers}   ", Fore.WHITE  + "Nmap est un outil d'analyse réseau qui permet de découvrir des hôtes, scanner des ports et identifier des services à des fins d'administration ou de sécurité." + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {sit}  {versp}   ", Fore.CYAN + "https://nmap.org/" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│============| ", Fore.WHITE + "WireShark-4.4.13-x64", Fore.LIGHTBLACK_EX + " |============│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│ ", Fore.WHITE + f"Description   {vers}   ", Fore.WHITE + "Wireshark est un analyseur de paquets réseau qui capture et inspecte le trafic en temps réel pour le débogage, l'analyse ou la sécurité." + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + f"│ {sit}  {versp}   ", Fore.CYAN + "https://www.wireshark.org/" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "│" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "└────────────────────────────────────────────────│" + Fore.RESET)



def Information_Systeme():
    
    o.system("color 8")
    o.system("systeminfo")

    print()
    
    print(Fore.LIGHTBLACK_EX + "─────────────────" + Fore.RESET)
    print(Fore.LIGHTBLACK_EX + "System : ",o.name + Fore.RESET)
    print(Fore.LIGHTBLACK_EX + "Platform : ", s.platform + Fore.RESET)
    print(Fore.LIGHTBLACK_EX + "─────────────────" + Fore.RESET)



def Routeur_Vers_Destination():

    print()

    print(Fore.LIGHTCYAN_EX + "Cette comment peut être soummise à des problèbles éthique." + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Assurez-vous d'utiliser cette commande sur votre réseau [ machine / site / routeur ] sur la quelle vous ête explicitement autorisé." + Fore.RESET); print()

    auth = input("J'ai lu et comprend les risque que ça peut engendré ( O / N )  : ").lower()

    if auth != "o":
        print(Fore.LIGHTRED_EX + "Engagement refusé. Commande interdite." + Fore.RESET)
        return

    else:
        o.system("cls")
        
        nom_cible = input("Entre la cible [IP ou nom de domaine] : ")
        sub.run(["tracert", nom_cible])



async def Information_Sur_Le_Reseau():

    o.system("cls")

    print()

    o.system("ipconfig /all")

    print()

    o.system("netstat")
    o.system("netstat -ano")
    o.system("netstat -b")

    print()

    o.system("arp -a -v")

    print()

    o.system("route print")

    print()

    o.system("getmac")

    print()

    choix = input("Afficher les détail Wifi (O/N) ? : ").lower()

    if choix == "o":
        
        print()

        print(Fore.LIGHTBLUE_EX + "[=====WIFI=====]" + Fore.RESET)
        
        print()
        
        o.system("netsh interface show interface")
        o.system("netsh wlan show profiles")
        o.system("netsh wlan show interfaces")
        o.system("netsh wlan show drivers")
        o.system("netsh wlan show networks mode=bssid")

        print()

        choix = input("Afficher les détail DNS (O/N) ? : ").lower()

        if choix == "o":

            print()

            print(Fore.LIGHTYELLOW_EX + "[=====DNS=====]" + Fore.RESET)

            print()

            o.system("ipconfig /displaydns")

            print()

            choix = input("Afficher les détail du Pare-Feu (O/N) ? : ").lower()

            if choix == "o":
                
                print()

                print(Fore.LIGHTRED_EX + "[=====Pare-Feu=====]" + Fore.RESET)

                print()

                o.system("netsh advfirewall firewall show rule name=all")

                print()

                print(Fore.LIGHTGREEN_EX + "La commande sais fini sans problème" + Fore.RESET)

                print()

                input("Appuie sur ' Entrée ' pour finir la commande.")
            
            else:
                print("La commande a pris fin")
                t.sleep(1)

        else:
            print("La commande a pris fin")
            t.sleep(1)
    
    else:
        print("La commande a pris fin")
        t.sleep(1)



async def Scanne_De_Port():

    print()

    print(Fore.LIGHTRED_EX + "Attention !" + Fore.RESET, Fore.LIGHTCYAN_EX + "Cette action peut être soumise à des restrictions légales selon la cible." + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Utilise UNIQUEMENT les IP dont tu a l'autorisation. Exemple Ip : 127.0.0.1 | Exemple Reseaux : 192.0.X.X/24" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Pour continuer tu dois t'engager à utiliser ce scan de façon purement éthique" + Fore.RESET)

    print()

    verify = input("Tu t'engage à utiliser le scan de façon purement éthique (O/N) ? : ").lower()

    print()

    if verify == "o":
        print(Fore.GREEN + "== Scanne autorisé ==" + Fore.RESET)

        t.sleep(1)

        o.system("cls")

        scanner = nmap.PortScanner()
        
        network = input("Entre une IP ou un réseau : ")
        
        print(f"\n[~]-> Scan léger en cours sur : {network}\n")
        
        scanner.scan(
            hosts=network,
            arguments="-T2 --top-ports 20 --open -sS"
            
        )
        
        for host in scanner.all_hosts():
            if scanner[host].state() == "up":

                print("=" * 50)
                print(f"[@]-> IP active : {host}")
                print()
                
                for proto in scanner[host].all_protocols():

                    print(f"    Protocole : {proto}")
                    ports = scanner[host][proto].keys()
                    
                    for port in sorted(ports):

                        service = scanner[host][proto][port]["name"]
                        state = scanner[host][proto][port]["state"]
                        
                        print(
                            f"{Fore.LIGHTCYAN_EX}Port {Fore.LIGHTYELLOW_EX}{port:<5} | "
                            f"{Fore.LIGHTCYAN_EX}État : {Fore.LIGHTYELLOW_EX}{state:<5} | "
                            f"{Fore.LIGHTCYAN_EX}Service : {Fore.LIGHTYELLOW_EX}{service}"
                            )
            print()
            print(Fore.LIGHTGREEN_EX + "Le Scanne sais fini sans problème" + Fore.RESET)

    else:
        print(Fore.LIGHTRED_EX + "Engagement refuser. Scanne interdi." + Fore.RESET)



def Sniffing_Reseau():
        
        asyncio.set_event_loop(asyncio.new_event_loop())

        print()
        
        print(Fore.LIGHTRED_EX + "Attention !" + Fore.RESET, Fore.LIGHTCYAN_EX + "Cette action peut être soumise à des restrictions légales selon la cible." + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + "Utilise UNIQUEMENT les Réseaux dont tu a l'autorisation." + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + "Pour continuer tu dois t'engager à utiliser ce scan de façon purement éthique" + Fore.RESET)
        print(Fore.LIGHTBLACK_EX + "[ Des permitions Administrateur seront requise. ]" + Fore.RESET)
        
        print()
        
        verify = input("Tu t'engage à utiliser le scan de façon purement éthique (O/N) ? : ").lower()
        
        print()

        if verify == "o":
            print(Fore.GREEN + "== Sniffing réseaux autorisé ==" + Fore.RESET)
            
            o.system("cls")
            
            cap = pyshark.LiveCapture(
                
                interface="Ethernet",
                tshark_path=r"C:\Program Files\Wireshark\tshark.exe"
            
            )
            
            try:

                for packet in cap.sniff_continuously(packet_count=5):
                    print(packet)
            
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nArrêt manuel du sniffing." + Fore.RESET)
                return
                
            finally:
                cap.close()
                print(Fore.GREEN + "Capture réseau terminée proprement." + Fore.RESET)
        
        else:
            print(Fore.LIGHTRED_EX + "Engagement refuser. Sniffing réseaux interdit." + Fore.RESET)



def Reverse_DNS():

    print()

    print(Fore.LIGHTRED_EX + "Attention !" + Fore.RESET, Fore.LIGHTCYAN_EX + "Cette action peut être soumise à des restrictions légales selon la cible." + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Utilise UNIQUEMENT les IP dont tu a l'autorisation. Exemple Ip : 127.0.0.1 |" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Pour continuer tu dois t'engager à utiliser ce scan de façon purement éthique" + Fore.RESET)
    print()

    print()

    verify = input("Tu t'engage à utiliser le Reverse DNS de façon purement éthique (O/N) ? : ").lower()

    print()

    o.system("cls")

    if verify == "o":
        print(Fore.GREEN + "== Reverse DNS autorisé ==" + Fore.RESET)

        print()

        ip = input("Entre un IP : ")

        print()

        try:

            ipaddress.ip_address(ip)
        
        except ValueError as e:
            print()

        try:

            hostname, aliaslist, iplist = socket.gethostbyaddr(ip)

            print(Fore.LIGHTCYAN_EX + f"Hostname : " + Fore.LIGHTYELLOW_EX + f"{hostname} | {aliaslist} | {iplist}")

        except ValueError:
            print("IP invalide")
            return
            
            print()

        print("Hostname : inconnu")

        print()

        print(Fore.LIGHTGREEN_EX + "Le Reverse DNS sais fini sans problème" + Fore.RESET)

        input()

    else:
        print(Fore.LIGHTRED_EX + "Engagement refuser Reverse DNS interdi." + Fore.RESET)



def Identiter_Depuis_Ip():

    texteHost = Fore.LIGHTWHITE_EX + "Résultat du scan" + Fore.RESET

    esp = Fore.LIGHTBLACK_EX + "│"  + Fore.RESET

    textefin = Fore.LIGHTGREEN_EX + "Scan terminé sans problème." + Fore.RESET

    bar =  Fore.LIGHTBLACK_EX + "]" + Fore.RESET

    barr = Fore.LIGHTBLACK_EX + "]/─>" + Fore.RESET

    print()
    print(Fore.LIGHTRED_EX + "Attention !" + Fore.RESET, Fore.LIGHTCYAN_EX + "Cette action peut être soumise à des restrictions légales selon la cible." + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Utilise UNIQUEMENT les IP dont tu as l'autorisation. Exemple : 127.0.0.1" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Pour continuer tu dois t'engager à utiliser ce scan de façon éthique" + Fore.RESET)
    print()

    verify = input("Tu t'engages (O/N) ? : ").lower()
    print()

    o.system("cls")

    if verify != "o":
        print(Fore.LIGHTRED_EX + "Engagement refusé. Reconstruction interdite." + Fore.RESET)
        return
    
    o.system("cls")

    print(Fore.GREEN + "== Reconstruction autorisée ==" + Fore.RESET)

    print()

    network = input("Entre une IP : ")

    try:
        
        ipaddress.ip_address(network)  # Vérifie que c'est une IP valide
        
    except ValueError:
        print("IP invalide")
        return

    print()

    try:

        hostname, aliaslist, iplist = socket.gethostbyaddr(network)

    except:

        hostname = "inconnu"
        aliaslist = []
        iplist = []

    scanner = nmap.PortScanner()

    print(f"\n[~]-> Scan en cours sur : {network}\n")

    try:

        scanner.scan(
            hosts=network,
            arguments="-sT -T4 --top-ports 100 --open -sV"
        )

    except Exception as e:
        print("Erreur scan :", e)
        input()
        return

    for host in scanner.all_hosts():

        if scanner[host].state() == "up":

            print()

            print(Fore.LIGHTBLACK_EX + f"┌─/[{texteHost}{barr}" + Fore.RESET)

            print(f"{esp}")

            print(f"{esp}", Fore.LIGHTGREEN_EX + f"[@]-> IP active : {host}" + Fore.RESET)

            print(f"{esp}")

            print(f"{esp}", Fore.LIGHTCYAN_EX + "Hostname : " + Fore.LIGHTYELLOW_EX + f"{hostname}" + Fore.RESET)

            print(f"{esp}")

            if 'osmatch' in scanner[host] and scanner[host]['osmatch']:

                os_name = scanner[host]['osmatch'][0]['name']
                print(f"{esp} ", Fore.LIGHTCYAN_EX + "OS probable : " + Fore.LIGHTYELLOW_EX + os_name + Fore.RESET)

                print(f"{esp}")

            else:
                print(f"{esp}", Fore.LIGHTCYAN_EX + "OS probable : " + Fore.LIGHTYELLOW_EX + "inconnu" + Fore.RESET)
            
                print(f"{esp}")

            for proto in scanner[host].all_protocols():

                print(f"{esp}", Fore.LIGHTMAGENTA_EX + f"Protocole : {proto}" + Fore.RESET)

                ports = scanner[host][proto].keys()

                print(f"{esp}")

                for port in sorted(ports):

                    data = scanner[host][proto][port]
                    service = data.get("name", "unknown")
                    state = data.get("state", "unknown")

                    print(f"{esp}", Fore.LIGHTCYAN_EX + f"Port {port:<5} | " + Fore.LIGHTYELLOW_EX + f"{state:<5} | {service}" + Fore.RESET)
                          

            print(f"{esp}")
            
    print(f"{esp}", Fore.LIGHTBLUE_EX + "[~]-> Traceroute" + Fore.RESET)

    print(f"{esp}")

    print(Fore.LIGHTBLACK_EX + "-")

    sub.run(["tracert", network])

    print(Fore.LIGHTBLACK_EX + "_")

    print(f"{esp}")

    print(Fore.LIGHTBLACK_EX + f"└───────────────────────────────────────────│[{textefin}{bar}" + Fore.RESET)

    input()



def Teste_De_Port_Specifique():

    texteHost = Fore.LIGHTWHITE_EX + "Résultat de PortCheck" + Fore.RESET

    textefin = Fore.LIGHTGREEN_EX + "PortCheck terminé sans problème." + Fore.RESET

    barr = Fore.LIGHTBLACK_EX + "]/─>" + Fore.RESET

    bar =  Fore.LIGHTBLACK_EX + "]" + Fore.RESET

    esp = Fore.LIGHTBLACK_EX + "│"  + Fore.RESET

    print("\n== PortCheck ==\n")

    ip = input("IP : ")
    port = input("Port : ")

    # Sécurité IP
    try:

        ipaddress.ip_address(ip)

    except:
        print("IP invalide")
        return

    # Sécurité port
    if not port.isdigit():

        print("Port invalide")
        return

    port = int(port)

    if port < 0 or port > 65535:
        print("Port hors limite")
        return
    
    o.system("cls")

    print("\n[~] Test en cours...\n")

    print()

    s = socket.socket()
    s.settimeout(1)

    start = t.time()

    try:

        print(Fore.LIGHTBLACK_EX + f"┌─/[{texteHost}{barr}" + Fore.RESET)

        s.connect((ip, port))

        print(esp)

        print(f"{esp}[OPEN] {Fore.LIGHTYELLOW_EX}{ip}:{port}")

    except:

        print(esp)

        print(f"{esp} {Fore.LIGHTCYAN_EX}[CLOSED] {Fore.LIGHTYELLOW_EX}{ip}:{port}")

    print(Fore.LIGHTBLACK_EX + f"└────────────────│[{textefin}{bar}" + Fore.RESET)

    end = t.time()
    print(f"Temps : {round(end - start, 3)} sec")

    s.close()
    input()



def Information_Sur_Un_Domaine():

    texteHost = Fore.LIGHTWHITE_EX + "Résultat de Whois" + Fore.RESET

    escc = Fore.LIGHTBLACK_EX + "└───────────|" + Fore.RESET

    textefin = Fore.LIGHTGREEN_EX + "Whois terminé sans problème." + Fore.RESET

    barr = Fore.LIGHTBLACK_EX + "]/─>" + Fore.RESET

    bar =  Fore.LIGHTBLACK_EX + "]" + Fore.RESET

    esp = Fore.LIGHTBLACK_EX + "│"  + Fore.RESET

    print("\n== Whois ==\n")

    domain = input("Domaine (ex: google.com) : ").strip()

    if "." not in domain:
        print("Domaine invalide")
        return
    
    o.system("cls")

    print("\n[~] Recherche...\n")

    try:

        info = whois.whois(domain)

        print(Fore.LIGHTBLACK_EX + f"┌─/[{texteHost}{barr}" + Fore.RESET)

        print(escc)
        
        print(f"{esp} {Fore.LIGHTCYAN_EX}Nom : {Fore.LIGHTYELLOW_EX}{info.domain_name}{Fore.RESET}")
        
        print(escc)
        
        print(f"{esp} {Fore.LIGHTCYAN_EX}Registrar : {Fore.LIGHTYELLOW_EX}{info.registrar}{Fore.RESET}")
        
        print(escc)
        
        print(f"{esp} {Fore.LIGHTCYAN_EX}Création : {Fore.LIGHTYELLOW_EX}{info.creation_date}{Fore.RESET}")
        
        print(escc)
        
        print(f"{esp} {Fore.LIGHTCYAN_EX}Expiration : {Fore.LIGHTYELLOW_EX}{info.expiration_date}{Fore.RESET}")
        
        print(escc)
        
        print(f"{esp} {Fore.LIGHTCYAN_EX}Pays : {Fore.LIGHTYELLOW_EX}{info.country}{Fore.RESET}")

        print(escc)

        print(Fore.LIGHTBLACK_EX + f"└────────────────│[{textefin}{bar}" + Fore.RESET)

    except Exception as e:
        print("Erreur Whois :", e)

    input()


def Log():

    user_name = Fore.LIGHTBLUE_EX + "Name User" + Fore.RESET

    commande_valide = Fore.CYAN + "Commande Valide" + Fore.RESET

    commande_invalide = Fore.LIGHTRED_EX + "Commande Invalide" + Fore.RESET

    error_text = Fore.LIGHTYELLOW_EX + "Erreur" + Fore.RESET

    error_autre_text = Fore.LIGHTGREEN_EX + "Autre Erreur" + Fore.RESET


    print()
    print(f"┌─/[{user_name}]/─>") # User name
    print("│")

    for element_name in logger_name:
        print(f"│ {element_name}")

    print()
    print(f"┌─/[{commande_valide}]/─>") # Commande valide
    print("│")
    
    for element_valide in logger_valide:
        print(f"│ {Fore.CYAN + element_valide + Fore.RESET}")
    
    print("│")
    print(f"┌─/[{commande_invalide}]/─>") # Commande invalide
    print("│")

    for element_invalide in logger_invalide:
        print(f"│ {Fore.LIGHTRED_EX + element_invalide + Fore.RESET}")
    
    print("│")
    print(f"┌─/[{error_text}]/─>") # Erreur
    print("│")

    for element_erreur in logger_error:
        print(f"│ {Fore.LIGHTYELLOW_EX + element_erreur + Fore.RESET}")
    
    print("│")
    print(f"┌─/[{error_autre_text}]/─>") # Autre erreur
    print("│")

    for element_autre in logger_autre:
        print(f"│ {Fore.LIGHTGREEN_EX + element_autre + Fore.RESET}")
    
    print("└───────────────────────────────────────────│")

commands = {
    "clear": Effacer_Terminal,
    "exit": Sortie_De_Programme,
    "get-help": Liste_Des_Commands,
    "-tools": Outils_Utiliser,
    "get-computertype": Information_Systeme,
    "-shark": Sniffing_Reseau,
    "run-hackrow.exe": Hackrow_Terminal,
    "-inject": Labo_A_Injection,
    "get-hop": Routeur_Vers_Destination,
    "get-helper": Outils_Et_Assistance,
    "interface": Information_Interface_Reseau,
    "-interface -ip": Configuration_Ip_Et_Dns_Interface,
    "-interface -add": Address_Et_Interface,
    "-reverse /dns": Reverse_DNS,
    "-hostinfo": Identiter_Depuis_Ip,
    "-portcheck": Teste_De_Port_Specifique,
    "-whois": Information_Sur_Un_Domaine,
    "run-dashboard": Serveur_Dashboard,
    "-copy_site": Copy_Site,
    "get-computerinfo": Computer_Information,
    "net-speed": Download_upload,
    "get-log": Log,
    
}

