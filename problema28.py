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


class CarroDeportivo(Carro):
    def __init__(self, modelo, marca, kilometros, velocidad_maxima):
        super().__init__(modelo, marca, kilometros)
        self.velocidad_maxima = velocidad_maxima

    def turbo(self):
        print("Turbo activado en", self.modelo, "a velocidad máxima de", self.velocidad_maxima, "km/h")

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

# Relación de dependencia
class Taller:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dueños = []
        self.mecanicos = []
        self.carros = []

    def añadir_dueño(self, dueño):
        self.dueños.append(dueño)
        print("Dueño", dueño.nombre, "añadido al taller", self.nombre)

    def añadir_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)
        print("Mecánico", mecanico.nombre, "añadido al taller", self.nombre)

    def añadir_carro(self, carro):
        self.carros.append(carro)
        print("Carro", carro.modelo, "añadido al taller", self.nombre)

    def mantener_carros(self):
        for mecanico in self.mecanicos:
            for carro in self.carros:
                mecanico.cambiar_aceite(carro)
                mecanico.revisar_motor(carro)

    def listar_dueños(self):
        for dueño in self.dueños:
            print("Dueño:", dueño.nombre)

    def listar_mecanicos(self):
        for mecanico in self.mecanicos:
            print("Mecánico:", mecanico.nombre)

    def listar_carros(self):
        for carro in self.carros:
            print("Carro:", carro.modelo)

#-------Declaración de cada carro
carro1 = Carro("nissan", "sentra", 46)
carro2 = Carro("jeep", "jeep", 50)
carro_deportivo1 = CarroDeportivo("Ferrari", "488", 10, 330)

#llantas
llanta1 = Llanta("Michelin", 16)
llanta2 = Llanta("Goodyear", 18)
llanta3 = Llanta("Pirelli", 20)

# Añadir llantas a los carros
carro1.añadir_llanta(llanta1)
carro2.añadir_llanta(llanta2)
carro_deportivo1.añadir_llanta(llanta3)

# Crear taller
taller = Taller("Taller Central")

# Interacciones con dueños y mecánicos
dueño = Dueño("pedro")
mecanico = Mecanico("juan")

# Añadir dueño, mecánico y carros al taller
taller.añadir_dueño(dueño)
taller.añadir_mecanico(mecanico)
taller.añadir_carro(carro1)
taller.añadir_carro(carro2)
taller.añadir_carro(carro_deportivo1)

# Listar dueños, mecánicos y carros en el taller
taller.listar_dueños()
taller.listar_mecanicos()
taller.listar_carros()

# Realizar mantenimiento a los carros en el taller
taller.mantener_carros()

# Usar el método turbo del carro deportivo
carro_deportivo1.turbo()
