"""
Implementar un traductor de palabras del español a inglés usando la estructura de diccionario. 
Debe solicitar una palabra al usuario y verificar si existe en el diccionario y mostrar la traducción.
En caso de no existir la palabra en el diccionario, solicitar si desea agregar al diccionario.
El diccionario se detiene al introducir 0
"""

dictionary = {
    "partner":"compañero", 
    "client":"cliente", 
    "boss":"jefe", 
    "friend":"amigo", 
    "comrade":"camarada"
}

print("diccionario")
print("ingrese una palabra para traducir (solo minusculas): ")
word = input("palabra: ")


# buscar primero por clave (ingles) 
if word in dictionary: 
    print(f"Traducción: {dictionary[word]}") 

# buscar por valor (español) 
elif word in dictionary.values(): 
# recorrer items para encontrar la clave correspondiente 
    for key, value in dictionary.items(): 
        if value == word: 
            print(f"Traducción: {key}") 
            break 

else: 
    print("La palabra no está en el diccionario.")
