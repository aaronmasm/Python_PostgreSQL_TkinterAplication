-- Creamos la tabla students
CREATE TABLE students(id Serial, name  text, address text, age int);

-- Insertamos dos datos de prueba
INSERT INTO students(name, address, age) VALUES
    ('Ryan', 'San Francisco', 23);
INSERT INTO students(name, address, age) VALUES
    ('Joe', 'Los Angeles', 30);

-- Consultamos la tabla students para ver su contenido
SELECT * from students;