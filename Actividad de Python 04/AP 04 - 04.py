#04 Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución: resultado = 10/0

try:
    resultado = 10/0
    print(resultado)
except Exception as e:
    print(f'{type(e).__name__} No se puede dividir entre 0')

#Honestamente creo que esta actividad debería ser más extensa