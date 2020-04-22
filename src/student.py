from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

# Inicializando el GUI y colocando el título a la ventana
root = Tk()
root.title("Python & PostgreSQL")


# Creamos la función que tomará los inputs de la función anónima lambda y los enviará a la db.
# También nos conectaremos a la db mediante el objeto conn y sus parámetros;
# cabe resaltar, que psycopg2 sirve para conectarnos a PostgreSQL
def save_new_student(name, age, address):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="A300785masm",
        host="localhost",
        port="5432"
    )

    # Creamos el cursor para la consulta SQL
    cursor = conn.cursor()

    # Creamos la consulta(query) SQL
    query = '''INSERT INTO students(name, age, address) VALUES (%s, %s, %s)'''

    # Ejecuta la consulta SQL
    cursor.execute(query, (name, age, address))

    # Enviamos un mensaje a la consola
    print("Data Saved!")

    # Guardamos (commit) los cambios
    conn.commit()

    # Cerramos la consulta
    conn.close()

    # Actualizamos la aplicación con las nuevas entradas
    display_students()


# Listamos los datos de los estudiantes
def display_students():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="A300785masm",
        host="localhost",
        port="5432"
    )

    # Creamos el cursor para la consulta SQL
    cursor = conn.cursor()

    # Creamos la consulta(query) SQL
    query = '''SELECT * FROM students'''

    # Ejecuta la consulta SQL
    cursor.execute(query)

    # Retornamos una lista con los datos que tenemos en la DB
    row = cursor.fetchall()

    # Colocamos los elementos en un contenedor mediante Listbox
    listbox = Listbox(frame, width=20, height=10)

    # Posición del Listbox
    listbox.grid(row=10, columnspan=4, sticky=W + E)

    # Insertamos los datos mediante un ciclo for, NOTA IMPORTANTE:
    # La constante "END" no hace nada, sirve para ingresar un elemento
    # inmediatamente después del ultimo
    for x in row:
        listbox.insert(END, x)

    # Guardamos (commit) los cambios
    conn.commit()

    # Cerramos la consulta
    conn.close()


# Definimos la función Buscar (Search)
def search(id):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="A300785masm",
        host="localhost",
        port="5432"
    )

    # Creamos el cursor para la consulta SQL
    cursor = conn.cursor()

    # Creamos la consulta(query) SQL
    query = '''SELECT * FROM students WHERE id=%s'''

    # Ejecuta la consulta SQL
    cursor.execute(query, (id))

    # Retornamos una lista con los datos que tenemos en la DB
    row = cursor.fetchone()

    # Llamamos a la función de la fila que hemos encontrado
    display_search_result(row)

    # Guardamos (commit) los cambios
    conn.commit()

    # Cerramos la consulta
    conn.close()


# Función para mostrar el resultado en el frame
def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W + E)
    listbox.insert(END, row)


# Configuramos el Canvas del GUI
canvas = Canvas(root, height=380, width=400)
canvas.pack()

# Configurando el Frame para los espaciados
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Colocamos los Labels y los Inputs
# Título del formulario
label = Label(frame, text="Add a Student")  # Texto del Label
label.grid(row=0, column=1)  # Posición del Label

# Name Input
label = Label(frame, text="Name: ")
label.grid(row=1, column=0)

# Colocamos las entradas de textos
entry_name = Entry(frame)  # Entrada en el Frame
entry_name.grid(row=1, column=1)  # Posición del Entry

# Age Input
label = Label(frame, text="Age: ")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address Input
label = Label(frame, text="Address: ")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

# Colocamos el Botón “Registered” que tomará la información de los inputs mediante la función get()
# la función command  enviará los get() a la función anónima lambda save_new_student() para que puedan
# enviarse a la DB. Ver la función save_new_student() a partir de la linea 9
button = Button(frame, text="Registered", command=lambda: save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
))

# Posición del Button
button.grid(row=4, column=1, sticky=W + E)

# Búsquedas
label = Label(frame, text="Search Data")
label.grid(row=5, column=1)

label = Label(frame, text="Search by Id")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

# Llamamos a la función display_students()
display_students()

# Corremos la aplicación con un mainloop()
root.mainloop()
