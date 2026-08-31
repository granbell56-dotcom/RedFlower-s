# changement de langue
# langue PYTHON

def pyFR():
    from PONT import pont_fr
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Les commandes en Python seront en anglais.")
        print('Tapez `exit` pour quitter le mode Python.')
        print('Utilisez `print()`, `for`, `def`, etc.\n')

        # Mode sécurisé actif
        safe_mode = True

        # Commandes interdites en mode sécurisé
        bloc_interdits = [
            "import os", "import sys", "import subprocess", "import socket",
            "from socket", "__import__", "eval(", "exec(", "open(", "compile(",
            "globals(", "locals(", "input("
        ]

        while True:

            try:
                commande = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c detecté.")
                continue
            
            if commande.strip().lower() == "exit":
                print("Retour au menu Hackrow.")
                pont_fr()
                

            if safe_mode and any(interdit in commande for interdit in bloc_interdits):
                print("Commande interdite pour des raisons de sécurité.")
                continue

            try:
                result = eval(commande)
                if result is not None:
                    print(result)
            except SyntaxError:
                try:
                    exec(commande)
                except Exception as e:
                    print(f"[Erreur exec] {e}")
            except Exception as e:
                print(f"[Erreur eval] {e}")

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        