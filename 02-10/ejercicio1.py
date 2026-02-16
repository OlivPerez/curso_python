"""
print("bienvenido al curso")
name = input("ingrese su nombre: ")
print("hola " + name)
"""

print("ingrese dos numeros para dividir: ")
num1 = int(input("dividendo: "))
num2 = int(input("divisor: "))

if num2 == 0:
    res= "Indeterminado, no se puede dividir entre cero"
else:
    res= str(num1/num2)

print("resultado: " + res)