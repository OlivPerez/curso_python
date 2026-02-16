# realizar un programa que calcule el perimetro y area de 
# las siguientes figuras: rectangulo, triangulo y circulo

pi = 3.14
endless = True

def getRectanguloP(largo, ancho):
    return (largo + ancho) * 2

def getRectanguloA(largo, ancho):
    return(largo * ancho)

def getTrianguloP(l1, l2, l3):
    return(l1 + l2 + l3)

def getTrianguloA(base, altura):
    return((base * altura)/2)

def getCirculoP(radio):
    return(2 * pi * radio)

def getCirculoA(radio):
    return(pi * (radio ** 2))

def menu():
    print("calculadora geometrica, que desea calcular?")
    print("1. perimetro de rectangulo")
    print("2. area de rectangulo")
    print("3. perimetro de triangulo")
    print("4. area de triangulo")
    print("5. perimetro de circulo")
    print("6. area de circulo")
    print("7. salir")
    select = input("seleccione una opcion: ")
    return select

while endless == True:
    select = menu()
    if select == "1":
        largo = float(input("ingrese largo del rectangulo: "))
        ancho = float(input("ingrese ancho del rectangulo: "))
        resultado = getRectanguloP(largo, ancho)
        print(f"perimetro del rectangulo: {resultado}\n")

    elif select == "2":
        largo = float(input("ingrese largo del rectangulo: "))
        ancho = float(input("ingrese ancho del rectangulo: "))
        resultado = getRectanguloA(largo, ancho)
        print(f"Area del rectangulo: {resultado}\n")

    elif select == "3":
        l1 = float(input("ingrese lo que mide el primer lado: "))
        l2 = float(input("ingrese lo que mide el segundo lado: "))
        l3 = float(input("ingrese lo que mide el tercer lado: "))
        resultado = getTrianguloP(l1, l2, l3)
        print(f"perimetro del triangulo: {resultado}\n")

    elif select == "4":
        base = float(input("ingrese lo que mide la base del rectangulo: "))
        altura = float(input("ingrese lo que mide la altura del triangulo: "))
        resultado = getTrianguloA(base, altura)
        print(f"area del triangulo: {resultado}\n")

    elif select == "5":
        radio = float(input("ingrese lo que mide el radio del circulo: "))
        resultado = getCirculoP(radio)
        print(f"perimetro del circulo: {resultado}\n")

    elif select == "6":
        radio = float(input("ingrese lo que mide el radio del circulo: "))
        resultado = getCirculoA(radio)
        print(f"area del circulo: {resultado}\n")

    elif select == "7":
        print("saliendo del programa\n")
        break
    else:
        print("no entiendo lo que quieres hacer\n")
