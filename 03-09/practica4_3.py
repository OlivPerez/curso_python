# mostrar los numeros PARES del 1 al 100
# usando while y for

# while
i = 1
while(i <= 100):
    if(i % 2 == 0):
        print(i)
    i = i + 1

# for
for j in range(100):
    if(j % 2 == 0):
        print(j)