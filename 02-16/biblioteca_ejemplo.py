# panel windows

import os   # importar libreria del sistema operativo
import time # importar libreria de tiempo

def wait(text): # funcion que falsea una pantalla de carga simple
    for x in range(6):
        os.system("cls") # ejecutar el comando "cls" para limpiar la pantalla
        print(f"cargando {text} {x * 20}%...")
        time.sleep(0.2) # esperar 0,3 segundos

true = True
while true == True:
    os.system("cls")
    print("seleccione una opcion del menu")
    option = input("1. calc\n2. paint\n3. apagar\n4. NO APAGAR\n5. salir\n")
    if option == "1":
        wait("calculadora")
        os.system("calc")
    elif option == "2":
        wait("paint")
        os.system("mspaint")
    elif option == "3":
        wait("apagando en 5 minutos")
        os.system("shutdown -s -t 300")
    elif option == "4":
        wait("cancelar apagado")
        os.system("shutdown -a")
    elif option == "5":
        print("saliendo del programa")
        break
    else:
        print("no entiendo esa orden")