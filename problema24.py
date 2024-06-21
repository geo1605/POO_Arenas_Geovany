class Carro:
    def __init__(self, modelo, marca, kilómetros):
        #-------atributos----------
        self.modelo = modelo
        self.marca = marca
        self.kilometros = kilómetros
    #--------Métodos-------------
    def acelera():
        print("acelera")#imprimir
    def freno():
        print("freno")#imprimir
    
class Dueño: #segunda clase
    def __init__(self, nombre): # asignacion
        self.nombre = nombre
        self.carros = []

    def añadir(self, Carro):
        self.carros.append(Carro) #agregar carros a dueño
        print(Carro.modelo, " añadido a carros de ", self.nombre)
    
    def lista(self):
        for carros in self.carros:
            print(carros.modelo)
    
    def carros_uso(self):
        for carros in self.carros:
            Carro.acelera()

    
#-------Declaración de cada carro
carro1 = Carro("nissan", "sentra", 46)
carro2 = Carro("jeep", "jeep", 50)
dueño = Dueño("pedro")

dueño.añadir(carro1)
dueño.añadir(carro2)
dueño.lista()
dueño.carros_uso()
