# 01 Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.


def mayor(num1, num2, num3):
    '''
    Retorna el valor máximo entre tres números positivo sólo si éste es único, de lo contrario retorna -1.
    param.:
    num1: numero natural.
    num2: numero natural.
    num3: numero natural.
    '''

    if num1 > num2:
        if num1 > num3:
            return num1
        elif num3 > num1:
            return num3
        else :
            return -1
    elif num2 > num1:
        if num2 > num3:
            return num2
        elif num3 > num2:
            return num3
        else :
            return -1
    elif num2 > num3:
        return -1
    elif num3 > num2:
        return num3
    else:
        return -1

'''
Prueba de la función

print(mayor(1, 1, 1)) #-1
print(mayor(0, 1, 1)) #-1
print(mayor(1, 0, 1)) #-1
print(mayor(1, 1, 0)) #-1
print(mayor(1, 0, 0)) # 1
print(mayor(0, 1, 0)) # 1
print(mayor(0, 0, 1)) # 1
'''

#Se pide en consola los 3 números asignados a primerNumero, segundoNumero y tercerNumero

print('Ingresar 3 números positivos')
primerNumero = int(input('Escriba el primer número:'))
segundoNumero = int(input('Escriba el segundo número:'))
tercerNumero = int(input('Escriba el tercer número:'))

#Control de que los números sean positivos

while primerNumero < 0 or segundoNumero < 0 or tercerNumero < 0:
    print('Alguno de los 3 números no es valido, por favor ingresar 3 números positivos (ejemplo.: 1, 5 y 7')
    primerNumero = int(input('Escriba el primer número:'))
    segundoNumero = int(input('Escriba el segundo número:'))
    tercerNumero = int(input('Escriba el tercer número:'))

#Se asigna el resultado de la función en 'resultado'

resultado = mayor(primerNumero, segundoNumero, tercerNumero)

#Se usa un if para mostrar en consola si hay un mayor valor y cual es o si no

if resultado == -1:
    print('No hay un mayor valor que los otros en los tres números dados.')
else:
    print(f'El mayor número es: {resultado}')
