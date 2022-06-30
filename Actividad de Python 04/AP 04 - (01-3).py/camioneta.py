import coche

class Camioneta(coche.Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        coche.Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f'Es de color {self.color}, tiene {self.ruedas} ruedas, puede alcanzar una velocidad de {self.velocidad}km/h, tiene una cilindrada de {self.cilindrada}cc y puede tener una carga de {self.carga}kg'
