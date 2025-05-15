
#%%
# Creating a class in Python

class Pajaro:
    pass 

mi_pajaro = Pajaro()
otro_pajaro = Pajaro()

print(mi_pajaro)   # <__main__.Pajaro object at 0x7f8c1c2e3d90>
print(otro_pajaro) # <__main__.Pajaro object at 0x7f8c1c2e3d90>
print(type(mi_pajaro)) # <class '__main__.Pajaro'>


# %%
# Attributes:

class Pajaro: # this is the class definition
    
    # calss attributes
    alas = True # this is a class atribute, it is shared by all instances of the class
    
    def __init__(self,color, especie): # init parameters 
        self.color = color # color of the bird this is an instance attribute
        self.especie = especie
        
mi_pajaro = Pajaro("rojo", "canario") # this is an instance of the class Pajaro

print(mi_pajaro.color)
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)
        


# %%

# Methods:

class Pajaro: # this is the class
    
    # calss attributes
    alas = True
    
    def __init__(self,color, especie): # init parameters
        self.color = color # instance attribute
        self.especie = especie # instance attribute
    
    # this is an instance method <---
    def piar(self): 
        print(f"pio, mi color es {self.color}")
    
    # The instance method can call other instance methods
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        self.piar()
    
    # the instance method can change the instance atributes
    def cambiar_color(self):
        self.color = 'Negro'
        print(f"Ahora el pajaro es {self.color}")
        
    # class methods <---
    # This method does not need an instance to run 
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
    
    # Static method <---
    # This method helps us to set attributes that cannot be modified 
    @staticmethod
    def mirar():
        print("EL pajaro mira")
    
    
        
piolin = Pajaro("amarillo", "canario") # this is an instance of the class Pajaro
# piolin.piar() # this is how to call a method of the class Pajaro
# piolin.volar(10) # this is how to call a method of the class Pajaro
# piolin.cambiar_color()

#  We can change the class attributes as  follows
piolin.alas = False
print(piolin.alas)
Pajaro.poner_huevos(3)

# %%

