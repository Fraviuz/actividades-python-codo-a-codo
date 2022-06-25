#09 Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, Editar contacto, Cerrar agenda.

class Agenda:

    contactos = []

    def new_contacto(self, nombre, telefono, email):
        '''
        Crea un nuevo diccionario 'contacto' que luego es agregado a la lista contactos.
        param:.
        nombre: Cadena de texto, Nombre del contacto.
        telefono: Número natural, teléfono del contacto.
        email: Cadena de texto, Email del contacto.
        '''
        contacto = {
            'nombre':nombre,
            'teléfono':telefono,
            'email':email
        }

        self.contactos.append(contacto)

        print()
        print(f'{len(self.contactos)-1} - Nombre: {contacto["nombre"]} Teléfono: {contacto["teléfono"]} Email: {contacto["email"]}')

    def lista_de_contactos(self):
        '''
        Muestra contactos en la lista 'contactos' o si no hay contactos imprime 'No hay contactos agendados'.
        '''
        if len(self.contactos) == 0:
            print('No hay contactos agendados.')
        else:
            for i in range(len(self.contactos)):
                print(f'{i} - Nombre: {self.contactos[i]["nombre"]} Teléfono: {self.contactos[i]["teléfono"]} Email: {self.contactos[i]["email"]}')

    def buscar(self, dato):
        #dos cosas que se pueden hacer para mejorar este método es retornar si el contacto existe y hacer búsquedas parciales o hacer que retorne el indice y crear un método que imprima el contacto basado en el indice.
        '''
        Imprime contacto buscado, puede ser nombre, email o número de teléfono. Si no es encontrado imprime 'Contacto no se encuentra el la agenda'.
        '''
        contacto_existe = False

        for i in range(len(self.contactos)):
            if self.contactos[i]['nombre'] == dato or self.contactos[i]['email'] == dato or str(self.contactos[i]['teléfono']) == dato:
                print(f'{i} - Nombre: {self.contactos[i]["nombre"]} Teléfono: {self.contactos[i]["teléfono"]} Email: {self.contactos[i]["email"]}')
                contacto_existe = True

        if contacto_existe == False:
            print('Contacto no se encuentra el la agenda')


    def editar_contacto(self, indice, llave, nuevo_contenido):
        '''
        Updates contenido del contacto en el diccionario de contactos.
        param:.
        indice: Número natural, indice del contacto
        llave: Cadena de texto, representa la llave del diccionario contacto.
        nuevo_contenido: Cadena de texto, nombre, número o email nuevo.
        '''
        self.contactos[indice].update({llave:nuevo_contenido})

    def cantidad_de_contactos(self):
        return len(self.contactos)

    def imprimir_contacto_indice(self, indice):
        print(f'{indice} - Nombre: {self.contactos[indice]["nombre"]} Teléfono: {self.contactos[indice]["teléfono"]} Email: {self.contactos[indice]["email"]}')



test_agenda = Agenda()

#Menu en consola
numero_ingresado = -1
while numero_ingresado != 0:
    print('--------------------------------')
    print('1 - Nuevo Contacto')
    print('2 - Lista de contactos')
    print('3 - Buscar un contacto')
    print('4 - Editar un contacto')
    print('0 - Cerrar Agenda')
    numero_ingresado=int(input('Seleccionar Opción: '))
    print('--------------------------------')

    if numero_ingresado == 1:
        #Nuevo contacto

        nombre=input('Ingrese nombre del contacto: ')
        telefono=int(input('Ingrese teléfono del contacto: '))
        email=input('Ingrese email del contacto: ')

        test_agenda.new_contacto(nombre, telefono, email)

    if numero_ingresado == 2:
        #Lista de Contacto

        test_agenda.lista_de_contactos()

    if numero_ingresado == 3:
        #Buscar contacto

        dato_ingresado=input('Contacto buscar: ')
        test_agenda.buscar(dato_ingresado)


    if numero_ingresado == 4:
        #Editar contacto

        numero_ingresado=int(input('Ingrese el indice de contacto a editar o -1 para cancelar: '))

        while numero_ingresado > test_agenda.cantidad_de_contactos()-1 or numero_ingresado < -1:
            #Control de numero ingresado
            print('Numero de indice no existe')
            numero_ingresado=int(input('Ingrese numero de contacto a editar (indice) o -1 para cancelar: '))

        if numero_ingresado != -1:
            indice= numero_ingresado
            while numero_ingresado != 4:
                print('--------------------------------')
                test_agenda.imprimir_contacto_indice(indice)
                print('--------------------------------')
                print('1 - Editar nombre')
                print('2 - Editar teléfono')
                print('3 - Editar email')
                print('4 - Finalizar edición')
                numero_ingresado=int(input('Seleccionar Opción: '))
                print('--------------------------------')

                if numero_ingresado == 1:
                    nuevo_nombre = input('Ingrese nuevo nombre: ')
                    test_agenda.editar_contacto(indice, 'nombre', nuevo_nombre)

                if numero_ingresado == 2:
                    nuevo_telefono = int(input('Ingrese nuevo nombre: '))
                    test_agenda.editar_contacto(indice, 'nombre', nuevo_telefono)

                if numero_ingresado == 3:
                    nuevo_email = input('Ingrese nuevo email: ')
                    test_agenda.editar_contacto(indice, 'nombre', nuevo_email)




