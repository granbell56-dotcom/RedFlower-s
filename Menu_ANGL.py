# menu anglais

import sys
import time as t
import os
import platform
import sys
from Change_Lang_ANGL_PYTHON_BRIDE import pyANGL
from Change_Lang_ANGL_PYTHON import pyANGLpy
from Change_Lang_ANGL_CROW import crow
from Change_Lang_ANGL_BATCH import BatchANGL
from mini_nmap import prompt_and_run

from PHost_ANGL import main

from PONT import pont_flower

from colorama import Fore, init

init()

versp = Fore.MAGENTA + "->" + Fore.RESET # <-- direction en violet

def MenuANG():
    try:
        while True:
            print("\n")
            print(r"─/[ HackRow ]\─")
            print("\n")
            print("Use //help to display the list of available commands.")

            print("\n")

            try:
                command = input("<Crow> :  ").lower()
            
            except KeyboardInterrupt:
                print("Ctrl c Detected.")
                continue

            print()

            if command == "//py":
                pyANGL()
            
            elif command == "//py//":
                pyANGLpy()

            elif command == "///crow":
                crow()

            elif command == "batch":
                BatchANGL()
            
            elif command == "//nmap":
                prompt_and_run(lang="en")
            
            elif command == "phost":
                os.system("cls")
                main()

            elif command == "clear":
                os.system('cls')
            
            elif command == "exit":
                pont_flower()

            elif command == "//flist":
                print("\n")
                print(os.listdir())


            if command == "//dcree":
                new_folder = input("Enter the name of the new folder: ")

                try:
                    os.mkdir(new_folder)
                
                    if os.path.exists(new_folder):
                        print("The folder was successfully created and verified.")

                    else:
                        print("The folder was not found after creation.")

                except FileExistsError:
                    print("The folder already exists.")


            elif command == "//dsd":

                main_folder = input("Enter the name of the folder: ")
                sub_folder = input("Enter the name of the subfolder: ")
    
                full_path = os.path.join(main_folder, sub_folder)
                
                try:
                    os.makedirs(full_path)

                    if os.path.exists(main_folder):

                        print("The main folder was successfully created and verified.")

                    if os.path.exists(full_path):

                        print("The subfolder was successfully created and verified.")

                except FileExistsError:
                    print("The folder or subfolder already exists.")


            elif command == "//sf":
                file_to_delete = input("Which file do you want to delete?: ")
                
                try:

                    os.remove(file_to_delete)
                    print("The file was successfully deleted.")
                
                except FileNotFoundError:
                    print("The file does not exist.")
                    
                except Exception as e:
                    print(f"Error while deleting the file: {e}")
            

            elif command == "//sd":
                folder_to_delete = input("Which folder do you want to delete?: ")
                
                try:

                    os.rmdir(folder_to_delete)
                    print("The folder was successfully deleted.")
                
                except FileNotFoundError:
                    print("The folder does not exist.")
                    
                except OSError:
                    print("The folder is not empty or cannot be deleted.")
                    
                except Exception as e:
                    print(f"Error while deleting the folder: {e}")


            elif command == "//renome":
                
                old_name = input("Which file or folder do you want to rename?: ")
                
                if not os.path.exists(old_name):

                    print("The specified file or folder does not exist.")
                
                else:
                    new_name = input("Enter the new name: ")
                    extension = input("Do you want to add an extension? (e.g.: .txt, .py, leave empty otherwise): ").strip()
                    
                    if extension:

                        if not extension.startswith('.'):

                            extension = '.' + extension
                            
                            if not new_name.endswith(extension):

                                new_name += extension
                                
                                try:

                                    os.rename(old_name, new_name)
                                    print(f"Success: '{old_name}' has been renamed to '{new_name}' successfully.")
                                
                                except Exception as e:
                                    print(f"An error occurred during renaming: {e}")


            elif command == "//vfe":
                print("\n")
                file_to_check = input("Which file do you want to check for existence?: ")
                
                try:
                    if os.path.exists(file_to_check):
                        print("This file exists on your machine.")
        
                    else:
                        print("Your file does not exist on your machine.")
                        
                except Exception as e:
                    print(f"An error occurred: error -> {e}")


            elif command == "//vuf":
                print("\n")
                file_name = input("Enter the name of the file to check: ")
                
                if os.path.exists(file_name) and os.path.isfile(file_name):
                    
                    name_without_ext, extension = os.path.splitext(file_name)

                    print("It is a valid file.")
                    print(f"Name without extension: {name_without_ext}")
                    print(f"Detected extension: {extension}")
    
                else:
                    print("This is not a valid file or it does not exist.")


            elif command == "//vud":

                print("\n")

                folder_name = input("Enter the name of the folder to check: ")
    
                if os.path.exists(folder_name) and os.path.isdir(folder_name):

                    print("It is a valid folder.")
                    print(f"Folder name: {os.path.basename(folder_name)}")
                    print(f"Absolute path: {os.path.abspath(folder_name)}")

                else:
                 print("This is not a valid folder or it does not exist.")
            

            elif command == "//rc":
                print(os.getcwd())
            

            elif command == "//cr":
                change_fichier = input("Enter a file path : ")
                try:
                    os.chdir(change_fichier)

                except Exception as e:
                    print(f"There was a mistake ' error -> {e} '")
                

            elif command == "//ccv":

                folder_path = input("Enter a folder path: ")
                file_name = input("Enter a file name, e.g.: file.txt: ")

                full_path = os.path.join(folder_path, file_name)
                print(f"Full path: {full_path}")
            

            elif command == "dca":
                
                print()

                try:
                    chemain_absolu = input("Enter the name of a file : ")

                    print()

                    trouve = False
                    
                    for root, folders, files in os.walk("C:\\"):
                        
                        for file in files:
                            if file.startswith(chemain_absolu):
                                print(f"Absolute path : {os.path.join(root, file)}")

                                trouve = True
                                pass
                        
                        for folder in folders:
                            if folder.startswith(chemain_absolu):
                                print(f"Absolute path : {os.path.join(root, folder)}")
                                
                                trouve = True

                                pass

                        if trouve:
                            pass

                    if not trouve:
                        print("File or folder name not found.")
                
                except Exception as e:
                    print(f"Error while retrieving -> {e}")
            

            elif command == "//nfu":
                
                print()

                name_file_nfu = input("Enter a file path : ")

                try:
                    if os.path.exists(name_file_nfu):
                        print(f"nom : {os.path.basename(name_file_nfu)}")
                    
                    else:
                        print("Path not found. Check the path.")
                
                except Exception as e:
                    print(f"Error - > {e}")
                
                except KeyboardInterrupt:
                    continue


            elif command == "//ndp":

                try:
                    name_file_ndp = input("Entrer a chamain : ")
                    
                    if os.path.exists(name_file_ndp):
                        print(f"Parent's name : {os.path.dirname(name_file_ndp)}")

                    else:
                        print("Path not found. Check the path.")

                except Exception as e:
                    print(f"Error -> {e}")
                
                except KeyboardInterrupt as e:
                    print("Ctrl c Not active.")
                    continue
            

            elif command == "//ns":

                print()

                print(f"System name : {os.name}")
            

            elif command == "//ave":

                print()

                paths = os.environ['PATH'].split(';')

                for p in paths:
                    print(p)
            

            elif command == "//rve":

                print()
                
                print(f"User name : {os.getenv('USERNAME')}")
            

            elif command == "//dve":

                ajout_path = input("Enter a name : ").strip()

                print()

                try:
                    
                    sep = ';' if platform.system() == 'Windows' else ':'


                    print("-----PATH before modification-----")

                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):

                        print(f"{i:02}. {p}")
                        
                        if ajout_path and ajout_path not in os.environ['PATH'].split(sep):

                            nouveau_path = os.environ["PATH"] + sep + ajout_path
                            os.putenv("PATH", ajout_path)

                            os.environ["PATH"] = nouveau_path

                    print()
                    
                    print("-----PATH after modification-----")
                    
                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):
                        print(f"{i:02}. {p}")

                except Exception as e:
                    print(f"Error -> {e}")


            elif command == "//ecs":

                commande = input("Bath >>> : ")

                print(f"{os.system(commande)}")

            
            elif command == "//ofpd":

                chemain_ofpd = input("Entered a path : ")

                if os.path.exists(chemain_ofpd):
                    os.startfile(chemain_ofpd)
                
                else:
                    print("Invalid path.")


            elif command == "//idpa":
                print(os.getpid())
            

            elif command == "//nuc":
                print(f"User logged in : {os.getlogin()}")


            elif command == "//idpp":
                print(f"The parent process ID is : {os.getppid()}")


            elif command =="//laps":
                argu = sys.argv
                print(f"Argument found : {argu}")
            

            elif command == "//nds":
                script_name = sys.argv[0]
                print(f"Script name : {script_name}")


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


            elif command == "//help":
                
                print()

                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Change Language", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//[ language ]  {versp} ", Fore.WHITE + "ex :", Fore.LIGHTGREEN_EX + " py, batch, PHost, ///crow ' Crow is HackRow's custom language ' " + Fore.RESET)
                print("│")
                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Terminal", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"clear  {versp} ", Fore.LIGHTGREEN_EX + "' Clear screen '." + Fore.RESET)
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "File System", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Flist  {versp} ", Fore.LIGHTGREEN_EX + "' List all files in a folder '." + Fore.RESET) # os.listdir('.')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Dcree -[folder name]  {versp} ", Fore.LIGHTGREEN_EX + "' create a new folder '." + Fore.RESET) # os.mkdir("nouveau_dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DSD -[folder/subfolder/...]  {versp} ", Fore.LIGHTGREEN_EX + "' Create folders and necessary subfolders '." + Fore.RESET) # os.makedirs("a/b/c")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SF -[filename.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Delete a file '." + Fore.RESET) # os.remove("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SD -[folder name]  {versp} ", Fore.LIGHTGREEN_EX + "' Delete an empty folder '." + Fore.RESET) # os.rmdir("dossier_vide")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Renome -[old_name.txt, new_name.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' renomme ou deplace un fichier'." + Fore.RESET) # os.rename("ancien.txt", "nouveau.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VFE -[filename.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Check if a file exists '." + Fore.RESET) # os.path.exist("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUF -[filename.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Check if the path is a file '." + Fore.RESET) # os.path.isfile("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUD -[folder name]  {versp} ", Fore.LIGHTGREEN_EX + "' Check if the path is a directory '." + Fore.RESET) # os.path.isdir("mon_dossier")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Paths & Directories", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RC {versp} ", Fore.LIGHTGREEN_EX + "' Show the current working directory '." + Fore.RESET) # os.getcwd() / print(os.getcwd())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CR -[folder name] {versp} ", Fore.LIGHTGREEN_EX + "' Change the current directory '." + Fore.RESET) # os.chdir / os.chdir("dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CCV -[folder] -[file] {versp} ", Fore.LIGHTGREEN_EX + "' Create a valid path '." + Fore.RESET) # os.path.join() / os.path.join("mon_dossier", "fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DCA -[filename] {versp} ", Fore.LIGHTGREEN_EX + "' Get the absolute path '." + Fore.RESET) # os.path.abspath() / os.path.abspath("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NFU -[path] -[file.txt] {versp} ", Fore.LIGHTGREEN_EX + "' Get file name only '." + Fore.RESET) # os.path.basename() / os.path.basename("/chemain/fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDP -[path] -[file.txt] {versp} ", Fore.LIGHTGREEN_EX + "' Get parent folder name '." + Fore.RESET) # os.path.dirname() / os.path.dirname("/chemain/fichier.txt")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "System Environment", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NS ", Fore.LIGHTGREEN_EX + "' Get the name of the operating system '." + Fore.RESET) # os.name / print(os.name)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//AVE ", Fore.LIGHTGREEN_EX + "' Access all environment variables '." + Fore.RESET) # os.environ / os.environ['PATH']
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RVE ", Fore.LIGHTGREEN_EX + "' Retrieve a specific environment variable '." + Fore.RESET) # os.getenv() / os.getenv('USERNAME')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DVE ", Fore.LIGHTGREEN_EX + "' Set a new environment variable '." + Fore.RESET) # os.putenv() / os.putenv('MON_VAR', '123')
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Execute System Commands", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//ECS {versp} ", Fore.LIGHTGREEN_EX + "' Execute a shell command '." + Fore.RESET) # os.system() / os.system("echo hello")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//OFPD -[file] {versp} ", Fore.LIGHTGREEN_EX + "' Open a file using the default program '." + Fore.RESET) # os.startfile() / os.startfile("image.jpg")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Processes & Users", Fore.WHITE + "]/─>")
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPA {versp} ", Fore.LIGHTGREEN_EX + "' Get the current process ID '." + Fore.RESET) # os.getpid() / print(os.getpid())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NUC {versp} ", Fore.LIGHTGREEN_EX + "' Get the name of the currently logged-in user '." + Fore.RESET) # os.getlogin() / os.getlogin()
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPP {versp} ", Fore.LIGHTGREEN_EX + "' Get the parent process ID '." + Fore.RESET) # os.getppid() / print(os.getppid())
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Command-line Arguments ( line of code )", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LAPS {versp} ", Fore.LIGHTGREEN_EX + "' List all arguments passed to the script '." + Fore.RESET) # sys.argv / print(sys.argv)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDS {versp} ", Fore.LIGHTGREEN_EX + "' Get the script name ( argv[0]) '." + Fore.RESET) # sys.argv[0] / print(sys.argv[0])
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "System Information", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SS {versp} ", Fore.LIGHTGREEN_EX + "' Output text to the standard console '." + Fore.RESET) # ssys.stdout / sys.stdout.write("hello\n")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VC {versp} ", Fore.LIGHTGREEN_EX + "' Get the full version '.") # sys.version / print(sys.version)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VSFT {versp} ", Fore.LIGHTGREEN_EX + "' Get the version as a tuple '." + Fore.RESET) # sys.version_info / print(sys.version_info)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//PF {versp} ", Fore.LIGHTGREEN_EX + "' Get the operating system platform '." + Fore.RESET) # sys.platform / print(sys.platform)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CVI {versp} ", Fore.LIGHTGREEN_EX + "' Path to the Python interpreter '." + Fore.RESET) # sys.executable / print(sys.executable)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LCCM {versp}", Fore.LIGHTGREEN_EX + "' List all module search paths '." + Fore.RESET) # sys.path / print(sys.path)
                print("│")
                print("└─────────────────────────────────────────────────────────────────────────────[", Fore.LIGHTGREEN_EX + "END", Fore.WHITE + "]" + Fore.RESET)
        
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Ctrl + detected." + Fore.RESET) 
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error -> {e}" + Fore.RESET)
        