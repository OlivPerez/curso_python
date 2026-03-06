# programa simple para lanzar dados

import os, time, random, sys

def roll():
    return random.randrange(1,7)

while True:
    print("elige un numero del 1 al 6, escribe cualquier otro caracter para salir")
    option = int(input("numero: "))
    if option >= 1 and option <= 6:
        os.system("cls")
        print(f"seleccionaste el {option}")
        print("lanzando dado", end="", flush = True) # fuerza a que se muestre inmediatamente
        for i in range(3): 
            time.sleep(0.3)
            print(".", end="") 
            sys.stdout.flush()

        dice = roll()
        print(end= "\n")
        time.sleep(0.3)
        print(f"el dado ha caido en {dice}")

        if dice == option:
            print("has acertado, felicidades! jugar otra vez?")
        else:
            print("mejor suerte para la proxima, volver a intentarlo?")
    else:
        print("juego terminado")
        break