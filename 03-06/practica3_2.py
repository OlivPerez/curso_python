# entrada y salida 2

# Crea un programa que lea dos números ingresados por el usuario y muestre en pantalla la suma, resta,
# multiplicación y división de ambos

n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))

print(f"suma = {n1 + n2}")
print(f"resta = {n1 - n2}")
print(f"multiplicacion = {n1 * n2}")
print(f"division = {n1 / n2 if n2 != 0 else 'no se puede dividir entre cero, idiota'}")