cantidad=int(input("Cuantos estudiantes desea agregar = "))
nombres=[]
i=0
while i<cantidad:
    nombre=input('Digite el nombre : ')
    nombres.append(nombre)
    i += 1
print(nombres)