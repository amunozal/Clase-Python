opcion=int(input("Que desea hacer \n 1-Agregar \n 2-Salir \n"))
lista=[]
while True:
    if opcion == 1:
        producto=input("Producto = ")
        precio=int(input("Precio = "))
        lista.append(producto)
        lista.append(precio)
    elif opcion == 2:
        break
print(lista)