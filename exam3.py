import sqlite3
conexion1=sqlite3.connect("personas.db")

try:    
    conexion1.execute("""create table personas(cedula integer primary key, nombre text)""")
    print("se crea tabla")
except sqlite3.OperationalError:
    print("Ya existen")
    
while True:
    opcion=int(input("Que desea hacer \n 1-Agregar Nombre \n 2-Ver Nombre \n 3-Salir \n"))
    if opcion == 1:
        ced=(input("Agregue la cedula del Nombre = \n"))
        name=(input("Agregue el nombre del Nombre = \n"))
        conexion1.execute("insert into personas(cedula, nombre)values(?,?)",(ced,name))
        conexion1.commit()
    elif opcion == 2:
        curso1=conexion1.execute("select cedula,nombre from personas")
        for fila in curso1:
            print(fila)
    elif opcion == 3:
        break
conexion1.close()