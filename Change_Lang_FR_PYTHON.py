# changement de langue
# langue PYTHON

def pyFRpy():
    from PONT import pont_fr
    
    try:
        print("\n")
        print("/-- HackRow --/")
        print("\n")
        print("Les commandes en Python seront en anglais.")
        print('Tapez `exit` pour quitter le mode Python.')
        print('Utilisez `print()`, `for`, `def`, etc.\n')

        while True:

            try:
                commande = input("<PY> : ")
            
            except KeyboardInterrupt:
                print("Ctrl c detecté.")
                continue
            
            if commande.strip().lower() == "exit":
                print("Retour au menu Hackrow.")
                pont_fr()

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
        