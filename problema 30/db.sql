CREATE DATABASE escu;

USE escu;

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    grado VARCHAR(10),
    email VARCHAR(100)
);

INSERT INTO estudiantes (nombre, edad, grado, email) VALUES
('Juan Pérez', 15, '10', 'juan.perez@escuela.com'),
('María García', 14, '9', 'maria.garcia@escuela.com'),
('Carlos Sánchez', 16, '11', 'carlos.sanchez@escuela.com'),
('Ana Rodríguez', 17, '12', 'ana.rodriguez@escuela.com'),
('Luis Fernández', 15, '10', 'luis.fernandez@escuela.com');

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion VARCHAR(255)
);

INSERT INTO cursos (nombre, descripcion) VALUES
('Matemáticas', 'Curso de matemáticas avanzado'),
('Historia', 'Curso de historia mundial'),
('Ciencias', 'Curso de ciencias naturales'),
('Inglés', 'Curso de inglés intermedio'),
('Computación', 'Curso de computación básica');

CREATE TABLE inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO inscripciones (id_estudiante, id_curso) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);
