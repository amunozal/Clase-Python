#Cree un software con dos bases de datos, la primera con el nombre empleados y la segunda transacciones
#en la base de datos empleados, cree dos tabla con los nombres
#1) empleados y 2)Horarios. en la tabla 
#en la tabla empleados cree 3 casillas
#1) nombre, 2)cedula y 3) puesto
#en la base de datos trasnsacciones , cree 3 tablas 
# 1 Inevtario. 2 efectivo y 3 activos
#con las casillas en inventario: 1 entrada, 2 salida y 3 saldo 
#solicitele al usuario ingresar los datos de un nuevo empleado o ver los empleados que ya hay.

import sqlite3
conexion1=sqlite3.connect("empleados.db")
conexion2=sqlite3.connect("transacciones.db")
try:    
    conexion1.execute("""create table empleados(cedula integer primary key, nombre text,puesto text)""")
    conexion1.execute("""create table horarios""")
    conexion2.execute("""create table inventario(codigo integer primary key AUTOINCREMENT, entrada text,salida text,saldo real)""")
    conexion2.execute("""create table efectivo""")
    conexion2.execute("""create table activos""")
    print("se crea tabla")
except sqlite3.OperationalError:
    print("Ya existen")

while True:
    opcion=int(input("Que desea hacer \n 1-Agregar empleado \n 2-Ver empleado \n 3-Salir \n"))
    if opcion == 1:
        ced=(input("Agregue la cedula del empleado = \n"))
        name=(input("Agregue el nombre del empleado = \n"))
        pos=(input("Agregue el puesto del empleado = \n"))
        conexion1.execute("insert into empleados(cedula, nombre, puesto)values(?,?,?)",(ced,name,pos))
        conexion1.commit()
    elif opcion == 2:
        curso1=conexion1.execute("select cedula,nombre,puesto from empleados")
        for fila in curso1:
            print(fila)
    elif opcion == 3:
        break
conexion1.close()
conexion2.close()