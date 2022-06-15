#03 Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1. 

def cambio(total, recibido):

    '''
    Muestra en consola el cambio a entregar dividido en billetes de mayor a menor denominación.
    param.:
    total: Total de la compra.
    recibido: Monto recibido.
    '''

    cambioTotal = recibido-total
    billetes = 0
    cambioPrint = f'La compra es de ${total} y se abono ${recibido}, el vuelto debe contener: '

    if cambioTotal<0:
        print('El monto ingresado es insuficiente para pagar el total')
    else:
        while cambioTotal >= 500:
            billetes+=1
            cambioTotal-=500
        if billetes > 0 :
            cambioPrint= (f'{cambioPrint} {billetes} billetes de $500')
            billetes = 0

        while cambioTotal >= 100:
            billetes+=1
            cambioTotal-=100
        if billetes > 0 :
            cambioPrint= (f'{cambioPrint} {billetes} billetes de $100')
            billetes = 0

        if cambioTotal >= 50:
            cambioPrint= (f'{cambioPrint} 1 billete de $50')
            cambioTotal-=50

        while cambioTotal >= 20:
            billetes+=1
            cambioTotal-=20
        if billetes > 0 :
            cambioPrint= (f'{cambioPrint} {billetes} billetes de $20')
            billetes = 0

        if cambioTotal >= 10:
            cambioPrint= (f'{cambioPrint} 1 billete de $10')
            cambioTotal-=10

        if cambioTotal >= 1:
            cambioPrint= (f'{cambioPrint} {cambioTotal} billetes de $1')

        print(cambioPrint)

totalIngresado = int(input('Ingrese el total de la compra: '))
recibidoIngresado = int(input('Ingrese el dinero recibido: '))

cambio(totalIngresado,recibidoIngresado)

#Hay ina manera mas fácil de hacer esto pero luego lo hago (trabajar diferencia como una lista)