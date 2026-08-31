
# Terminal

from colorama import Fore, init
import time as t
import os as o

from Menu_ANGL import MenuANG
from Menu_FR import MenuFR
from Menu_ESPA import MenuESP

from Histoire import history

init()

texte = Fore.LIGHTRED_EX + "Choose your language" + Fore.RESET
texte_input = Fore.WHITE + "What do you want to do ? " +  Fore.RESET
carractere_end = Fore.LIGHTBLACK_EX + "]"  + Fore.RESET
carractere = Fore.WHITE + " : " + Fore.RESET

def HackrowFlowers():
    
   while True:
        try:
           
           print()
           print(Fore.LIGHTBLACK_EX + "Hackrow-Terminal ; Version 2 [ RedFlower's Edition ] Developed by LUUXO "  + Fore.RESET)
           print()
           print()

           print(Fore.LIGHTBLACK_EX + "developed by Luuxo" + Fore.RESET); print()

           print(Fore.LIGHTBLACK_EX + f"┌─────[{texte}", Fore.LIGHTBLACK_EX + "]─────[>]" + Fore.RESET)
           print(Fore.LIGHTBLACK_EX + f"│ ", Fore.LIGHTYELLOW_EX + "/1 English " + Fore.RESET)
           print(Fore.LIGHTBLACK_EX + f"│ ", Fore.LIGHTYELLOW_EX + "/2 French ( Defeault language )" + Fore.RESET)
           print(Fore.LIGHTBLACK_EX + f"│ ", Fore.LIGHTYELLOW_EX + "/3 Spanish " + Fore.RESET)
           print(Fore.LIGHTBLACK_EX + f"│ ", Fore.LIGHTYELLOW_EX + "/4 Leave " + Fore.RESET)
           
           try:
              
              languages = input(Fore.LIGHTBLACK_EX + f"└─────────[ {texte_input}{carractere_end}{carractere}" + Fore.RESET).lower()

           except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + "Ctrl c Detected." + Fore.RESET)
            continue

           print()

           if languages == "1":
             o.system("cls")
             MenuANG()
              
           elif languages == "2":
             MenuFR()

           elif languages == "3":
             MenuESP()

           elif languages == "4":
             print("Closing the current program...")
             t.sleep(1)
             break
           
           elif languages == "history":
              o.system("cls")
              history()
              
           else:
             print(Fore.LIGHTRED_EX + "Choose a number between 1 and 3 to select a language and 4 for leave the program." + Fore.RESET)

        except Exception as e:
           print(Fore.LIGHTRED_EX + f"Invalid entry 'error -> {e} '" + Fore.RESET)
           
