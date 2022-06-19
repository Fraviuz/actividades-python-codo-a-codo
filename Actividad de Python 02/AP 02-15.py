#15 Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas. 

def eliminar_de_cadena(cadena_entrada,posicion,cantidad):
    '''
    Retorna cadena modificada de manera tal ce se elimine los caracteres a partir de la posición dada y la cantidad.
    param:.
    posicion: Número Entero. Indice donde se empieza a eliminar los caracteres.
    cantidad: Número Entero. Cantidad de caracteres a eliminar.
    '''
    if posicion >= 0 and posicion + cantidad <= len(cadena_entrada):
        cadena_salida = cadena_entrada[0:posicion]
        cadena_salida += cadena_entrada[posicion+cantidad:len(cadena_entrada)]
        return cadena_salida
    else:
        return 'La posicion ingresada est fuera de index o la cantidad de caracteres supera la cantidad que hay después de la posición'

test_string = 'El carro de mi abuelo realmente necesita más que solo un pequeño arreglo. Lo que el necesita es intervención divina para poder andar de nuevo.'

print(eliminar_de_cadena(test_string,3,4))
print(eliminar_de_cadena(test_string,0,3))
print(eliminar_de_cadena(test_string,9,6))
print(eliminar_de_cadena(test_string,0,len(test_string)))
print(eliminar_de_cadena(test_string,0,len(test_string)+1))
print(eliminar_de_cadena(test_string,-2,1))
#Creo que se puede editar la función para que acepte posiciones negativas