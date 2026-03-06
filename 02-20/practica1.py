# promedio y estado

grades = []
tam = 3
sum = 0

for i in range(tam):
    grade = 0
    while grade < 1 or grade > 5:
        grade = int(input(f"nota: {i + 1}: "))
    grades.append(grade)

for i in range(len(grades)):
    sum = sum + grades[i]

average = sum / tam
print("------ESTADISTICAS------")
print(f"promedio: {average}")
status = ""
if(float(average > 1.7)):
    status = "aprobado"
else:
    status = "reprobado"

print(f"el alumno ha {status}")