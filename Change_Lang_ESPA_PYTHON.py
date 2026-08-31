
def pyESPApy():
    from PONT import pont_espa
    
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Los comandos de Python deben escribirse en inglés.")
        print('Escribe `exit` para salir del modo Python.')
        print('Usa `print()`, `for`, `def`, etc.\n')

        while True:

            try:
                comando = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c Detectado.")
                continue

            if comando.strip().lower() == "exit":
                print("Volviendo al menú de Hackrow.")
                pont_espa()

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
        