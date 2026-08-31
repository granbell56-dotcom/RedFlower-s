
from colorama import Fore, init
import time
from Menu import menu

init(autoreset=True)

def logo():

    print(Fore.RED + r"""

                                                
 █████             █  ██████   █                                  █          
 █   ▓█            █  █        █                                  █          
 █    █  ███    ██▓█  █        █     ███  █░    █  ███    █▒██▒   █    ▒███▒ 
 █   ▒█ ▓▓ ▒█  █▓ ▓█  █        █    █▓ ▓█ ▓▒   ▒█ ▓▓ ▒█   ██  █        █▒ ░█ 
 █████  █   █  █   █  ██████   █    █   █ ░█ █ █▒ █   █   █            █▒░   
 █  ░█▒ █████  █   █  █        █    █   █  █▒█▒█  █████   █            ░███▒ 
 █   ░█ █      █   █  █        █    █   █  █████  █       █               ▒█ 
 █    █ ▓▓  █  █▓ ▓█  █        █░   █▓ ▓█  ▒█▒█▒  ▓▓  █   █            █░ ▒█ 
 █    ▒  ███▒   ██▓█  █        ▒██   ███    █ █    ███▒   █            ▒███▒ 
                                                                             """)
    

    time.sleep(1)
    menu()
    
if __name__ == "__main__":
    logo()
    