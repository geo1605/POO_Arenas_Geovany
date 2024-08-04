import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'escu',
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    def in_estudiante():
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        grado = input("Grado: ")
        email = input("Email: ")
        insert_query = "INSERT INTO estudiantes (nombre, edad, grado, email) VALUES (%s, %s, %s, %s)"
        data = (nombre, edad, grado, email)
        cursor.execute(insert_query, data)
        cnx.commit()
        print("Estudiante insertado correctamente.")

    def sel_estudiante():
        select_query = "SELECT * FROM estudiantes"
        cursor.execute(select_query)
        for (id, nombre, edad, grado, email) in cursor:
            print(f"{id}, {nombre}, {edad}, {grado}, {email}")
        print("Datos seleccionados correctamente.")

    def ed_estudiante():
        id = int(input("ID del estudiante a actualizar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        update_query = "UPDATE estudiantes SET nombre = %s WHERE id = %s"
        data = (nuevo_nombre, id)
        cursor.execute(update_query, data)
        cnx.commit()
        print("Estudiante actualizado correctamente.")

    def el_student():
        id = int(input("ID del estudiante a eliminar: "))
        delete_query = "DELETE FROM estudiantes WHERE id = %s"
        data = (id,)
        cursor.execute(delete_query, data)
        cnx.commit()
        print("Estudiante eliminado correctamente.")

    while True:
        print("Seleccione una opción:")
        print("1. Insertar estudiante")
        print("2. Ver estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Ingrese su elección (1-5): ")

        if opcion == '1':
            in_estudiante()
        elif opcion == '2':
            sel_estudiante()
        elif opcion == '3':
            ed_estudiante()
        elif opcion == '4':
            el_student()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está mal con tu nombre de usuario o contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
