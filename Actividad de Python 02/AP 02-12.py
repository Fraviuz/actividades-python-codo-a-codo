#12 Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento. 

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

    #Lista de meses con 30 días
    listaMesMin = [4,6,9,11]

    #Método para identificar si un año es bisiesto o no. 
    #Si un año es múltiplo de 4 y no de 100 es bisiesto.
    #Si un año es múltiplo de 4, de 100 y de 400 es bisiesto.
    if año % 4 == 0:
        if año % 100 != 0:
            esBisiesto = True
        elif año % 400 == 0:
            esBisiesto = True

    #Se comprueba las mas simples primero, luego si el mes es de 30 días y por ultimo los días en Febrero que es distinto si es bisiesto o no.
    if año < 1582 or mes < 1 or mes > 12 or dia > 31 or dia < 1:
        esValido = False
    elif mes in listaMesMin and dia > 30:
        esValido = False
    elif mes == 2 and esBisiesto and dia > 29:
        esValido = False
    elif mes == 2 and esBisiesto == False and dia > 28:
        esValido = False

    return esValido

def fecha_larga(fecha_tupla):
    '''
    Retorna cadena con fecha en formato largo.
    param:.
    fecha_tupla: Tupla con números correspondientes al dia, mes y año.
    '''

    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

    dia = fecha_tupla[0]
    mes = fecha_tupla[1]
    año = 2000 + fecha_tupla[2]

    if esFecha(dia, mes, año):
        fecha = f'{str(dia)} de {str(meses[mes-1])} de {str(año)}'
        return fecha
    else:
        return 'Fecha ingresada en Tupla no es valida'

fecha_1 = (17, 6, 22)
fecha_2 = (21, 2, 18)
fecha_3 = (31, 6, 10)

print(fecha_larga(fecha_1))
print(fecha_larga(fecha_2))
print(fecha_larga(fecha_3))