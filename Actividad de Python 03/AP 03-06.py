#06 Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no (>=4 aprueba).

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        '''
        Imprime en consola el nombre del alumno, su nota y si aprobó o no.
        '''
        print(f'El alumno {self.nombre} tiene una nota de {self.nota}')
        if self.nota >= 4:
            print('El alumno aprobó')
        else:
            print('El alumno reprobó')

lisa = Alumno('Lisa', 10)
bart = Alumno('Bart', 3)

lisa.imprimir()
bart.imprimir()

