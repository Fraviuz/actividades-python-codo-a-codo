import vehiculo

class Bicicleta(vehiculo.Vehiculo):

    def __init__(self, color, ruedas, tipo):
        vehiculo.Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Es de color {self.color}, tiene {self.ruedas} ruedas y es {self.tipo}'
