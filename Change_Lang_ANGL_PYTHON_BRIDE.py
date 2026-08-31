
def pyANGL():
    from PONT import pont_angl
    
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Python commands must be written in English.")
        print('Type `exit` to leave Python mode.')
        print('Use `print()`, `for`, `def`, etc.\n')

        # Secure mode is enabled
        safe_mode = True

        # Forbidden commands in secure mode
        forbidden_commands = [
            "import os", "import sys", "import subprocess", "import socket",
            "from socket", "__import__", "eval(", "exec(", "open(", "compile(",
            "globals(", "locals(", "input("
        ]

        while True:

            try:
                command = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c Detected.")
                continue
            
            if command.strip().lower() == "exit":
                print("Returning to Hackrow menu.")
                pont_angl()

            if safe_mode and any(blocked in command for blocked in forbidden_commands):
                print("Command not allowed for security reasons.")
                continue

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
        