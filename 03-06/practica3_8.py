# tuplas

# Define una tupla con los nombres de los meses del año. Luego, solicita al usuario un número
# del 1 al 12 y muestra el nombre del mes correspondiente.

months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
           "agosto", "setiembre", "octubre", "noviembre", "diciembre")
month_num = int(input("ingrese un numero del 1 al 12: "))

if(month_num <= 12 and month_num >= 1):
    print(f"el mes correspondiente es {months[month_num - 1]}")
else:
    print("el numero ingresado es invalido")