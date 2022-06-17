# 04 Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:

'''
**********
**********
**********
**********
**********

**
****
******
********
**********
'''

def star_print_lineas(cantidad):
    '''
    Imprime parámetro cantidad de lineas con este formato ********** en consola.
    param:.
    cantidad: Número de lineas a imprimir.
    '''
    for i in range(cantidad):
        print('**********')

def star_print_escalera(cantidad):
    '''
    Imprime parámetro cantidad de lineas donde cada linea aumenta el formato a imprimir agregando ** al final.
    param:.
    cantidad: Número de lineas a imprimir.
    '''
    for i in range(cantidad):
        lineaPrint = ''
        sets = i
        while(sets >= 0):
            sets -= 1
            lineaPrint = f'{lineaPrint}**'
        print(lineaPrint)

star_print_lineas(5)
star_print_escalera(5)


