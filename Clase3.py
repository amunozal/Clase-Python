import sqlite3
conexion=sqlite3.connect("bd.db")
try:    
    #crear una tabla en la base de datos creada
    conexion.execute("""create table articulos(codigo integer primary key AUTOINCREMENT, description text,precio real)""")
    print("se crea tabla")
except sqlite3.OperationalError:
    print("Ya existe")
#agregar datos en la base de datos 
conexion.execute("insert into articulos(description, precio )values(?,?)",("naranja",20))
conexion.commit()
#mostrar datos de la base de datos 
curso=conexion.execute("select codigo,description,precio from articulos")
for fila in curso:
    print(fila)
conexion.close()

#SQL base de datos nativa de python
#Nativa se refiere a que no se necesita mucho para que se comuniquen entre si
#import sqlite3 --> Base de datos 
#conexion=sqlite3.connect("bd.db")
#conexio es la variable
#sqlite3 es el motor / connect es para conectar / ("bd.db") nombre de la base de datos /
#conexion.execute("""create table articulos(codigo integer primary key AUTOINCREMENT, description text,precio real)""")
#crea la tabla dentro de la base de datos

#try - para que se siga ejecutando auque haya un error
#except - cuando hay un error se refleja el except

