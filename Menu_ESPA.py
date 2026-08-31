# menu espagnol

import sys
import time as t
import os
import platform
import sys
from Change_Lang_ESPA_PYTHON_BRIDE import pyESPA
from Change_Lang_ESPA_PYTHON import pyESPApy
from Change_Lang_ESPA_CROW import crow
from Change_Lang_ESPA_BATCH import BatchESPA
from mini_nmap import prompt_and_run

from PHost_ESPA import main

from PONT import pont_flower

from colorama import Fore, init

init()

versp = Fore.MAGENTA + "->" + Fore.RESET # <-- direction en violet

def MenuESP():
    try:
        while True:
            print("\n")
            print(r"─/[ HackRow ]\─")
            print("\n")
            print("Usa //ayuda para mostrar la lista de comandos disponibles.")

            print("\n")

            try:
                command = input("<Crow> : ").lower()
            
            except KeyboardInterrupt:
                print("Ctrl c Detectado")
                continue

            print()

            if command == "//py":
                pyESPA()
            
            elif command == "//py//":
                pyESPApy()

            elif command =="///crow":
                crow()
            
            elif command == "batch":
                BatchESPA()
            

            elif command == "//nmap":
                prompt_and_run(lang="es")
            
            elif command == "phost":
                os.system("cls")
                main()
            
            elif command == "clear":
                os.system('cls')
            
            elif command == "salida":
                pont_flower()

            elif command == "//flist":
                print("\n")
                print(os.listdir())


            if command == "//dcree":
                nueva_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
                
                try:
                    
                    os.mkdir(nueva_carpeta)
                    
                    if os.path.exists(nueva_carpeta):
                        print("La carpeta ha sido creada y verificada con éxito.")

                    else:
                        print("No se encontró la carpeta después de crearla.")

                except FileExistsError:
                    print("La carpeta ya existe.")


            elif command == "//dsd":

                carpeta_principal = input("Ingrese el nombre de la carpeta: ")

                subcarpeta = input("Ingrese el nombre de la subcarpeta: ")
    
                ruta_completa = os.path.join(carpeta_principal, subcarpeta)
                
                try:

                    os.makedirs(ruta_completa)
                    
                    if os.path.exists(carpeta_principal):

                        print("La carpeta principal ha sido creada y verificada con éxito.")

                    if os.path.exists(ruta_completa):
                        print("La subcarpeta ha sido creada y verificada con éxito.")

                except FileExistsError:
                    print("La carpeta o subcarpeta ya existe.")


            elif command == "//sf":

                file_to_delete = input("¿Qué archivo desea eliminar?: ")
                
                try:

                    os.remove(file_to_delete)
                    print("El archivo ha sido eliminado correctamente.")
                    
                except FileNotFoundError:
                    print("El archivo no existe.")
                
                except Exception as e:
                    print(f"Error al eliminar el archivo: {e}")


            elif command == "//sd":
                
                folder_to_delete = input("¿Qué carpeta desea eliminar?: ")
                
                try:

                    os.rmdir(folder_to_delete)
                    print("La carpeta ha sido eliminada correctamente.")
                
                except FileNotFoundError:
                    print("La carpeta no existe.")
                
                except OSError:
                    print("La carpeta no está vacía o no se puede eliminar.")
                
                except Exception as e:
                    print(f"Error al eliminar la carpeta: {e}")
                

            elif command == "//renome":
                
                old_name = input("¿Qué archivo o carpeta desea renombrar?: ")
                
                if not os.path.exists(old_name):
                    print("El archivo o carpeta especificado no existe.")
                    
                else:
                    new_name = input("Ingrese el nuevo nombre: ")
                    extension = input("¿Desea agregar una extensión? (ej: .txt, .py, dejar vacío si no): ").strip()
                    
                    if extension:

                        if not extension.startswith('.'):

                            extension = '.' + extension
                            
                            if not new_name.endswith(extension):

                                new_name += extension
                                
                                try:

                                    os.rename(old_name, new_name)
                                    print(f"Éxito: '{old_name}' ha sido renombrado a '{new_name}' correctamente.")
                                
                                except Exception as e:
                                    print(f"Ocurrió un error al renombrar: {e}")


            elif command == "//vfe":

                print("\n")

                archivo_a_verificar = input("¿Qué archivo desea verificar si existe?: ")
                
                try:

                    if os.path.exists(archivo_a_verificar):
                        print("Este archivo existe en su equipo.")
        
                    else:
                        print("El archivo no existe en su equipo.")
    
                except Exception as e:
                    print(f"Ocurrió un error: error -> {e}")
                    

            elif command == "//vuf":
                print("\n")
                nombre_del_archivo = input("Ingrese el nombre del archivo a verificar: ")
                
                if os.path.exists(nombre_del_archivo) and os.path.isfile(nombre_del_archivo):
                    nombre_sin_ext, extension = os.path.splitext(nombre_del_archivo)
                    print("Es un archivo válido.")
                    print(f"Nombre sin extensión: {nombre_sin_ext}")
                    print(f"Extensión detectada: {extension}")

                else:
                    print("No es un archivo válido o no existe.")
                    

            elif command == "//vud":
                print("\n")
                nombre_de_la_carpeta = input("Ingrese el nombre de la carpeta a verificar: ")
                
                if os.path.exists(nombre_de_la_carpeta) and os.path.isdir(nombre_de_la_carpeta):
                    print("Es una carpeta válida.")
                    print(f"Nombre de la carpeta: {os.path.basename(nombre_de_la_carpeta)}")
                    print(f"Ruta absoluta: {os.path.abspath(nombre_de_la_carpeta)}")

                else:
                    print("No es una carpeta válida o no existe.")
            

            elif command == "//rc":
                print(os.getcwd())
            

            elif command == "//cr":
                change_fichier = input("Ingrese una ruta de archivo : ")
                try:
                    os.chdir(change_fichier)

                except Exception as e:
                    print(f"Hubo un error ' error -> {e} '")

            
            elif command == "//ccv":
                folder_path = input("Introduzca la ruta de una carpeta: ")
                file_name = input("Introduzca un nombre de archivo, ej.: archivo.txt: ")
                
                full_path = os.path.join(folder_path, file_name)
                print(f"Ruta completa: {full_path}")


            elif command == "dca":
                
                print()

                try:
                    chemain_absolu = input("Introduzca un nombre de archivo : ")

                    print()

                    trouve = False
                    
                    for raiz, carpetas, archivos in os.walk("C:\\"):
                        
                        for archivo in archivos:
                            
                            if archivo.startswith(chemain_absolu):
                                print(f"Camino absoluto : {os.path.join(raiz, archivo)}")

                                trouve = True
                                pass
                        
                        for carpeta in carpetas:
                            if carpeta.startswith(chemain_absolu):
                                print(f"Camino absoluto : {os.path.join(raiz, carpeta)}")
                                
                                trouve = True

                                pass

                        if trouve:
                            pass

                    if not trouve:
                        print("Nombre de archivo o carpeta no encontrado.")

                except Exception as e:
                    print(f"Error al recuperar -> {e}")
            

            elif command == "//nfu":

                print()

                nombre_archivo_nfu = input("Introduzca una ruta de archivo : ")

                try:
                    if os.path.exists(nombre_archivo_nfu):
                        print(f"nom : {os.path.basename(nombre_archivo_nfu)}")
                    
                    else:
                        print("Ruta no encontrada. Por favor, verifique la ruta.")
                
                except Exception as e:
                    print(f"Erreur - > {e}")
                
                except KeyboardInterrupt:
                    continue


            elif command == "//ndp":

                try:
                    nombre_archivo_ndp = input("Entrada a una chamain : ")
                    
                    if os.path.exists(nombre_archivo_ndp):
                        print(f"nombre de los padres : {os.path.dirname(nombre_archivo_ndp)}")

                    else:
                        print("Nombre de archivo o carpeta no encontrado.")

                except Exception as e:
                    print(f"Error -> {e}")
                
                except KeyboardInterrupt as e:
                    print("Ctrl c Non actif.")
                    continue
            

            elif command == "//ns":
                
                print()

                print(f"Nombre del sistema : {os.name}")
            

            elif command == "//ave":

                print()

                paths = os.environ['PATH'].split(';')

                for p in paths:
                    print(p)
            

            elif command == "//rve":

                print()
                
                print(f"Nombre de usuario : {os.getenv('USERNAME')}")


            elif command == "//dve":
                ajout_path = input("Introduce un nombre : ").strip()

                print()

                try:
                    
                    sep = ';' if platform.system() == 'Windows' else ':'


                    print("-----PATH antes de la modificación-----")

                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):

                        print(f"{i:02}. {p}")
                        
                        if ajout_path and ajout_path not in os.environ['PATH'].split(sep):

                            nouveau_path = os.environ["PATH"] + sep + ajout_path
                            os.putenv("PATH", ajout_path)

                            os.environ["PATH"] = nouveau_path

                    print()
                    
                    print("-----PATH después de la modificación-----")
                    
                    print()

                    for i, p in enumerate(os.environ['PATH'].split(sep), 1):
                        print(f"{i:02}. {p}")

                except Exception as e:
                    print(f"Error -> {e}")
            

            elif command == "//ecs":

                commande = input("Bath >>> : ")

                print(f"{os.system(commande)}")
                
            
            elif command == "//ofpd":

                chemain_ofpd = input("Entró en un camino : ")

                if os.path.exists(chemain_ofpd):
                    os.startfile(chemain_ofpd)
                
                else:
                    print("Ruta no válida.")


            elif command == "//idpa":
                print(os.getpid())
            

            elif command == "//nuc":
                print(f"Usuario registrado : {os.getlogin()}")
            

            elif command == "//idpp":
                print(f"El ID del proceso principal es : {os.getppid()}")
            

            elif command =="//laps":
                argu = sys.argv
                print(f"Argumento encontrado : {argu}")
            

            elif command == "//nds":
                script_name = sys.argv[0]
                print(f"Nombre del guión : {script_name}")
            

            elif command == "//ss":

                command_ss = input("<<< : ")

                sys.stdout.write(command_ss)


            elif command  == "//vc":

                print()

                print(sys.version)
            

            elif command == "//vsft":

                print(sys.version_info)


            elif command == "//pf":

                print(sys.platform)


            elif command == "//cvi":

                print(sys.executable)


            elif command == "//lccm":

                print(sys.path)


            elif command == "//ayuda":
                print("\n")
                
                print()

                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Cambiar idioma", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//[ idioma ]  {versp} ", Fore.WHITE + "ej :", Fore.LIGHTGREEN_EX + " py, batch, PHost, ///crow ' Crow es el lenguaje personalizado de HackRow ' " + Fore.RESET)
                print("│")
                print("┌────────────────────/[ ", Fore.LIGHTCYAN_EX + "Terminal", Fore.WHITE + " ]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"clear  {versp} ", Fore.LIGHTGREEN_EX + "' Borrar pantalla '." + Fore.RESET)
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Rutas y directorios", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Flist  {versp} ", Fore.LIGHTGREEN_EX + "' Lista todos los archivos en una carpeta '." + Fore.RESET) # os.listdir('.')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Dcree -[nombre de carpeta]  {versp} ", Fore.LIGHTGREEN_EX + "' Crea una nueva carpeta '." + Fore.RESET) # os.mkdir("nouveau_dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DSD -[carpeta/subcarpeta/...]  {versp} ", Fore.LIGHTGREEN_EX + "' Crea una estructura de carpetas necesarias '." + Fore.RESET) # os.makedirs("a/b/c")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SF -[archivo.txt ]  {versp} ", Fore.LIGHTGREEN_EX + "' Elimina un archivo '." + Fore.RESET) # os.remove("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SD -[nombre de carpeta ]  {versp} ", Fore.LIGHTGREEN_EX + "' Suprime un dossier vide '." + Fore.RESET) # os.rmdir("dossier_vide")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//Renome -[nombre_antiguo.txt, nombre_nuevo.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Renombra o mueve un archivo '." + Fore.RESET) # os.rename("ancien.txt", "nouveau.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VFE -[archivo.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Verifica si un archivo existe. '." + Fore.RESET) # os.path.exist("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUF -[archivo.txt]  {versp} ", Fore.LIGHTGREEN_EX + "' Verifica si es un archivo. '." + Fore.RESET) # os.path.isfile("teste.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VUD -[carpeta]  {versp} ", Fore.LIGHTGREEN_EX + "' Verifica si es una carpeta. '." + Fore.RESET) # os.path.isdir("mon_dossier")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Rutas y directorios", Fore.WHITE + "]/─>"+ Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RC {versp} ", Fore.LIGHTGREEN_EX + "'  Muestra la carpeta de trabajo actual. '." + Fore.RESET) # os.getcwd() / print(os.getcwd())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CR -[carpeta] {versp} ", Fore.LIGHTGREEN_EX + "' Cambia de directorio '." + Fore.RESET) # os.chdir / os.chdir("dossier")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CCV -[carpeta] -[archivo] {versp} ", Fore.LIGHTGREEN_EX + "' Construye una ruta válida '." + Fore.RESET) # os.path.join() / os.path.join("mon_dossier", "fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DCA -[archivo] {versp} ", Fore.LIGHTGREEN_EX + "' Muestra la ruta absoluta '." + Fore.RESET) # os.path.abspath() / os.path.abspath("fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NFU -[ruta] -[archivo.txt] {versp} ", Fore.LIGHTGREEN_EX + "' Muestra solo el nombre del archivo '." + Fore.RESET) # os.path.basename() / os.path.basename("/chemain/fichier.txt")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDP -[ruta] -[archivo.txt] {versp} ", Fore.LIGHTGREEN_EX + "' Muestra el nombre de la carpeta principal '." + Fore.RESET) # os.path.dirname() / os.path.dirname("/chemain/fichier.txt")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Entorno del sistema", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NS ", Fore.LIGHTGREEN_EX + "' Muestra el nombre del sistema operativo '." + Fore.RESET) # os.name / print(os.name)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//AVE ", Fore.LIGHTGREEN_EX + "' Accede a las variables de entorno '." + Fore.RESET) # os.environ / os.environ['PATH']
                print("│ ", Fore.LIGHTYELLOW_EX + f"//RVE ", Fore.LIGHTGREEN_EX + "' Obtiene una variable de entorno específica '." + Fore.RESET) # os.getenv() / os.getenv('USERNAME')
                print("│ ", Fore.LIGHTYELLOW_EX + f"//DVE ", Fore.LIGHTGREEN_EX + "' Define una nueva variable de entorno '." + Fore.RESET) # os.putenv() / os.putenv('MON_VAR', '123')
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Ejecutar comandos del sistema", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//ECS {versp} ", Fore.LIGHTGREEN_EX + "' Ejecuta un comando en la terminal '." + Fore.RESET) # os.system() / os.system("echo hello")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//OFPD -[archivo] {versp} ", Fore.LIGHTGREEN_EX + "' Abre un archivo con el programa predeterminado '." + Fore.RESET) # os.startfile() / os.startfile("image.jpg")
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Procesos y usuarios", Fore.WHITE + "]/─>")
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPA {versp} ", Fore.LIGHTGREEN_EX + "' Muestra el ID del proceso actual '." + Fore.RESET) # os.getpid() / print(os.getpid())
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NUC {versp} ", Fore.LIGHTGREEN_EX + "' Muestra el nombre del usuario conectado '." + Fore.RESET) # os.getlogin() / os.getlogin()
                print("│ ", Fore.LIGHTYELLOW_EX + f"//IDPP {versp} ", Fore.LIGHTGREEN_EX + "' Muestra el ID del proceso padre '." + Fore.RESET) # os.getppid() / print(os.getppid())
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Argumentos de línea de comandos ( línea de código )", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LAPS {versp} ", Fore.LIGHTGREEN_EX + "' Lista los argumentos pasados al script '." + Fore.RESET) # sys.argv / print(sys.argv)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//NDS {versp} ", Fore.LIGHTGREEN_EX + "' Muestra el nombre del script ( argv[0]) '." + Fore.RESET) # sys.argv[0] / print(sys.argv[0])
                print("│")
                print("┌────────────────────/[", Fore.LIGHTCYAN_EX + "Información del sistema", Fore.WHITE + "]/─>" + Fore.RESET)
                print("│")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//SS {versp} ", Fore.LIGHTGREEN_EX + "' Escribe texto en la salida estándar (consola) '." + Fore.RESET) # ssys.stdout / sys.stdout.write("hello\n")
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VC {versp} ", Fore.LIGHTGREEN_EX + "' Muestra la versión completa '.") # sys.version / print(sys.version)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//VSFT {versp} ", Fore.LIGHTGREEN_EX + "' Muestra la versión como una tupla '." + Fore.RESET) # sys.version_info / print(sys.version_info)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//PF {versp} ", Fore.LIGHTGREEN_EX + "' Muestra la plataforma del sistema operativo '." + Fore.RESET) # sys.platform / print(sys.platform)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//CVI {versp} ", Fore.LIGHTGREEN_EX + "' Ruta del intérprete '." + Fore.RESET) # sys.executable / print(sys.executable)
                print("│ ", Fore.LIGHTYELLOW_EX + f"//LCCM {versp}", Fore.LIGHTGREEN_EX + "' Lista las rutas donde buscar los módulos '." + Fore.RESET) # sys.path / print(sys.path)
                print("│")
                print("└─────────────────────────────────────────────────────────────────────────────[", Fore.LIGHTGREEN_EX + "END", Fore.WHITE + "]" + Fore.RESET)


    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Se ha detectado la tecla Ctrl+." + Fore.RESET) 
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error -> {e}")
        