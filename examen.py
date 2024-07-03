#clase padre 
class Carro:
    def __init__(self, modelo, marca, kilometros):
        self.modelo = modelo
        self.marca = marca
        self.kilometros = kilometros
        self.llantas = []
        self.motor = None
        self.frenos = None

    def añadir_llanta(self, llanta):
        self.llantas.append(llanta)
        print("Llanta de marca", llanta.marca, "añadida al carro", self.modelo)

    def añadir_motor(self, motor):
        self.motor = motor
        print("Motor de marca", motor.marca, "añadido al carro", self.modelo)

    def añadir_frenos(self, frenos):
        self.frenos = frenos
        print("Frenos de tipo", frenos.tipo, "añadidos al carro", self.modelo)

    def acelera(self):
        print("El carro", self.modelo, "está acelerando.")

    def frena(self):
        print("El carro", self.modelo, "está frenando.")

#herencia
class CarroDeportivo(Carro):
    def __init__(self, modelo, marca, kilometros, velocidad_maxima):
        super().__init__(modelo, marca, kilometros)
        self.velocidad_maxima = velocidad_maxima

    def turbo(self):
        print("Turbo activado en", self.modelo, "a velocidad máxima de", self.velocidad_maxima, "km/h")

#dependencia
class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carros = []

    def añadir(self, carro):
        self.carros.append(carro)
        print(carro.modelo, "añadido a carros de", self.nombre)

    def lista(self):
        for carro in self.carros:
            print(carro.modelo)

    def carros_uso(self):
        for carro in self.carros:
            carro.acelera()

#asociación
class Mecanico:
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


class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

    def arrancar(self):
        print("El motor de marca", self.marca, "ha arrancado.")

    def apagar(self):
        print("El motor de marca", self.marca, "ha sido apagado.")


class Frenos:
    def __init__(self, tipo):
        self.tipo = tipo

    def aplicar(self):
        print("Frenos de tipo", self.tipo, "aplicados.")

    def liberar(self):
        print("Frenos de tipo", self.tipo, "liberados.")

#dependencia
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


carro1 = Carro("Nissan", "Sentra", 46)
carro2 = Carro("Jeep", "Wrangler", 50)
carro_deportivo1 = CarroDeportivo("Ferrari", "488", 10, 330)

llanta1 = Llanta("Michelin", 16)
llanta2 = Llanta("Goodyear", 18)
llanta3 = Llanta("Pirelli", 20)

motor1 = Motor("Honda", 120)
motor2 = Motor("Ford", 200)

frenos1 = Frenos("Disco")
frenos2 = Frenos("Tambor")

carro1.añadir_llanta(llanta1)
carro2.añadir_llanta(llanta2)
carro_deportivo1.añadir_llanta(llanta3)

carro1.añadir_motor(motor1)
carro2.añadir_motor(motor2)
carro_deportivo1.añadir_motor(motor1)

carro1.añadir_frenos(frenos1)
carro2.añadir_frenos(frenos2)
carro_deportivo1.añadir_frenos(frenos1)

taller = Taller("Taller Central")

dueño = Dueño("Pedro")
mecanico = Mecanico("Juan")

# Añadir dueño, mecánico y carros al taller
taller.añadir_dueño(dueño)
taller.añadir_mecanico(mecanico)
taller.añadir_carro(carro1)
taller.añadir_carro(carro2)
taller.añadir_carro(carro_deportivo1)

while True:
    print("\nMenú:")
    print("1. Listar dueños")
    print("2. Listar mecánicos")
    print("3. Listar carros")
    print("4. Realizar mantenimiento a los carros")
    print("5. Activar turbo del carro deportivo")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        taller.listar_dueños()
    elif opcion == "2":
        taller.listar_mecanicos()
    elif opcion == "3":
        taller.listar_carros()
    elif opcion == "4":
        taller.mantener_carros()
    elif opcion == "5":
        carro_deportivo1.turbo()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

