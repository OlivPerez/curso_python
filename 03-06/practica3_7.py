# listas

# Crea un programa que solicite al usuario 5 números y los almacene en una lista. Luego, muestra
# la lista y la suma de todos sus elementos.

numbers = []

for i in range(5):
    n = float(input(f"ingrese el numero que ocupara la posicion numero {i + 1}: "))
    numbers.append(n)

print("lista de numeros: ", numbers)
print("suma de numeros: ", sum(numbers))