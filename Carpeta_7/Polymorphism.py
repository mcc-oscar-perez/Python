#%%
class Vaca:
    
    def __init__(self, nombre): # Instance attributes 
        self.nombre =  nombre
        
    def hablar(self):           # Instance Method 
        print(self.nombre + "dice muuu")
        
class Oveja: 
    
    def __init__(self, nombre): # Instance attributes 
        self.nombre =  nombre
        
    def hablar(self):           # Instance Method 
        print(self.nombre + "dice beee")
        

vaca1 = Vaca("Aurora")
Oveja1 = Oveja("Nube")

def animal_habla(animal):
    animal.hablar()
    
animal_habla(vaca1)

# %%
# Practical exercises 

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))
    
#%%

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
gandalf = Mago()     # instance 
hawkeye = Arquero()  # instance 
jack = Samurai()     # instance 

personajes = [hawkeye, gandalf, jack]

for personaje in personajes:
    personaje.atacar()

#%%

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()

# %%
