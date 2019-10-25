#!/usr/bin/env python
# coding: utf-8

# cada vez que ceramos un objeto de esa clase, la identificacion del constructor es la primera en ejecutarse
# la forma de inicializar el valor de un atributo de clase son constructor

# class three:
#         val=7
# #Constructor __init__(self)

# tambien podemos hacer esto dentro de las funciones de clase:

# In[16]:


class three:
        def func(self,val):
            self.val=val
t=three()
t.func(8)
t.val


# In[18]:


t.func(6) #Tambien nos permite reinicializar atributos
t.val


# In[23]:


#o podemos pedirle informacion al usuario.

class three:
    def __init__(self):
        self.val=input("What value?")
t=three()


# In[24]:


t.val


# creacion de objetos
#  _new__ es un metodo de clase estatica nos permite controlar la creacion de objetos 
# cada vez que hacemos una llamada al constructor de la clase, realiza una llamada a __new__
# si bien esta es una funcion predeterminada para cada clase, definitivamente podemos jugar con ella

# In[34]:


class demo:
        def __new__(self):
                return 'dataflair'
d=demo()
type(d)


# Tambien podemos crear un nuevo atributo exclusivamente para este objeto y leerlo al definir valores
# no hay mucho que pueda hacer una vez que ya haya definido el objeto

# In[33]:


kumquat.color='orange'
print("i am",kumquat.color)


# Entonces,que sucede cuando no proporcionamos explicitamente un constructor para una clase?
# puede PYTHON manejarlo? por que no lo intentamos?

# In[38]:


class color:
    def show(self):
        print("You can see me"
orange=color()
orange.show()


# In[39]:


Un constructor que Python nos presta cuando olvidamos incluir uno.
Este


# In[52]:


class itspower:
    def __init__(self,x):
        self.x=x
    def __pow__(self,other):
        return self.x**other.x
a=itspower(2)
b=itspower(10)
a**b


# In[53]:


def factorial(n):
    f=1
    while n>0:
        f*=n
        n-=1
    print(f)
factorial(4)


# In[56]:


def factorial(numero):
    print ("Valor inicial ->",numero)
    if numero > 1:
        numero = numero * factorial(numero -1)
    print ("valor final ->",numero)
.    return numero
p.rint (factorial(5))


# In[ ]:




