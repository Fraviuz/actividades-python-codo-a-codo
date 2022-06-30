#10  En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total. 

class Cliente:

    def __init__(self, nombre):
        self.cantidad=0
        self.nombre = nombre


    def depositar(self, deposito):
        self.cantidad += deposito

    def extraer(self, extraccion):
        if self.cantidad - extraccion < 0:
            print('Extracción no es posible')
        else: 
            self.cantidad -= extraccion

    def mostrar_total(self):
        return self.cantidad

class Banco:

    def __init__(self):
        self.carlos = Cliente('Carlos')
        self.marta = Cliente('Marta')
        self.lisa = Cliente('Lisa')

    def operar(self):
        self.carlos.depositar(500)
        self.carlos.extraer(200)
        self.marta.depositar(100)
        self.marta.extraer(100)
        self.lisa.depositar(25)
        self.lisa.extraer(300)
        
    def deposito_total(self):
        print(f'Carlos tiene un deposito total de :{self.carlos.mostrar_total()}')
        print(f'Marta tiene un deposito total de :{self.marta.mostrar_total()}')
        print(f'Lisa tiene un deposito total de :{self.lisa.mostrar_total()}')

test_banco = Banco()
test_banco.operar()
test_banco.deposito_total()