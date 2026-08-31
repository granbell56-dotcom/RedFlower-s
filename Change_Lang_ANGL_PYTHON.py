
def pyANGLpy():
    from PONT import pont_angl
    
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Python commands must be written in English.")
        print('Type `exit` to leave Python mode.')
        print('Use `print()`, `for`, `def`, etc.\n')

        while True:

            try:
                command = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c Detected.")
                continue
            
            if command.strip().lower() == "exit":
                print("Returning to Hackrow menu.")
                pont_angl()

            try:
                result = eval(command)
                if result is not None:
                    print(result)

            except SyntaxError:
                try:
                    exec(command)

                except Exception as e:
                    print(f"[Exec Error] {e}")
                    
            except Exception as e:
                print(f"[Eval Error] {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        