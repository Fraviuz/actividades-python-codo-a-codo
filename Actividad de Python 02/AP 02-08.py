#08 Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

from os import remove

def eliminar_de_lista(lista,eliminar):
    '''
    Retorna copia de la primera lista la cual se le eliminan los elementos de la segunda lista.
    param:.
    lista: Lista de elementos a copiar.
    eliminar: Lista de elementos a eliminar.
    '''
    nueva_lista = lista.copy()

    for a_eliminar in eliminar:
        for elemento in nueva_lista:
            if a_eliminar == elemento:
                nueva_lista.remove(a_eliminar)

    return nueva_lista

cosas= ['Carro', 'Casa', 'Dolor de cabeza', 'Dinero', 'Amor', 'Vida', 'Dinero']
no_tengo= ['Carro', 'Dinero', 'Casa']
si_tengo= eliminar_de_lista(cosas, no_tengo)

print(cosas)
print(no_tengo)
print(si_tengo)



    

        