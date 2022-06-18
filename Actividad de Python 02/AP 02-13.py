#13 Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.

frase=str(input('Ingrese una frase:'))

def palabras_en_orden(cadena):
    '''
    Retorna lista ordenada (de menor caracteres a mayor) de palabras no repetidas presentes en el parámetro.
    param:.
    cadena: Cadena caracteres.
    '''

    palabra = ''
    set_palabras = set()
    lista_palabras = []
    
    for i in range(len(cadena)):
        if cadena[i] != ' ' and cadena[i] != ',' and cadena[i] != '.':
            #Operación lógica para solo guardar los caracteres de la cadena cunado no es un espacio ' ', una coma ',' o un punto '.'.
            palabra = f'{palabra}{cadena[i]}'
        elif cadena[i] == ' ' or i+1 == len(cadena):
            #En caso de ser un espacio o el ultimo carácter se guarda la palabra en el set (set_palabras) y la cadena(palabra) retorna a un estado vació.
            set_palabras.add(palabra)
            palabra = ''
    
    for value in set_palabras:
        #Loop para convertir el set en una lista para organizar con el método de lista sort().
        lista_palabras.append(value)
    
    lista_palabras.sort(key=len)
    
    return lista_palabras

print(palabras_en_orden(frase))

'''
cadena_prueba = 'El carro de mi abuelo realmente necesita más que solo un pequeño arreglo. Lo que el necesita es intervención divina para poder andar de nuevo.'
print(palabras_en_orden(cadena_prueba))
'''