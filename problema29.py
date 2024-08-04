def show_menu():
    print("Seleccione una opción para obtener una explicación:")
    print("1. Abstracción")
    print("2. Encapsulamiento")
    print("3. Herencia")
    print("4. Polimorfismo")
    print("5. Salir")

def Abstraccion():
    print("\nAbstracción:\nLa abstracción es el proceso de ocultar los detalles de implementación y mostrar solo la funcionalidad esencial.\nEn otras palabras, se enfoca en los aspectos relevantes del objeto que son necesarios para el contexto de uso.\n")

def Encapsulamiento():
    print("\nEncapsulamiento:\nEl encapsulamiento es el principio de ocultar los detalles internos de un objeto y permitir el acceso solo a través de métodos definidos.Esto ayuda a proteger los datos y la integridad del objeto.\n")

def Herencia():
    print("\nHerencia:\nLa herencia es un mecanismo por el cual una clase puede heredar propiedades y comportamientos de otra clase.Esto permite la reutilización de código y la creación de jerarquías de clases.\n")

def Polimorfismo():
    print("\nPolimorfismo:\nEl polimorfismo es la capacidad de un objeto para tomar muchas formas.En términos de programación, permite que una sola interfaz sea utilizada para diferentes tipos de objetos.\n")

def main():
    while True:
        show_menu()
        choice = input("Ingrese su elección (1-5): ")
        
        if choice == '1':
            Abstraccion()
        elif choice == '2':
            Encapsulamiento()
        elif choice == '3':
            Herencia()
        elif choice == '4':
            Polimorfismo()
        elif choice == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
