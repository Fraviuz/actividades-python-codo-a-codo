import coche, camioneta, bicicleta, motocicleta

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

    for value in vehiculos:
        print(value)


if __name__ == "__main__":
    main()