import agregar1
import eliminar1

nombres=[]
while True:
    agregar=(input("1 = Desea agregar un estudiante \n2 = Desea eliminar un estudiante \n3 = Salir \n"))
    if agregar == '1':
        agregar1.agregar(nombres)
    elif agregar == '2':
        eliminar1.eliminar(nombres)
    elif agregar == '3':
        break
print(nombres)