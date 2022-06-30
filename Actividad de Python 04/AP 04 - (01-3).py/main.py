import coche, camioneta, bicicleta, motocicleta

def catalogar(lista, ruedas = -1):
    if ruedas == -1:
        for value in lista:
            print(type(value).__name__)
            print(f'{value} \n')
    else:
        encontrados = 0
        imprimir = ''
        for value in lista:
            if value.ruedas == ruedas:
                imprimir+= f'\n{type(value).__name__}'
                imprimir+= f'\n{value} \n'
                encontrados += 1
        print(f'Se han encontrado {encontrados} vehículos con {ruedas} ruedas:')
        print(imprimir)



def main():
    vehiculos = []

    carro_rojo = coche.Coche('Rojo', 4, 250, 1500)
    camioneta_azul = camioneta.Camioneta('Azul', 4, 300, 4000, 500)
    bicicleta_verde = bicicleta.Bicicleta('Verde', 2, "Voladora")
    moto_dorada = motocicleta.Motocicleta('Dorada', 2, 'Montañera', 350, 3000)

    vehiculos.append(carro_rojo)
    vehiculos.append(camioneta_azul)
    vehiculos.append(bicicleta_verde)
    vehiculos.append(moto_dorada)

    catalogar(vehiculos,0)
    catalogar(vehiculos,2)
    catalogar(vehiculos,4)
    catalogar(vehiculos)


if __name__ == "__main__":
    main()