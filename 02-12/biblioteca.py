# Crear una aplicación agenda para guardar el nombre y el teléfono


agenda = {"emergencia": "911", "bomberos": "120"}
def cargar_nuevo():
    nombre = input("ingrese nombre: ")
    telefono = input("ingrese numero de telefono: ")
    agenda[nombre] = telefono
    
def ver_contactos():
    print(agenda)

true = True
while true == True:
    print("agenda telefonica")
    op = input("1. cargar nuevo\n2. ver contactos\n3. salir\nseleccione una opcion: ")
    if op == "1":
        cargar_nuevo()
      
    elif op == "2":
        ver_contactos()
    elif op == "3":
        print("saliendo del programa")
        break
    else:
        print("no entiendo esa orden")