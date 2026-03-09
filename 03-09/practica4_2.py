# leer por teclado 2 numeros e imprimir el mayor o si son iguales

n1 = int(input("ingrese el primer numero para comparar: "))
n2 = int(input("ingrese el segundo numero para comparar: "))

if(n1 > n2):
    print(f"el primer numero ({n1}) es el mayor")
elif(n1 == n2):
    print("ambos numeros son iguales")
else:
    print(f"el segundo numero ({n2}) es el mayor")