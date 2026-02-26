text = input("introduce un texto cualquiera: \n")
file_name = "archivo-" + text + ".txt"
f = open(file_name, "w") # apertura w= write, r = read, a = append
f.write(f"{text}\n")
f.close()