#01 Crear la clase Persona con los métodos “set_nombre”, “set_edad”,“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.

#02 Agregarle a la clase anterior un constructor que reciba nombre y edad.

#03 Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.

#04 Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.

#05 Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self,nueva_nombre):
        self.nombre = nueva_nombre

    def set_edad(self,nueva_edad):
        self.edad = nueva_edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(f'{self.nombre} tiene {self.edad} años.')

    def es_mayor_de_edad(self):
        if self.edad > 17:
            return True
        else:
            return False

    def es_mayor_que(self, otra_persona):
        if self.edad > otra_persona.get_edad():
            print(f'{self.nombre} es mayor que {otra_persona.get_nombre()}')
        elif self.edad < otra_persona.get_edad():
            print(f'{otra_persona.get_nombre()} es mayor que {self.nombre}')
        else:
            print('ambos tienen la misma edad')

    def get_mayor(persona_uno, persona_dos): #buscar método estático
        if persona_uno.get_edad() > persona_dos.get_edad():
            return persona_uno
        elif persona_uno.get_edad() > persona_dos.get_edad():
            return persona_dos
        else:
            print('ambos tienen la misma edad')

    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años.'

carlos = Persona('Carlos',26)
carla = Persona('Carla',17)

carlos.print_persona()
carla.print_persona()

print(carlos.es_mayor_de_edad())
print(carla.es_mayor_de_edad())

carlos.es_mayor_que(carla)
carla.es_mayor_que(carlos)
carla.es_mayor_que(carla)

print(Persona.get_mayor(carlos,carla))