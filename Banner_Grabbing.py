
import nmap
import asyncio
import itertools
import sys
import os as o
from colorama import Fore, init

init(autoreset=True)

nm = nmap.PortScanner()



async def loading():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        sys.stdout.write(f"\r{Fore.LIGHTCYAN_EX}[+] Scan en cours... {c}")
        sys.stdout.flush()
        await asyncio.sleep(0.1)



def print_block(title, content):
    print(f"\n┌─/[{title}]/─>")
    print("└───────────|")
    print(f"│ {content}")
    print("└───────────|")



async def scan(target):
    print(f"\n{Fore.LIGHTCYAN_EX}[+] Scan sur : {target}\n")

    loader = asyncio.create_task(loading())

    try:
        await asyncio.to_thread(
            nm.scan,
            hosts=target,
            arguments='-sS -sV -O -A -T4 -Pn --script=default,vuln,http-headers,ssl-enum-ciphers'
        )

    finally:
        loader.cancel()
        print(f"\r{Fore.LIGHTGREEN_EX}[+] Scan terminé.            ")

    for host in nm.all_hosts():
        print_block("Résultat de Scan", f"Host : {host}")

        # OS
        if 'osmatch' in nm[host]:
            for osmatch in nm[host]['osmatch']:
                print_block("OS Détecté", f"{osmatch['name']} ({osmatch['accuracy']}%)")

        for proto in nm[host].all_protocols():
            print_block("Protocole", proto.upper())

            for port in nm[host][proto]:
                data = nm[host][proto][port]

                state = data['state']
                service = data['name']
                version = data.get('version', '')

                print(
                    f"{Fore.LIGHTCYAN_EX}Port {Fore.LIGHTYELLOW_EX}{port:<5} | "
                    f"{Fore.LIGHTCYAN_EX}État : {Fore.LIGHTYELLOW_EX}{state:<7} | "
                    f"{Fore.LIGHTCYAN_EX}Service : {Fore.LIGHTYELLOW_EX}{service} "
                    f"{Fore.LIGHTMAGENTA_EX}{version}"
                )

                # Scripts (vuln, http, ssl)
                if 'script' in data:
                    print(f"{Fore.LIGHTBLACK_EX}└─ Scripts :")

                    for script_name, output in data['script'].items():
                        print(f"\n[{Fore.LIGHTCYAN_EX}{script_name}{Fore.RESET}]")
                        print(f"{Fore.WHITE}{output}")
        
        input()



async def Run_Grabbing():
    target = input(f"{Fore.LIGHTCYAN_EX}IP ou domaine : {Fore.RESET}")
    await scan(target)



def Banner_Grabbing_():
    
    print(Fore.LIGHTCYAN_EX + "Cette comment peut être soummise à des problèbles éthique." + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "Assurez-vous d'utiliser cette commande sur votre réseau [ machine / site / routeur ] sur la quelle vous ête explicitement autorisé." + Fore.RESET); print()
    
    auth = input("J'ai lu et comprend les risque que ça peut engendré ( O / N )  : ").lower()

    if auth == "o":
        asyncio.run(Run_Grabbing())
       
    else:
         print(Fore.LIGHTRED_EX + "Engagement refusé. Commande interdite." + Fore.RESET)
         return
    
    

if __name__ == "__main__":
    asyncio.run(Run_Grabbing())
    