# menu francais

import sys
import time as t
import os
import platform
import sys
from Change_Lang_FR_PYTHON_BRIDE import pyFR
from Change_Lang_FR_PYTHON import pyFRpy
from Change_Lang_FR_CROW import crow
from Change_Lang_FR_BATCH import BatchFR
from mini_nmap import prompt_and_run

from PHost_FR import main

from PONT import pont_flower

from colorama import Fore, init

init()

versp = Fore.MAGENTA + "->" + Fore.RESET # <-- direction en violet

def MenuFR():
    try:
        while True:
            print("\n")
            print(r"─/[ HackRow ]\─")
            print("\n")
            print("Utilisé //aide pour afficher la liste des commande disponible.")

            print("\n")

            try:
                command = input("<Crow> : ").lower()
            
            except KeyboardInterrupt:
                print("Ctrl c Detecté.")
                continue

            print()
                
            if  command == "//py":
                pyFR()
            
            elif command == "//py//":
                pyFRpy()
                
            elif command == "///crow":
                crow()
            
            elif command == "//batch":
                BatchFR()

            elif command == "phost":
                os.system("cls")
                main()

            elif command == "clear":
                os.system('cls')

            elif command == "sortie":
                pont_flower()

            elif command == "//nmap":
                prompt_and_run(lang="fr")

            elif command == "//flist":
                print("\n")
                print(os.listdir())
            
            if command == "//dcree":
                nouveau_dossier = input("Entrée le nom du nouveau dossier : ")
                
                try:
                    os.mkdir(nouveau_dossier)

                    if os.path.exists(nouveau_dossier):  
                        print("Le dossier a été créé et vérifié avec succès.")

                    else:
                      print("Le dossier n'a pas été trouvé après création.")

                except FileExistsError:
                    print("Le dossier existe déjà.")

            
            elif command == "//dsd":
                dossier_a_cree = input("Entrée le nom du dossier : ")
                sous_dossier = input("Entrée le nom du sous-dossier : ")
                
                chemin_complet = os.path.join(dossier_a_cree, sous_dossier)
                
                try:
                    os.makedirs(chemin_complet)
                    
                    if os.path.exists(dossier_a_cree):
                     print("Le dossier principal a été créé et vérifié avec succès.")
        
                    if os.path.exists(chemin_complet):
                      print("Le sous-dossier a été créé et vérifié avec succès.")

                except FileExistsError:
                 print("Le dossier ou le sous-dossier existe déjà.")


            elif command == "//sf":
                fichier_a_supprimer = input("Quel fichier voulez-vous supprimer ? : ")
                
                try:

                    os.remove(fichier_a_supprimer)
                    print("Le fichier a été supprimé avec succès.")
                
                except FileNotFoundError:
                    print("Le fichier n'existe pas.")
                    
                except Exception as e:
                    print(f"Erreur lors de la suppression du fichier : {e}")
            

            elif command == "//sd":
                dossier_a_supprimer = input("Quel dossier voulez-vous supprimer ? : ")
                
                try:
                    
                    os.rmdir(dossier_a_supprimer)
                    print("Le dossier a été supprimé avec succès.")
                    
                except FileNotFoundError:
                    print("Le dossier n'existe pas.")
                    
                except OSError:
                    print("Le dossier n'est pas vide ou ne peut pas être supprimé.")
                    
                except Exception as e:
                    print(f"Erreur lors de la suppression du dossier : {e}")


            elif command == "//renome":
                
                ancien_nom = input("Quel fichier ou dossier voulez-vous renommer ? : ")
                
                if not os.path.exists(ancien_nom):
                    print("Le fichier ou dossier spécifié n'existe pas.")
                    
                else:
                    nouveau_nom = input("Entrez le nouveau nom : ")
                    extension = input("Voulez-vous ajouter une extension ? (ex : .txt, .py, laisser vide sinon) : ").strip()
                    
                    if extension:
                        
                        if not extension.startswith('.'):
                            extension = '.' + extension
                            
                            if not nouveau_nom.endswith(extension):
                                nouveau_nom += extension
                                
                                try:

                                    os.rename(ancien_nom, nouveau_nom)
                                    print(f"Succès : '{ancien_nom}' a été renommé en '{nouveau_nom}' avec succès.")
                                
                                except Exception as e:
                                    print(f"Erreur lors du renommage : {e}")


            elif command == "//vef":
                print("\n")
                fichier_a_verifier = input("Quel fichier voulez-vous verifier sont existance ? : ")

                try:
                    if os.path.exists(fichier_a_verifier):
                        print("Ce fichier existe sur vôtre machine.")
                    
                    else:
                        print("Vôtre fichier existe pas sur vôtre machine.")
                
                except Exception as e:
                    print(f"Il y a eu une erreur ' erreur -> {e} '")


            elif command == "//vuf":
                print("\n")
                nom_du_fichier = input("Entrez le nom du fichier à vérifier : ")
                
                if os.path.exists(nom_du_fichier) and os.path.isfile(nom_du_fichier):
                    nom_sans_extension, extension = os.path.splitext(nom_du_fichier)
                    print(f"C'est bien un fichier.")
                    print(f"Nom sans extension : {nom_sans_extension}")
                    print(f"Extension détectée : {extension}")
                
                else:
                 print("Ce n'est pas un fichier valide ou il n'existe pas.")
            

            elif command == "//vud":
                print("\n")
                nom_du_dossier = input("Entrez le nom du dossier à vérifier : ")
                
                if os.path.exists(nom_du_dossier) and os.path.isdir(nom_du_dossier):
                    print(f"C'est bien un dossier.")
                    print(f"Nom du dossier : {os.path.basename(nom_du_dossier)}")
                    print(f"Chemin absolu : {os.path.abspath(nom_du_dossier)}")

                else:
                   print("Ce n'est pas un dossier valide ou il n'existe pas.")


            elif command == "//rc":
                print(os.getcwd())
            

            elif command == "//cr":
                change_fichier = input("Entrée un chamin de fichier : ")
                try:
                    os.chdir(change_fichier)

                except Exception as e:
                    print(f"Il y a eu une erreur ' erreur -> {e} '")


            elif command == "//ccv":

                dossier = input("Entrez le chemin d'un dossier : ")
                fichier = input("Entrez un nom de fichier, ex : fichier.txt : ")
                
                chemin_complet = os.path.join(dossier, fichier)
                print(f"Chemin complet : {chemin_complet}")
                    

            elif command == "//dca":
                
                print()

                try:
                    chemain_absolu = input("Entrée le nom d'un fichier : ")

                    print()

                    trouve = False
                    
                    for racine, dossiers, fichiers in os.walk("C:\\"):
                        
                        for fichier in fichiers:
                            if fichier.startswith(chemain_absolu):
                                print(f"Chemain absolu : {os.path.join(racine, fichier)}")

                                trouve = True
                                pass
                        
                        for dossier in dossiers:
                            if dossier.startswith(chemain_absolu):
                                print(f"Chemain absolu : {os.path.join(racine, dossier)}")
                                
                                trouve = True

                                pass

                        if trouve:
                            pass

                    if not trouve:
                        print("Nom de fichier ou dossier introuvable.")

                except Exception as e:
                    print(f"Erreur lors de la récuperation -> {e}")


            elif command == "//nfu":

                print()

                nom_fichier_nfu = input("Entrée un chemain de fichier : ")

                try:
                    if os.path.exists(nom_fichier_nfu):
                        print(f"nom : {os.path.basename(nom_fichier_nfu)}")
                    
                    else:
                        print("Chemain introuvable. Vérifier le chemain.")
                
                except Exception as e:
                    print(f"Erreur - > {e}")
                
                except KeyboardInterrupt:
                    continue
            

            elif command == "//ndp":

                try:
                    nom_fichier_ndp = input("Entrée un chamain : ")
                    
                    if os.path.exists(nom_fichier_ndp):
                        print(f"Nom du parent : {os.path.dirname(nom_fichier_ndp)}")

                    else:
                        print("Chemain introuvable. Vérifier le chemain.")

                except Exception as e:
                    print(f"Erreur -> {e}")
                
                except KeyboardInterrupt as e:
                    print("Ctrl c Non actif.")
                    continue
                

            elif command == "//ns":

                print()

                print(f"Nom du systène : {os.name}")
            

            elif command == "//ave":

                print()

                paths = os.environ['PATH'].split(';')

                for p in paths:
                    print(p)
            

            elif command == "//rve":

                print()

                print(f"Nom d'utilisateur : {os.getenv('USERNAME')}")
            

            elif command == "//dve":

                ajout_path = input("Entrée un nom : ").strip()

                print()

                try:
                    
                    sep = ';' if platform.system() == 'Windows' else ':'


                    print("-----PATH avant modification-----")

                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):

                        print(f"{i:02}. {p}")
                        
                        if ajout_path and ajout_path not in os.environ['PATH'].split(sep):

                            nouveau_path = os.environ["PATH"] + sep + ajout_path
                            os.putenv("PATH", ajout_path)

                            os.environ["PATH"] = nouveau_path

                    print()

                    print("-----PATH aprês modofication-----")
                    
                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):
                        print(f"{i:02}. {p}")

                except Exception as e:
                    print(f"Erreur -> {e}")
                

            elif command == "//Ecs":

                commande = input("Bath >>> : ")

                print(f"{os.system(commande)}")
            

            elif command == "//ofpd":

                chemain_ofpd = input("Entée un chemain : ")

                if os.path.exists(chemain_ofpd):
                    os.startfile(chemain_ofpd)
                
                else:
                    print("Chemain invalide.")

            
            elif command == "//idpa":
                print(os.getpid())


            elif command == "//nuc":
                print(f"Utilisateur connecté : {os.getlogin()}")
            

            elif command == "//idpp":
                print(f"L'ID du processus parent est : {os.getppid()}")


            elif command =="//laps":
                argu = sys.argv
                print(f"Argument trouvé : {argu}")
            

            elif command == "//nds":
                script_name = sys.argv[0]
                print(f"Nom du script : {script_name}")


            elif command == "//ss":

                command_ss = input("<<< : ")

                sys.stdout.write(command_ss)


            elif command  == "//vc":

                print()

                print(sys.version)
            
            elif command == "vsft":

                print(sys.version_info)


            elif command == "//pf":

                print(sys.platform)
            

            elif command == "//cvi":

                print(sys.executable)

            
            elif command == "//lccm":

                print(sys.path)
                
                
            elif command == "//aide":
                print()

                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Changer de langue", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//[ langue ]  {versp} ", Fore.WHITE + "ex :", Fore.LIGHTGREEN_EX + " py, batch, PHost, ///crow ' crow langage de HackRow ' " + Fore.RESET)
                print("│")
                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Terminal", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"clear  {versp} ", Fore.LIGHTGREEN_EX + "' Effacer l'écran '." + Fore.RESET)
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Systeme de fichier", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Flist  {versp} ", Fore.LIGHTGREEN_EX + "' Liste les fichiers d'un dossier '." + Fore.RESET) # os.listdir('.')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Dcree -[nom du dossier]  {versp} ", Fore.LIGHTGREEN_EX + "' Cree un dossier '." + Fore.RESET) # os.mkdir("nouveau_dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DSD -[nom des sous-dossier]  {versp} ", Fore.LIGHTGREEN_EX + "' Cree un dossier avec tout les sous-dossier necessaire '." + Fore.RESET) # os.makedirs("a/b/c")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SF -[Fichier a suprimer.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Suprime un fichier '." + Fore.RESET) # os.remove("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SD -[Nom du dossier vide]  {versp} ", Fore.LIGHTGREEN_EX + "' Suprime un dossier vide '." + Fore.RESET) # os.rmdir("dossier_vide")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Renome -[ancien nom.txt, nouveau.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' renomme ou deplace un fichier'." + Fore.RESET) # os.rename("ancien.txt", "nouveau.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VFE -[Nom du fichier.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' verifie si le fichier existe '." + Fore.RESET) # os.path.exist("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUF -[fichier.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' verifie si c'est un fichier '." + Fore.RESET) # os.path.isfile("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUD -[dossier]  {versp} ", Fore.LIGHTGREEN_EX + "' virifie si c'est un dossier '." + Fore.RESET) # os.path.isdir("mon_dossier")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Chemins et repertoires", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RC {versp} ", Fore.LIGHTGREEN_EX + "' Chemain actuel, repertoire courant '." + Fore.RESET) # os.getcwd() / print(os.getcwd())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CR -[dossier] {versp} ", Fore.LIGHTGREEN_EX + "' change de repertoire'." + Fore.RESET) # os.chdir / os.chdir("dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CCV -[nom du dossier] -[nom du fichier] {versp} ", Fore.LIGHTGREEN_EX + "' construit un chemin valide '." + Fore.RESET) # os.path.join() / os.path.join("mon_dossier", "fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DCA -[fichier] {versp} ", Fore.LIGHTGREEN_EX + "' donne le chemin absolu '." + Fore.RESET) # os.path.abspath() / os.path.abspath("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NFU -[chemin] -[fichier.txt] {versp} ", Fore.LIGHTGREEN_EX + "' nom du fichier uniquement '." + Fore.RESET) # os.path.basename() / os.path.basename("/chemain/fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDP -[chemain] -[fichier.txt] {versp} ", Fore.LIGHTGREEN_EX + "' nom du dossier parent '." + Fore.RESET) # os.path.dirname() / os.path.dirname("/chemain/fichier.txt")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Environement systeme", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NS ", Fore.LIGHTGREEN_EX + "' nom du système '." + Fore.RESET) # os.name / print(os.name)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//AVE ", Fore.LIGHTGREEN_EX + "' acces aux viariables d'environement '." + Fore.RESET) # os.environ / os.environ['PATH']
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RVE ", Fore.LIGHTGREEN_EX + "' recupere une varible d'environement '." + Fore.RESET) # os.getenv() / os.getenv('USERNAME')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DVE ", Fore.LIGHTGREEN_EX + "' definit une variable d'environement '." + Fore.RESET) # os.putenv() / os.putenv('MON_VAR', '123')
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Executer des commande systeme", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//ECS {versp} ", Fore.LIGHTGREEN_EX + "' Execute une commande shell '." + Fore.RESET) # os.system() / os.system("echo hello")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//OFPD -[fichier] {versp} ", Fore.LIGHTGREEN_EX + "' ouvre un fichier avec le programe par defeaut '." + Fore.RESET) # os.startfile() / os.startfile("image.jpg")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Processus et Utilisateurs", Fore.WHITE + "]/─>")
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPA {versp} ", Fore.LIGHTGREEN_EX + "' donne l'id du processus actuel '." + Fore.RESET) # os.getpid() / print(os.getpid())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NUC {versp} ", Fore.LIGHTGREEN_EX + "' nom de l'utilisateur connecté '." + Fore.RESET) # os.getlogin() / os.getlogin()
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPP {versp} ", Fore.LIGHTGREEN_EX + "' id du processus parent '." + Fore.RESET) # os.getppid() / print(os.getppid())
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Gestion des arguments ( ligne de code )", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LAPS {versp} ", Fore.LIGHTGREEN_EX + "' liste des argument passés au script '." + Fore.RESET) # sys.argv / print(sys.argv)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDS {versp} ", Fore.LIGHTGREEN_EX + "' nom du script ( argv[0]) '." + Fore.RESET) # sys.argv[0] / print(sys.argv[0])
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Information", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SS {versp} ", Fore.LIGHTGREEN_EX + "' sortie standard ( console ) '." + Fore.RESET) # ssys.stdout / sys.stdout.write("hello\n")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VC {versp} ", Fore.LIGHTGREEN_EX + "' version complete '.") # sys.version / print(sys.version)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VSFT {versp} ", Fore.LIGHTGREEN_EX + "' version complete sous forme de tuple '." + Fore.RESET) # sys.version_info / print(sys.version_info)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//PF {versp} ", Fore.LIGHTGREEN_EX + "' platforme systeme '." + Fore.RESET) # sys.platform / print(sys.platform)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CVI {versp} ", Fore.LIGHTGREEN_EX + "' chemain vers l'interpreteur '." + Fore.RESET) # sys.executable / print(sys.executable)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LCCM {versp}", Fore.LIGHTGREEN_EX + "' liste des chemain pour les modules '." + Fore.RESET) # sys.path / print(sys.path)
                print("│")
                print("└─────────────────────────────────────────────────────────────────────────────[", Fore.LIGHTGREEN_EX + "END", Fore.WHITE + "]" + Fore.RESET)
    
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + détécté." + Fore.RESET) 

    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Erreur -> {e}" + Fore.RESET)
        