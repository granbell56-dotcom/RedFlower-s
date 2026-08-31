# pont entre les fichier

from colorama import Fore, init

import time as t

init()



def pont_fr():

    try:
        from Menu_FR import MenuFR
        
        print("\n")
        print(Fore.LIGHTGREEN_EX + "Redirection en cours..." + Fore.RESET)
        t.sleep(2)
        
        MenuFR()
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)



def pont_angl():

    try:
        
        from Menu_ANGL import MenuANG
        
        print("\n")
        print(Fore.LIGHTGREEN_EX + "Redirection in progress..." + Fore.RESET)
        t.sleep(2)
        
        MenuANG()
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error -> {e}" + Fore.RESET)



def pont_espa():

    try:
        
        from Menu_ESPA import MenuESP
        
        print("\n")
        print(Fore.LIGHTGREEN_EX + "Redirección en progreso..." + Fore.RESET)
        t.sleep(2)
        
        MenuESP()
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error -> {e}" + Fore.RESET)


def pont_flower():

    try:
        
        from Menu import menu
        
        print("\n")
        print(Fore.LIGHTRED_EX + "RedFlower's" + Fore.RESET)
        t.sleep(1)
        
        menu()
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error -> {e}" + Fore.RESET)
