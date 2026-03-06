# Estructuras condicionales 1

# Escribe un programa que pida al usuario un número e indique si es positivo, negativo o cero.

n = float(input("ingrese un numero: "))

if(n > 0):
    print("el numero ingresado es positivo")
elif(n < 0):
    print("el numero ingresado es negativo")
else:
    print("el numero ingresado es neutro")
