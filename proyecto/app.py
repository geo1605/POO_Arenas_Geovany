
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Escuela"
)
cursor = conn.cursor()

# Clase Estudiante
class Estudiante:
    @staticmethod
    @app.route('/estudiantes')
    def estudiantes():
        cursor.execute("SELECT * FROM Estudiantes")
        estudiantes = cursor.fetchall()
        return render_template('estudiantes.html', estudiantes=estudiantes)

    @staticmethod
    @app.route('/agregar_estudiante', methods=['POST'])
    def agregar_estudiante():
        nombre = request.form['nombre']
        edad = request.form['edad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        grado = request.form['grado']
        curso_id = request.form['curso_id']

        cursor.execute("""
            INSERT INTO Estudiantes (nombre, edad, fecha_nacimiento, grado, curso_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, edad, fecha_nacimiento, grado, curso_id))
        conn.commit()
        return redirect(url_for('estudiantes'))

    @staticmethod
    @app.route('/eliminar_estudiante/<int:id>', methods=['POST'])
    def eliminar_estudiante(id):
        cursor.execute("DELETE FROM Estudiantes WHERE estudiante_id = %s", (id,))
        conn.commit()
        return redirect(url_for('estudiantes'))

    @staticmethod
    @app.route('/editar_estudiante/<int:id>', methods=['GET', 'POST'])
    def editar_estudiante(id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            edad = request.form['edad']
            fecha_nacimiento = request.form['fecha_nacimiento']
            grado = request.form['grado']
            curso_id = request.form['curso_id']

            cursor.execute("""
                UPDATE Estudiantes
                SET nombre = %s, edad = %s, fecha_nacimiento = %s, grado = %s, curso_id = %s
                WHERE estudiante_id = %s
            """, (nombre, edad, fecha_nacimiento, grado, curso_id, id))
            conn.commit()
            return redirect(url_for('estudiantes'))
        else:
            cursor.execute("SELECT * FROM Estudiantes WHERE estudiante_id = %s", (id,))
            estudiante = cursor.fetchone()
            return render_template('editar_estudiante.html', estudiante=estudiante)

# Clase Profesor
class Profesor:
    @staticmethod
    @app.route('/profesores')
    def profesores():
        cursor.execute("SELECT * FROM Profesores")
        profesores = cursor.fetchall()
        return render_template('profesores.html', profesores=profesores)

    @staticmethod
    @app.route('/agregar_profesor', methods=['POST'])
    def agregar_profesor():
        nombre = request.form['nombre']
        edad = request.form['edad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        departamento = request.form['departamento']
        salario = request.form['salario']

        cursor.execute("""
            INSERT INTO Profesores (nombre, edad, fecha_nacimiento, departamento, salario)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, edad, fecha_nacimiento, departamento, salario))
        conn.commit()
        return redirect(url_for('profesores'))

    @staticmethod
    @app.route('/eliminar_profesor/<int:id>', methods=['POST'])
    def eliminar_profesor(id):
        cursor.execute("DELETE FROM Profesores WHERE profesor_id = %s", (id,))
        conn.commit()
        return redirect(url_for('profesores'))

    @staticmethod
    @app.route('/editar_profesor/<int:id>', methods=['GET', 'POST'])
    def editar_profesor(id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            edad = request.form['edad']
            fecha_nacimiento = request.form['fecha_nacimiento']
            departamento = request.form['departamento']
            salario = request.form['salario']

            cursor.execute("""
                UPDATE Profesores
                SET nombre = %s, edad = %s, fecha_nacimiento = %s, departamento = %s, salario = %s
                WHERE profesor_id = %s
            """, (nombre, edad, fecha_nacimiento, departamento, salario, id))
            conn.commit()
            return redirect(url_for('profesores'))
        else:
            cursor.execute("SELECT * FROM Profesores WHERE profesor_id = %s", (id,))
            profesor = cursor.fetchone()
            return render_template('editar_profesor.html', profesor=profesor)

# Clase Curso
class Curso:
    @staticmethod
    @app.route('/cursos')
    def cursos():
        cursor.execute("SELECT * FROM Cursos")
        cursos = cursor.fetchall()
        return render_template('cursos.html', cursos=cursos)

    @staticmethod
    @app.route('/agregar_curso', methods=['POST'])
    def agregar_curso():
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        creditos = request.form['creditos']
        profesor_id = request.form['profesor_id']

        cursor.execute("""
            INSERT INTO Cursos (nombre, descripcion, creditos, profesor_id)
            VALUES (%s, %s, %s, %s)
        """, (nombre, descripcion, creditos, profesor_id))
        conn.commit()
        return redirect(url_for('cursos'))

    @staticmethod
    @app.route('/eliminar_curso/<int:id>', methods=['POST'])
    def eliminar_curso(id):
        cursor.execute("DELETE FROM Cursos WHERE curso_id = %s", (id,))
        conn.commit()
        return redirect(url_for('cursos'))

    @staticmethod
    @app.route('/editar_curso/<int:id>', methods=['GET', 'POST'])
    def editar_curso(id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            creditos = request.form['creditos']
            profesor_id = request.form['profesor_id']

            cursor.execute("""
                UPDATE Cursos
                SET nombre = %s, descripcion = %s, creditos = %s, profesor_id = %s
                WHERE curso_id = %s
            """, (nombre, descripcion, creditos, profesor_id, id))
            conn.commit()
            return redirect(url_for('cursos'))
        else:
            cursor.execute("SELECT * FROM Cursos WHERE curso_id = %s", (id,))
            curso = cursor.fetchone()
            return render_template('editar_curso.html', curso=curso)


# --- Asistencia ---
class Asistencia:
    @staticmethod
    @app.route('/asistencia')
    def asistencia():
        cursor.execute("SELECT * FROM Asistencia")
        asistencias = cursor.fetchall()  # Cambiado a 'asistencias'
        return render_template('asistencia.html', asistencias=asistencias)  # Usar 'asistencias'  # Usar 'asistencias'

    @staticmethod
    @app.route('/agregar_asistencia', methods=['POST'])
    def agregar_asistencia():
            fecha = request.form['fecha']
            estado = request.form['estado']
            estudiante_id = request.form['estudiante_id']
            curso_id = request.form['curso_id']

            cursor.execute("""
                INSERT INTO Asistencia (fecha, estado, estudiante_id, curso_id)
                VALUES (%s, %s, %s, %s)
            """, (fecha, estado, estudiante_id, curso_id))
            conn.commit()
            return redirect(url_for('asistencia'))



    @staticmethod
    @app.route('/editar_asistencia/<int:id>', methods=['GET', 'POST'])
    def editar_asistencia(id):
        if request.method == 'POST':
            fecha = request.form['fecha']
            estado = request.form['estado']
            estudiante_id = request.form['estudiante_id']
            curso_id = request.form['curso_id']

            cursor.execute("""
                UPDATE Asistencia
                SET fecha = %s, estado = %s, estudiante_id = %s, curso_id = %s
                WHERE asistencia_id = %s
            """, (fecha, estado, estudiante_id, curso_id, id))
            conn.commit()
            return redirect(url_for('asistencia'))
        else:
            cursor.execute("SELECT * FROM Asistencia WHERE asistencia_id = %s", (id,))
            asistencia = cursor.fetchone()
            return render_template('editar_asistencia.html', asistencia=asistencia)

    @staticmethod
    @app.route('/eliminar_asistencia/<int:id>', methods=['POST'])
    def eliminar_asistencia(id):
        cursor.execute("DELETE FROM Asistencia WHERE asistencia_id = %s", (id,))
        conn.commit()
        return redirect(url_for('asistencia'))
    
    @app.route('/asistencia_estudiante_curso/<int:estudiante_id>/<int:curso_id>')
    def asistencia_estudiante_curso(estudiante_id, curso_id):
        cursor.execute("""
            SELECT A.fecha, A.estado
            FROM Asistencia A
            WHERE A.estudiante_id = %s AND A.curso_id = %s
        """, (estudiante_id, curso_id))
        asistencias = cursor.fetchall()
        return render_template('asistencia_estudiante_curso.html', asistencias=asistencias)



# --- Director de Carrera ---
class DirectorCarrera:
    @staticmethod
    @app.route('/carrera')
    def carrera():
        cursor.execute("SELECT * FROM DirectoresCarrera")
        directores = cursor.fetchall()
        return render_template('carrera.html', directores=directores)

    @staticmethod
    @app.route('/agregar_director', methods=['POST'])  # Cambiado a '/agregar_director'
    def agregar_director():
        nombre = request.form['nombre']
        edad = request.form['edad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        departamento = request.form['departamento']
        telefono = request.form['telefono']
        email = request.form['email']
        salario = request.form['salario']

        cursor.execute("""
            INSERT INTO DirectoresCarrera (nombre, edad, fecha_nacimiento, departamento, telefono, email, salario)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, edad, fecha_nacimiento, departamento, telefono, email, salario))
        conn.commit()
        return redirect(url_for('carrera'))
    

    @staticmethod
    @app.route('/editar_carrera/<int:id>', methods=['GET', 'POST'])
    def editar_carrera(id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            edad = request.form['edad']
            fecha_nacimiento = request.form['fecha_nacimiento']
            departamento = request.form['departamento']
            telefono = request.form['telefono']
            email = request.form['email']
            salario = request.form['salario']

            cursor.execute("""
                UPDATE DirectoresCarrera
                SET nombre = %s, edad = %s, fecha_nacimiento = %s, departamento = %s, telefono = %s, email = %s, salario = %s
                WHERE director_id = %s
            """, (nombre, edad, fecha_nacimiento, departamento, telefono, email, salario, id))
            conn.commit()
            return redirect(url_for('carrera'))
        else:
            cursor.execute("SELECT * FROM DirectoresCarrera WHERE director_id = %s", (id,))
            director = cursor.fetchone()
            return render_template('editar_carrera.html', director=director)

    @staticmethod
    @app.route('/eliminar_carrera/<int:id>', methods=['POST'])
    def eliminar_carrera(id):
        cursor.execute("DELETE FROM DirectoresCarrera WHERE director_id = %s", (id,))
        conn.commit()
        return redirect(url_for('carrera'))
    
    
# Clase Calificaciones
class Calificacion:
    @staticmethod
    @app.route('/calificaciones')
    def calificaciones():
        cursor.execute("SELECT * FROM Calificaciones")
        calificaciones = cursor.fetchall()
        return render_template('calificaciones.html', calificaciones=calificaciones)

    @staticmethod
    @app.route('/agregar_calificacion', methods=['POST'])
    def agregar_calificacion():
        estudiante_id = request.form['estudiante_id']
        curso_id = request.form['curso_id']
        calificacion = request.form['calificacion']
        fecha = request.form['fecha']

        cursor.execute("""
            INSERT INTO Calificaciones (estudiante_id, curso_id, calificacion, fecha)
            VALUES (%s, %s, %s, %s)
        """, (estudiante_id, curso_id, calificacion, fecha))
        conn.commit()
        return redirect(url_for('calificaciones'))

    @staticmethod
    @app.route('/eliminar_calificacion/<int:id>', methods=['POST'])
    def eliminar_calificacion(id):
        cursor.execute("DELETE FROM Calificaciones WHERE calificacion_id = %s", (id,))
        conn.commit()
        return redirect(url_for('calificaciones'))

    @staticmethod
    @app.route('/editar_calificacion/<int:id>', methods=['GET', 'POST'])
    def editar_calificacion(id):
        if request.method == 'POST':
            estudiante_id = request.form['estudiante_id']
            curso_id = request.form['curso_id']
            calificacion = request.form['calificacion']
            fecha = request.form['fecha']

            cursor.execute("""
                UPDATE Calificaciones
                SET estudiante_id = %s, curso_id = %s, calificacion = %s, fecha = %s
                WHERE calificacion_id = %s
            """, (estudiante_id, curso_id, calificacion, fecha, id))
            conn.commit()
            return redirect(url_for('calificaciones'))
        else:
            cursor.execute("SELECT * FROM Calificaciones WHERE calificacion_id = %s", (id,))
            calificacion = cursor.fetchone()
            return render_template('editar_calificacion.html', calificacion=calificacion)
    @app.route('/calificaciones_estudiante/<int:estudiante_id>')
    def calificaciones_estudiante(estudiante_id):
        cursor.execute("""
            SELECT C.nombre, Ca.calificacion, Ca.fecha
            FROM Calificaciones Ca
            JOIN Cursos C ON Ca.curso_id = C.curso_id
            WHERE Ca.estudiante_id = %s
        """, (estudiante_id,))
        calificaciones = cursor.fetchall()
        return render_template('calificaciones_estudiante.html', calificaciones=calificaciones)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
