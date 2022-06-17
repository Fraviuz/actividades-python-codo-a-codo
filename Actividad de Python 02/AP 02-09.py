# 09 Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función. 

def es_ordenada(lista):
    '''
    Retorna True o False dependiendo si la lista en parámetros es ordenada o no.
    param:.
    lista: Lista a determinar si es ordenada o no.
    '''
    ordenada = lista.copy()
    
    ordenada.sort()

    if ordenada == lista:
        return True
    else:
        return False

lista_ordenada_palabras = ['Asfalto','Botella','Cilantro']
print(es_ordenada(lista_ordenada_palabras))
lista_no_ordenada_palabras = ['Roca','Ala','Zorro']
print(es_ordenada(lista_no_ordenada_palabras))
lista_ordenada_numeros = [1,2,3,4,5]
print(es_ordenada(lista_ordenada_numeros))
lista_no_ordenada_numeros = [100,2,35,4,-5]
print(es_ordenada(lista_no_ordenada_numeros))