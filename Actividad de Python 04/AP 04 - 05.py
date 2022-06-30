#05 Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar: Error: Imposible añadir elementos duplicados => [elemento].


def agregar_una_vez(lista, el):
    try:
        lista.index(el)
        print(f'Error: Imposible añadir elementos duplicados => [{el}]')
    except ValueError:
        lista.append(el)


elementos = ['test', 2]

agregar_una_vez(elementos, 3)
agregar_una_vez(elementos, 'testy')
agregar_una_vez(elementos, 2)

print(elementos)