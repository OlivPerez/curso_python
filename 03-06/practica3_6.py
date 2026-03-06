# Estructuras de repetición 2

# Crea un programa que solicite al usuario un número entero positivo y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for

n = int(input("ingrese un numero entero positivo: "))

for i in range(10):
    print(f"{n} x {i + 1} = {n * (i + 1)}")

