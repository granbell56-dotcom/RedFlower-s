
import os

def BatchFR():

    try:

        print("   (c) Microsoft Corporation. Tous droits réservés.")
        print("             ' exit ' pour quitter.")
         
        while True:

            from PONT import pont_fr

            print()
            
            command_batch = input(f"{os.getenv('USERNAME')}> ")

            if command_batch == "exit":
                
                pont_fr()

            os.system(command_batch)
    
    except Exception as e:
        print(f"Il y à eu une erreur. -> {e}")
        