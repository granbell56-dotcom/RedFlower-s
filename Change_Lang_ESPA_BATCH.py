
import os

def BatchESPA():

    try:

        print("   (c) Microsoft Corporation. Todos los derechos reservados.")
        print("             ' exit ' para irse.")
        
        while True:

            from PONT import pont_espa

            print()
            
            command_batch = input(f"{os.getenv('USERNAME')}> ")

            if command_batch == "exit":

                pont_espa()

            os.system(command_batch)
    
    except Exception as e:
        print(f"Hubo un error. -> {e}")
        