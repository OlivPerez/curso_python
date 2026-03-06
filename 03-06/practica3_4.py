# Estructuras condicionales 2

# Crea un programa que solicite tres números y determine cuál es el mayor.

a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))
c = float(input("ingrese el ultimo numero: "))

largest = max(a, b, c)
print(f"el numero mas alto es {largest}")