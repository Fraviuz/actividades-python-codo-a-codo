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

def starPrintLines(cantidad):
    for i in range(cantidad):
        print('**********')

def starPrintPiramide(cantidad):
    for i in range(cantidad):
        lineaPrint = ''
        sets = i
        while(sets >= 0):
            sets -= 1
            lineaPrint = f'{lineaPrint}**'
        print(lineaPrint)

starPrintLines(5)
starPrintPiramide(5)


