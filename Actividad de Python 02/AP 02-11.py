#  Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.

import math

def centrador(cadena):
    '''
    Imprime en consola la cadena recibida centrada suponiendo que esta es limitada por 80 columnas.
    param:.
    cadena: Cadena de caracteres a centrar.
    '''

    imprimir = ''

    for i in range(40 - math.ceil(len(cadena)/2)):
        imprimir = f'{imprimir} '

    imprimir = f'{imprimir}{cadena}'

    for i in range(40 - math.floor(len(cadena)/2)):
        imprimir = f'{imprimir} '

    print(imprimir)


centrador('Computation')
centrador('Revalidation')
centrador('tion')

