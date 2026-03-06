# backend del crud

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"
database = "empleados.db"

def innit_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS empleados(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT NOT NULL,
                 apellido TEXT NOT NULL,
                 ci TEXT NOT NULL,
                 telefono TEXT NOT NULL,
                 direccion TEXT NOT NULL,
                 fechahora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn.get_db()
    empleados = conn.execute('SELECT * FROM empleados ORDER BY id DESC')
    conn.close()
    return render_template('index.html', empleados = empleados)

@app.route("/crear", methods = ["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellido = request.form["apellido"].strip()
        cedula = request.form["cedula"].strip()
        telefono = request.form["telefono"].strip()
        direccion = request.form["direccion"].strip()

        try:
            conn = get_db()
            con.execute('INSERT INTO empleados (nombre, apellido, cedula, telefono, direccion) VALUES (?, ?, ?, ?, ?)',
                    (nombre, apellido, cedula, telefono, direccion))
            conn.commit()
            conn.close()
            flash('Empleado registrado', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('La cédula ya existe', 'error')
    return render_template('crear.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)