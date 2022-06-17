#06 Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.

es_par = lambda a : True if (a % 2 == 0) else False

numero_ingresado = int(input('Ingresa número a chequear:'))

if es_par(numero_ingresado):
    print('Es par')
else:
    print('Es impar')