
# %%
class Animal:
    
    # Instance attributes
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self): #<--- Instance method 
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    
    # Here we add instance atrributes to an inherited class
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    
    # Extended inheritance
    # In this case we modify a previously written method
    def hablar(self):
        print("pio")
    
    # We added an extra method that did not exist in the animal class.
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")


piolin = Pajaro(3, "Amarillo",60)
mi_animal = Animal(5,'Negro')

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

# %% 

class Padre:
    def hablar(self): # instance method
        print("hola")
        

class Madre:
    def reir(self): # instance method
        print("jajaja")
    
    def hablar(self): # instance method
        print('Que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass



mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()


# %%

# Practical exercises 
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass


#%%
class Vertebrado:
    
    vertebrado = True  # class attribues

class Ave(Vertebrado):
    
    tiene_pico = True       # class attribues
    def poner_huevos(self): # instance method 
        print("Poniendo huevos")

class Reptil(Vertebrado):
    
    venenoso = True  # class attribues

class Pez(Vertebrado):
    
    def nadar(self): # instance method 
        print("Nadando")
    
    def poner_huevos(self): # instance method 
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    
    def caminar(self): # instance method 
        print("Caminando")
    
    def amamantar(self): # instance method 
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass

#%%
class Padre():
    
    color_ojos = "marrón"    # class attribues
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    
    def reir(self): # instance method 
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
    
