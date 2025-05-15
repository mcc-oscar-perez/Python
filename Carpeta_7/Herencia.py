
# %%
class Animal:
    
    # Instance attributes
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self): #<--- Instance method 
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass



piolin = Pajaro(2, "Amarillo")
print(piolin.color)
piolin.nacer()


# This way we can check if our class inherits something and vice versa 
print(Pajaro.__bases__)
print(Animal.__subclasses__())

# %%
# Practical exercises:

class Persona:#<--- Class
    
    def __init__(self, nombre,edad): #<--- Instance attribute
        self.edad = edad
        self.nombre = nombre
    
class Alumno(Persona):#<---inheritance
    pass

class Mascota: #<---Class
    
    def __init__(self, edad, nombre,cantidad_patas):#<---Instance attribute
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):#<---inheritance
    pass


class Vehiculo: #<--- class
    
    def acelerar(slef): #<--- Instance method
        pass
    
    def frenar(self): #<--- Instance method
        pass
    
class Automovil(Vehiculo): #<--- Inheretance
    pass
    