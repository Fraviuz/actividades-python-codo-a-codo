import bicicleta

class Motocicleta(bicicleta.Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        bicicleta.Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        

    def __str__(self):
        return f'Es de color {self.color}, tiene {self.ruedas} ruedas, es {self.tipo}, puede alcanzar una velocidad de {self.velocidad}km/h y tiene una cilindrada de {self.cilindrada}cc'
