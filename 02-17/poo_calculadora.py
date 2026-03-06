class Calculator:
    """calculadora simple para sumar, restar, multiplicar y dividir"""
    
    # atributos
    num1 = None
    num2 = None
    result = None
    history = []

    # constructor
    def __init__(self): # constructor init
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.history.append
    
    # metodos
    def load(self, x, y):
        self.num1 = x
        self.num2 = y
    
    def add(self):      # sumar
        result = self.num1 + self.num2
        return result
    
    def substract(self):# restar
        result = self.num1 - self.num2
        return result
    
    def multiply(self): # multiplicar
        result = self.num1 * self.num2
        return result
    
    def divide(self):   #dividir
        result = self.num1 / self.num2
        return result

    if __name__ == "__main__":
        #crear la instancia del objeto
        calc = Calculator()
        calc.load(12,3)
        print(f"el resultado de {calc.num1} mas {calc.num2} es {calc.sumar()}")
