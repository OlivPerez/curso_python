# ejercicio 7
# Desarrollar un programa que encuentre números primos.

numero = 100 # numero a partir del cual se empezara a buscar primos
endless = True
while endless == True:
    numero = numero + 1
    primo = True
    for x in range(2, numero):
        if numero % x == 0:
            primo = False
    if primo == True:
        print(numero)


# Mejora el programa para que sea más eficiente y rápido
# a la hora de buscar números primos
numero = 100 # numero a partir del cual se empezara a buscar primos
endless = True
while endless == True:
    numero = numero + 1
    primo = True
    for x in range(2, int(numero/2)): # prueba con solo la mitad de los valores
        if numero % x == 0:
            primo = False # rompe el ciclo inmediato
            break
    if primo == True:
        print(numero)
