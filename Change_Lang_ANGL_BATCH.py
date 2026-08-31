
import os

def BatchANGL():

    try:

        print("   (c) Microsoft Corporation. All rights reserved.")
        print("           ' exit ' for leave.")
        
        while True:

            from PONT import pont_angl

            print()
            
            command_batch = input(f"{os.getenv('USERNAME')}> ")

            if command_batch == "exit":

                pont_angl()

            os.system(command_batch)
    
    except Exception as e:
        print(f"There was an error. -> {e}")
        