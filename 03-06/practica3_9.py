# Diccionarios

# Crea un diccionario donde las claves sean nombres de estudiantes y los valores sean sus notas.
# Luego, solicita un nombre al usuario e indica la nota correspondiente.

grades = {"juan" : 85, "maria" : 90, "peter" : 78, "jeanne" : 92}
name = input("ingrese el nombre del estudiante a revisar: ")

if name in grades:
    print(f"la nota del estudiante es de {grades[name]}")
else:
    print("estudiante no encontrado")