# cargar una oracion por teclado
# imprime la cantidad de vocales que tiene

string = input("escriba una frase: ")
longStr = len(string)
vocals = 0

chars = ["a", "e", "i", "o", "u", 
         "A", "E", "I", "O", "U",
         "á", "é", "í", "ó", "ú",
         "Á", "É", "Í", "Ó", "Ú"
         ]

for i in string:
    if i in chars:
        vocals = vocals + 1

print(f"la cantidad de vocales en la cadena es de: {vocals}")

"""
for i in range(longStr):
    if (string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
        vocals = vocals + 1
"""


