import sqlite3
connection = sqlite3.connect("dbTranslate.db")
try:
    connection.execute(
        """
        create table translate(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            es TEXT,
            en TEXT)
        """
    )
    print("se creo la tabla translate")
except sqlite3.OperationalError:
    print("la tabla translate ya existe")
connection.close()

# cargar datos
connection = sqlite3.connect("dbTranslate.db")
connection.execute("INSERT INTO translate(es, en) VALUES (?,?)", ("casa", "house"))
connection.execute("INSERT INTO translate(es, en) VALUES (?,?)", ("pluma", "feather"))
connection.execute("INSERT INTO translate(es, en) VALUES (?,?)", ("suerte", "luck"))
connection.execute("INSERT INTO translate(es, en) VALUES (?,?)", ("oro", "gold"))
connection.commit()
connection.close()

while True:
    print("traductor español a ingles")
    word = input("ingrese una palabra a traducir: ")
    connection = sqlite3.connect("dbTranslate.db")
    sentence = f"SELECT en FROM translate WHERE es = '{word}'"
    cursor = connection.execute(sentence)

    for record in cursor:
        print(f"{word} : {record[0]}")
    connection.close()
