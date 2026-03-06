"""
Crear una función que reciba una lista y otro argumento ASC o DESC, y ordene la lista de forma
ascendente o descendente según el argumento recibido. Utilice el método de ordenamiento burbuja.
"""

numeros = []
number = None
print("programa para ordenar numeros de una lista")
print("ingrese numeros enteros para agregar a la lista, ingrese 0 para terminar")

while True:
    number = int(input("siguiente numero: "))
    if number == 0:
        print(f"la lista ha quedado asi: \n{numeros}")
        break
    else:
        numeros.append(number)
        print(numeros)

print("\nopciones:\n1. ASC\n2. DESC")
while True:
    select = int(input("desea ordenar la lista en orden ascendente o descendente? "))

    if select == 1:
        # Orden ascendente con burbuja
        n = len(numeros)
        for i in range(n):
            for j in range(0, n - i - 1):
                if numeros[j] > numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
        print("lista ordenada de forma ascendente:")
        print(numeros)
        break
    elif select == 2:
        # Orden descendente con burbuja
        n = len(numeros)
        for i in range(n):
            for j in range(0, n - i - 1):
                if numeros[j] < numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
        print("lista ordenada de forma ascendente:")
        print(numeros)
        break
    else:
        print("no entiendo esa orden")
