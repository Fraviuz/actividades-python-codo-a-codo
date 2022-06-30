import vehiculo

class Coche(vehiculo.Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        vehiculo.Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'Es de color {self.color}, tiene {self.ruedas} ruedas, puede alcanzar una velocidad de {self.velocidad} km/h y tiene una cilindrada de {self.cilindrada} cc'
