# practica sobrecondicionales, bucles y diccionarios

"""
escribe un programa para validar si los datos de acceso (usuario y
contraseña) se encuentran en el diccionario, validar solo 3 intentos
erroneos de contraseña usando ciclo while
"""

registered = {"user":"admin", "password":"admin"}
i = 0
while True:
    i = 1 + i
    if(i > 3):
        print("cuenta bloqueada por exceso de intentos fallidos")
        break
    else:
        user = input("ingrese su nombre de usuario: ")
        password = input("ingrese su contraseña: ")

        if(user == registered["user"] and password == registered["password"]):
            print("sesion iniciada correctamente")
            break
            
        else:
            print("usuario o contraseña incorrectas")
            print(f"le quedan {3 - i} intentos restantes")
    

    