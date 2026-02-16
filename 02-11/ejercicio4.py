# hecho por oliver perez

# Strings / cadenas de texto

nombre = "oliver"
apellido = "perez martinez"

print(nombre + " " + apellido)

texto = "este texto tiene \nsalto de linea y \ttabulacion"
print(texto)

# formateo
user, password, email = "oger", 12345, "admin@admin.com"
print("su usuario y contraseña son {}, {} y su email es {}" .format(user, password, email))
print("su usuario y contraseña son %s, %d y su email es %s" % (user, password, email))
print("su usuario y contraseña son " + user + ", " + str(password) + " y su email es " + email)
print(f"su usuario y contraseña son {user}, {password} y su email es {email}")