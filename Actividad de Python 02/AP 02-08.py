#08 Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

from os import remove


def eliminar_de_lista(lista,eliminar):
    nueva_lista = lista
    for a_eliminar in eliminar:
        for elemento in nueva_lista:
            if a_eliminar == elemento:
                nueva_lista.remove(a_eliminar)
    return nueva_lista

cosas= ['Carro', 'Casa', 'Seguridad', 'Dinero', 'Amor', 'PC', 'Dinero']
no_tengo= ['Carro', 'Dinero', 'Casa']

print(cosas)
print(no_tengo)
print(eliminar_de_lista(cosas, no_tengo))



    

        