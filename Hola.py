producto=input("Producto")
precio=float(input("Precio"))
IVA=float(input("Porcentaje Impuesto"))
total=(precio*IVA)+precio
print(producto,total)