#07 Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 

from operator import concat
from tracemalloc import start


def lista_cuadrador(lista):
    lista_cuadrada = lista
    for i in range(len(lista_cuadrada)):
        lista_cuadrada[i] = lista_cuadrada[i] ** 2
    return lista_cuadrada
    

def crear_lista_num(tope):
    lists_num = []
    for i in range(tope):
        lists_num.append(i+1)
    return lists_num

def print_diez(lista):
    lista_print = lista
    if len(lista_print) > 10:
        start = len(lista_print) - 10
        for i in range(start, len(lista_print)):
            print(lista_print[i])
    else :
        for value in lista_print:
            print(value)

print_diez(lista_cuadrador(crear_lista_num(15)))
