# Crear una aplicación que utilice funciones para cargar una lista y
# otra para imprimir el contenido.

def cargar_lista(): # aqui se define una funcion llamada cargar_lista
    v = input("ingrese un valor: ")
    lista.append(v) # se agrega lo que contiene la variable v a la lista

def imprimir_lista(): # aqui se define otra funcion llamada imprimir_lista
    print("elementos de la lista: ")
    print(lista)

endless = True
lista = ["1"]

while endless == True:
    print("seleccione una opcion:")
    opcion = int(input("1. cargar nuevo\n2. mostrar lista\n3. salir\n"))
    if opcion == 1:
        cargar_lista()
    elif opcion == 2:
        imprimir_lista()
    elif opcion == 3:
        print("saliendo del programa")
        break
    else:
        print("no entiendo esa orden")
 