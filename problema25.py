class Carro:
    def __init__(self, modelo, marca, kilometros):
        #-------atributos----------
        self.modelo = modelo
        self.marca = marca
        self.kilometros = kilometros
    #--------Métodos-------------
    def acelera(self):
        print("acelera")  # imprimir

    def frena(self):
        print("frena")  # imprimir


class Dueño:  # segunda clase
    def __init__(self, nombre):  # asignacion
        self.nombre = nombre
        self.carros = []

    def añadir(self, carro):
        self.carros.append(carro)  # agregar carros a dueño
        print(carro.modelo, "añadido a carros de", self.nombre)

    def lista(self):
        for carro in self.carros:
            print(carro.modelo)

    def carros_uso(self):
        for carro in self.carros:
            carro.acelera()


class Mecanico:  # tercera clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros_mantenidos = []

    def cambiar_aceite(self, carro):
        self.carros_mantenidos.append(carro)
        print("Cambio de aceite realizado en", carro.modelo, "por", self.nombre)

    def revisar_motor(self, carro):
        self.carros_mantenidos.append(carro)
        print("Revisión del motor realizada en", carro.modelo, "por", self.nombre)

    def lista_carros_mantenidos(self):
        for carro in self.carros_mantenidos:
            print("Carro mantenido:", carro.modelo)




#-------Declaración de cada carro
carro1 = Carro("nissan", "sentra", 46)
carro2 = Carro("jeep", "jeep", 50)

dueño = Dueño("pedro")
dueño.añadir(carro1)
dueño.añadir(carro2)
dueño.lista()
dueño.carros_uso()

mecanico = Mecanico("juan")
mecanico.cambiar_aceite(carro1)
mecanico.revisar_motor(carro2)
mecanico.lista_carros_mantenidos()
