#07 Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:

    import math

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

        #Se calculan los ángulos a base de los lados con la ley de coseno
        self.angulo_ab = self.math.degrees(self.math.acos((-lado_c**2 + lado_b**2 + lado_a**2)/(2*lado_a*lado_b)))
        self.angulo_bc = self.math.degrees(self.math.acos((-lado_a**2 + lado_b**2 + lado_c**2)/(2*lado_c*lado_b)))
        self.angulo_ca = 180 - self.angulo_ab - self.angulo_bc

    def mayor_lado(self):
        print(f'La longitud del lado mas grande es: {max(self.lado_a, self.lado_b, self.lado_c)}')

    def tipo_de_triangulo(self):
        imprimir = ''
        if self.lado_a == self.lado_b == self.lado_c:
            imprimir = f'El triangulo es Equilátero y Acutángulo.'
        elif self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
            imprimir = f'El triangulo es Isósceles'
            if max(self.angulo_ab, self.angulo_bc, self.angulo_ca) < 90:
                imprimir= f'{imprimir} y Acutángulo.'
            elif max(self.angulo_ab, self.angulo_bc, self.angulo_ca) > 90:
                imprimir= f'{imprimir} y Obtusángulo.'
            else:
                imprimir= f'{imprimir} y Rectángulo.'
        else:
            imprimir = f'El triangulo es escaleno'
            if max(self.angulo_ab, self.angulo_bc, self.angulo_ca) < 90:
                imprimir= f'{imprimir} y Acutángulo.'
            elif max(self.angulo_ab, self.angulo_bc, self.angulo_ca) > 90:
                imprimir= f'{imprimir} y Obtusángulo.'
            else:
                imprimir= f'{imprimir} y Rectángulo.'
        print(imprimir)

    def __str__(self):
        return f'Lado a: {self.lado_a}, Lado b: {self.lado_b}, Lado c: {self.lado_c}, angulo ab: {round(self.angulo_ab, 2)}, angulo bc: {round(self.angulo_bc, 2)}, angulo ca: {round(self.angulo_ca, 2)}.'

triangulo_prueba = Triangulo(2,1,2)
print(triangulo_prueba)
triangulo_prueba.mayor_lado()
triangulo_prueba.tipo_de_triangulo()
    