# ingresar el sueldo de una persona, si supera los 800000000 millones mostrar un
# mensaje en pantalla indicando que debe abonar TRP.
# sino, mostrar el mensaje la persona debe abonar impuestos

IRP = 800000000000000
sueldo = int(input("ingrese de cuanto es sueldo: "))

sueldo_anual = sueldo * 12

if sueldo_anual > IRP:
    print("prepara el esfinter porque es necesario pagar impuestos")
else:
    print("que bueno, no es necesario pagar impuestos")