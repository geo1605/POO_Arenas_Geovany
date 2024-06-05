lista = [["numero de tarea", "tarea"]]
x = 0
z = 1
n = 0
while x != 3:
    print("----creador de tareas----")
    print("1. Agregar tarea")
    print("2. Terminar tarea")
    print("3. salir")
    y = int(input())
    x = y
    if y == 1:
        n = n + 1
        tarea = str(input("escribe la tarea: "))
        lista.append([n,tarea])
    if y == 2:
        if len(lista) == 1:
            print("No hay tareas para eliminar.")
        else:
            for tarea in lista:
                if tarea[0] != "numero de tarea": 
                    print(f'{tarea[0]} "{tarea[1]}"')
            try:
                num_eliminar = int(input("elije el numero que quieres remover: "))
                tarea_encontrada = False
                for tarea in lista:
                    if tarea[0] == num_eliminar:
                        lista.remove(tarea)
                        tarea_encontrada = True
                        break
                if not tarea_encontrada:
                    print("Numero de tarea no encontrado.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")

for tarea in lista:
    print(f'{tarea[0]} "{tarea[1]}"')

