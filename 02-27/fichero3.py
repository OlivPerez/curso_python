
# escritura
file = open("data.text", "w")
text = input("ingrese un texto a guardar: ")
file.write(text)
file.close()

# append, actualizar fichero
file = open("data.text", "a")

text = input("ingrese otro texto: ")
file.write(text)
file.close()

# leer fichero
file = open("data.text", "r")
for x in file:
    print(x)
file.close()
