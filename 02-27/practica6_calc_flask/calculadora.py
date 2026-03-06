from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/calc", methods=["GET", "POST"])
def calc():
    # metodo POST
    if request.method == "POST":
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        operation = request.form["operation"]

        # implementar resta, multiplicacion y division
        if(operation == "+"):
            r = n1 + n2
        
        elif(operation == "-"):
            r = n1 - n2
        
        elif(operation == "*"):
            r = n1 * n2
        
        elif(operation == "/"):
            if(n2 != 0):
                r = n1 / n2
            else:
                r = "no se puede dividir entre cero"

        

        return render_template("index.html", result = r)
    
    elif request.method == "GET":
        return render_template("index.html")