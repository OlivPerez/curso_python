# ejercicios practicos sobre condicionales
# ejercicio 1

# Dados dos números leídos por teclado, imprimir el mayor y si es par o impar.
n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un segundo numero: "))
if(n1 > n2):
    print(f"{n1} es mayor")
elif(n1 < n2):
    print(f"{n2} es mayor")
else:
    print("ha introducido el mismo numero dos veces")


# ejercicio 2
# Escriba un programa para validar los datos de acceso ingresados por
# teclado por el usuario. Los datos leídos son user y password. Se
# deben imprimir “acceso correcto” si los valores ingresados son
# “admin” y 12345 respectivamente. En cualquier otro caso “acceso denegado”

print("ingrese su usuario y contraseña (el usuario es admin y la contraseña es 12345)")
user = "admin"
password = "12345"
userInput = input("usuario: ")
if user == userInput:
    passwordInput = input("contraseña: ")
    if password == passwordInput:
        print("sesion iniciada")
    else:
        print("contraseña incorrecta")
else:
    print("el usuario que intento ingresar no existe")


# ejercicios practicos sobre bucles
# ejercicio 3
# Escriba un programa que recibe las calificaciones de los alumnos de
# la materia de Programación Python e imprime el promedio general.
# El programa se detiene cuando lee el número cero. Tenga en cuenta
# que se desconoce cuantas calificaciones serán introducidas

alumnos = 0
total = 0
ingresado = 1
print("ingrese las calificaciones de los alumnos para calcular promedio. al finalizar escriba el numero 0")
while(ingresado != 0):
    ingresado = int(input(f"calificacion {alumnos + 1}: "))
    total = total + ingresado 
    alumnos = alumnos + 1
promedio = total / (alumnos - 1)
print(f"se han ingresado {alumnos - 1} calificaciones")
print(f"el promedio es de {promedio}")


# ejercicio 4
# Modifique el programa anterior para que las calificaciones
# permitidas solo sean 1 al 5

alumnos = 0
total = 0
ingresado = 1
print("ingrese las calificaciones de los alumnos para calcular promedio. al finalizar escriba el numero 0")
while(ingresado != 0):
    ingresado = int(input(f"calificacion {alumnos + 1}: "))
    if(ingresado < 0 or ingresado > 5):
        print("debe ingresar un numero del 1 al 5, o 0 para terminar")
    else:
        total = total + ingresado 
        alumnos = alumnos + 1
promedio = total / (alumnos - 1)
print(f"se han ingresado {alumnos - 1} calificaciones")
print(f"el promedio es de {promedio}")


# ejercicio 5
# Imprimir todos los números pares que existen entre dos números
# leídos por teclado usando bucles for

n1 = int(input(f"ingrese el primer numero: "))
n2 = int(input(f"ingrese el segundo numero: "))
pares = 0

for x in range(n1 + 1, n2):
    if(x % 2 == 0):
        print(x)
        pares = pares + 1
print(f"hay {pares} numeros pares entre {n1} y {n2}")


# ejercicio 6
# Imprimir un cuadrado y un triángulo con asteriscos o cualquier otra
# letra usando la estructura de repetición for()

for x in range(0, 5):
    for i in range(0, 6): 
        print(f"*", end = " ")
    print(end = "\n")

print("\n")

for x in range(0, 6):
    for i in range(x, 6): 
        print(f"*", end = " ")
    print(end = "\n")

