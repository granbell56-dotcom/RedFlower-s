
def pyESPA():
    from PONT import pont_espa
    
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Los comandos de Python deben escribirse en inglés.")
        print('Escribe `exit` para salir del modo Python.')
        print('Usa `print()`, `for`, `def`, etc.\n')

        # Modo seguro activado
        modo_seguro = True

        # Comandos prohibidos en modo seguro
        comandos_prohibidos = [
            "import os", "import sys", "import subprocess", "import socket",
            "from socket", "__import__", "eval(", "exec(", "open(", "compile(",
            "globals(", "locals(", "input("
        ]

        while True:

            try:
                comando = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c Detectado.")
                continue

            if comando.strip().lower() == "exit":
                print("Volviendo al menú de Hackrow.")
                pont_espa()

            if modo_seguro and any(prohibido in comando for prohibido in comandos_prohibidos):
                print("Comando no permitido por razones de seguridad.")
                continue

            try:
                resultado = eval(comando)

                if resultado is not None:
                    print(resultado)

            except SyntaxError:
                try:
                    exec(comando)
                except Exception as e:
                    print(f"[Error exec] {e}")
                    
            except Exception as e:
                print(f"[Error eval] {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")
        