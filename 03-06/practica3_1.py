# entrada y salida 1

# Escribe un programa que solicite al usuario su nombre y edad, y luego muestre un mensaje con esa
# información en el formato:"Hola, [nombre]. Tienes [edad] años."

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
edadStr = str(edad)
print(f"bienvenido, {nombre}, tienes {edadStr} años, ¿no es asi?")