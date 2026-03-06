# programa para lanzar dados de diferentes tipos

# el usuario selecciona una cantidad de dados y los lados que 
# tiene el dado a lanzar en formato de XdY

import random, os

def roll(X,Y):
    result = 0
    for i in range(X + 1):
        result = result + random.randrange(1,Y+1)
    return result

X = int(input("dados que desea lanzar: "))
Y = int(input("cantidad de lados del dado: "))
print(f"lanzando {X} dados de {Y} lados...")
result = roll(X,Y)

print(f"ha sacado {result}")



