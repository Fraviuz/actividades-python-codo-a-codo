#08 Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos.Llamar a la clase Calculadora

class Calculadora:

    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def suma(self):
        print(self.numero_1 + self.numero_2)

    def resta(self):
        print(self.numero_1 - self.numero_2)

    def multiplicacion(self):
        print(self.numero_1 * self.numero_2)

    def division(self):
        print(self.numero_1 / self.numero_2)