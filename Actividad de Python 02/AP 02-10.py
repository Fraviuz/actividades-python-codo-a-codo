#10 Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.

def es_capicua(cadena):
    '''
    Retorna True o False dependiendo si una cadena de caracteres or números es capicúa o no.
    param:.
    cadena: Cadena/String de caracteres o una serie de números.
    '''
    caracteres = len(str(cadena)) - 1
    capicua = True
    i = 0

    while i < len(str(cadena)) and capicua:
        if str(cadena)[i] != str(cadena)[caracteres]:
            capicua = False
        caracteres-= 1
        i += 1
        
    return capicua

print(es_capicua('toot')) #True
print(es_capicua('tooy')) #False
print(es_capicua(1001)) #True
print(es_capicua(1002)) #False
print(es_capicua(10101)) #True