#02 Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

#Esta actividad es un poco abierta a interpretacion, por lo tanto voy a aclarar esos detalles aqui. Año solo números positivos, Mes entre 1 y 12, día es el que va tener el mayor trabajo, hay que identificar la cantidad a base del mes y si es el año bisiesto o no.

def esFecha(dia, mes, año):

    '''
    Retorna True o False dependiendo si la fecha es valida o no.
    param.:
    dia: numero natural.
    mes: numero natural.
    año: numero natural.
    '''

    #esValido Es usado para guardar si es valido o no para luego retornar
    #esBisiesto igualmente es usado para luego hacer control dependiendo de si el año es bisiesto o no
    esValido = True
    esBisiesto = False

    #Lista de meses con 30 dias
    listaMesMin = [4,6,9,11]

    #Metodo para identificar si un año es bisiesto o no. 
    #Si un año es multiplo de 4 y no de 100 es bisiesto.
    #Si un año es multiplo de 4, de 100 y de 400 es bisiesto.
    if año % 4 == 0:
        if año % 100 != 0:
            esBisiesto = True
        elif año % 400 == 0:
            esBisiesto = True

    #Se comprueba las mas simples primero, luego si el mes es de 30 dias y por ultimo los dias en Febrero que es distinto si es bisiesto o no.
    if año < 1582 or mes < 1 or mes > 12 or dia > 31 or dia < 1:
        esValido = False
    elif mes in listaMesMin and dia > 30:
        esValido = False
    elif mes == 2 and esBisiesto and dia > 29:
        esValido = False
    elif mes == 2 and esBisiesto == False and dia > 28:
        esValido = False

    return esValido


print('Ingrese la fecha a comprobar')
diaEntregado = int(input('Escriba el número del día:'))
mesEntregado = int(input('Escriba el número del mes:'))
añoEntregado = int(input('Escriba el número del año:'))

if esFecha(diaEntregado,mesEntregado,añoEntregado):
    print(f'La fecha {diaEntregado}/{mesEntregado}/{añoEntregado} Es Valida')
else:
    print(f'La fecha {diaEntregado}/{mesEntregado}/{añoEntregado} No es Valida')




    
    
