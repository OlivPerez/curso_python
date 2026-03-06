# Tkinter

# Crea una interfaz gráfica con Tkinter que contenga un botón. Al hacer clic en el botón,
# se debe abrir la calculadora de Windows (calc.exe)

import tkinter as tk
import os

def open_calc():
    os.system("calc")

window = tk.Tk()
window.title("abrir calculadora")

button = tk.Button(window, text="abrir calculadora", command=open_calc)
button.pack(pady=20)

window.mainloop()