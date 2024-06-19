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
    
#-------Declaración de cada carro
carro1 = Carro("nissan", "sentra", 46)
carro2 = Carro("jeep", "jeep", 50)
