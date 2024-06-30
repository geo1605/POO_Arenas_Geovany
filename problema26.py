class Carro:
    def __init__(self, modelo, marca, kilometros):
        #-------atributos----------
        self.modelo = modelo
        self.marca = marca
        self.kilometros = kilometros
        self.llantas = []
    #--------Métodos-------------
    def añadir_llanta(self, llanta):
        self.llantas.append(llanta)
        print("Llanta de marca", llanta.marca, "añadida al carro", self.modelo)
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

#asociación
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

#composición
class Llanta:
    def __init__(self, marca, tamaño):
        self.marca = marca
        self.tamaño = tamaño

    def inflar(self):
        print("La llanta de marca", self.marca, "ha sido inflada.")

    def desinflar(self):
        print("La llanta de marca", self.marca, "ha sido desinflada.")



#-------Declaración de cada carro
carro1 = Carro("nissan", "sentra", 46)
carro2 = Carro("jeep", "jeep", 50)

#llantas
llanta1 = Llanta("Michelin", 16)
llanta2 = Llanta("Goodyear", 18)

# Añadir llantas a los carros
carro1.añadir_llanta(llanta1)
carro2.añadir_llanta(llanta2)

# Interacciones con dueños y mecánicos
dueño = Dueño("pedro")
dueño.añadir(carro1)
dueño.añadir(carro2)
dueño.lista()
dueño.carros_uso()

mecanico = Mecanico("juan")
mecanico.cambiar_aceite(carro1)
mecanico.revisar_motor(carro2)
mecanico.lista_carros_mantenidos()