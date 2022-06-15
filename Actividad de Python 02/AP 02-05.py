# 05 Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. Desarrollar además un programa para verificar el comportamiento de la función.

def potencia(exponente):
    '''
    Retorna función lambda que potencia una base basada en el exponente definido.
    param.:
    exponente: numero entero usado como exponente.
    '''
    return lambda base : base ** exponente

al_Cuadrado = potencia(2)

base_ingresada = int(input('Ingresa numero de base:'))
print(al_Cuadrado(base_ingresada))
