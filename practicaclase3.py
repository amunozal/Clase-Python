import sqlite3
conexion=sqlite3.connect("bd2.db")
try:    
    conexion.execute("""create table articulos(codigo integer primary key AUTOINCREMENT, description text,precio real)""")
    print("se crea tabla")
except sqlite3.OperationalError:
    print("Ya existe")
 
desc=(input("Agregue la descripcion del articulo = \n"))
price=int(input("Agregue el precio del articulo = \n"))
conexion.execute("insert into articulos(description, precio )values(?,?)",(desc,price))
conexion.commit()
 
curso=conexion.execute("select codigo,description,precio from articulos")
for fila in curso:
    print(fila)
conexion.close()

