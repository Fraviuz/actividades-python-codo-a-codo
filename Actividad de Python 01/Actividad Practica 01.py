#01 Escribe un programa muestre por pantalla “Hello World”.

'''
print('Hello World')
'''

#02 Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5

'''
print(3 + 5)
'''

#03 Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”

'''
nombreUsuario = input('¿Cual es su nombre?:')
print('Hola ' + nombreUsuario)
'''

#04 Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.

'''
primerNumero = int(input('Escriba el primer número a sumar:'))
segundoNumero = int(input('Escriba el segundo número:'))

suma = primerNumero + segundoNumero

print(f'El total es: {suma}')
'''

#05 Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.

'''
primerNumero = int(input('Escriba el primer número:'))
segundoNumero = int(input('Escriba el segundo número:'))

if primerNumero > segundoNumero:
    print(primerNumero)
elif primerNumero < segundoNumero:
    print(segundoNumero)
else :
    print('Ambos números son iguales')

#or

print(max(primerNumero, segundoNumero))
'''

#06 Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.

'''
primerNumero = int(input('Escriba el primer número:'))
segundoNumero = int(input('Escriba el segundo número:'))
tercerNumero = int(input('Escriba el tercer número:'))

if primerNumero > segundoNumero and primerNumero > tercerNumero:
    print(primerNumero)
elif segundoNumero > primerNumero and segundoNumero > tercerNumero:
    print(segundoNumero)
else :
    print(tercerNumero)

#or

print(max(primerNumero, segundoNumero, tercerNumero))
'''

#07 Escribe un programa que pida un número y diga si es divisible por 2

'''
numero = int(input('Escriba un número:'))

if numero % 2 == 0:
    print('Es par')
else :
    print('No es par')
'''

#08 Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)

'''
numero = int(input('Escriba un número:'))

if numero % 2 == 0:
    print('Es divisible por 2')
elif numero % 3 == 0 :
    print('Es divisible por 3')
elif numero % 5 == 0 :
    print('Es divisible por 5')
elif numero % 7 == 0 :
    print('Es divisible por 7')
'''

#09 Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)

'''
numero = int(input('Escriba un número:'))

if numero % 2 == 0:
    print('Es divisible por 2')

if numero % 3 == 0 :
    print('Es divisible por 3')

if numero % 5 == 0 :
    print('Es divisible por 5')

if numero % 7 == 0 :
    print('Es divisible por 7')
'''

#10 Escribir un programa que escriba en pantalla los divisores de un número dado

'''
numero = int(input('Escriba un número:'))

for x in range(1, numero):
    if numero % x == 0:
        print(f'Es divisible por {x}')
'''

#11 Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)

'''
numero = int(input('Escriba un número:'))
primoIndex = 0  

#primoIndex es usado para registrar cada vez que se encuentre un divisor en el loop, si es primo va ser igual a 1 con la unica excepcion siendo 1.

for x in range(1, numero):
    if numero % x == 0:
        primoIndex+=1

#Con if vemos primoIndex para ver si es primo o no (0 no es primo)

if primoIndex == 1 or numero == 1:
    print(f'El numero {numero} es primo')
else :
    print(f'El numero {numero} no es primo')
'''

#12 Pide una nota (número). Muestra la calificación según la nota:
#   0-3: Muy deficiente
#   3-5: Insuficiente
#   5-6: Suficiente
#   6-7: Bien
#   7-9: Notable
#   9-10: Sobresaliente

'''
nota = int(input('Escriba la nota:'))

# While para hacer control de la nota entreagada y pedir una nota valida

while nota > 10 or nota < 0:
    nota = int(input('La nota ingresada no es valida, porfavor ingresar una nota valida (entre 0 y 10):'))

#no es claro cules son las notas correspondientes asi que tome prioridad nota mayores (Ej. 9 es Sobresaliente y no Notable)

if nota > 8:
    print('Sobresaliente')
elif nota > 6:
    print('Notable')
elif nota > 5:
    print('Bien')
elif nota > 4:
    print('Suficiente')
elif nota > 2:
    print('Insuficiente')
else :
    print('Muy deficiente')
'''

#13 Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma: 
#1
#22
#333...

'''
#Se crea un loop para pasar por todos los números del 1 al 30, output es usado para guardar los numeros para luego ser mostrados. Luedo de crea otro loop para guardar en output el número en igual cantidad que dicho número

for i in range(1,31):
    output = ''
    for j in range(i):
        output = f'{output}{i}'
    print(output)
'''

#14 Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 3):
#333
#22
#1

'''
#El codigo es similar  la actividad anterior con dos diferencias, Se pide por un número positivo y se hace control, luego ese numero (piramideNum) es usado en el range para definir el limite. Se le da otros parametros a range() para revertir el orden

piramideNum = int(input('Escriba un número positivo:'))

while piramideNum < 0:
    piramideNum = int(input('El número ingresado ne es positivo, porfavor ingrese un número valido:'))

for i in range(piramideNum,0,-1):
    output = ''
    for j in range(i):
        output = f'{output}{i}'
    print(output)
'''

#15 Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal.

'''
#Primero tenemos un loop que pase por los números del 1 al 500

for i in range(1,501):

    #output para guardar lo que se va mostrar en pantalla

    output=f'{i}'

    #Control para ver si es multiple de 4 o 9 y si lo es se agrega al output para luego ser impreso

    if i % 4 == 0:
        output = f'{output} (Múltiplo de 4)'

    if i % 9 == 0:
        output = f'{output} (Múltiplo de 9)'

    print(output)

    #Cada 5 lineas (multiplo de 5) se muestra una linea de separacion

    if i % 5 == 0:
        print('------------------------------------------------------------')
'''