#14  Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

def eliminar_claves(diccionario, claves):
    '''
    Retorna diccionario resultado de remover las llaves/claves ingresadas en la lista de el diccionario ingresado.
    param:.
    diccionario: Diccionario a copiar y remover las llaves.
    claves: Lista de llaves a eliminar.
    '''
    nuevo_diccionario = diccionario.copy()
    llaves = nuevo_diccionario.keys()
    for value in claves:
        if value in llaves:
            nuevo_diccionario.pop(value)
    return nuevo_diccionario

test = {
    'key1':'key1',
    'key2':'key2',
    'key3':'key3',
    'key4':'key4'
}

keys = ['key1','key5']

print(eliminar_claves(test,keys))