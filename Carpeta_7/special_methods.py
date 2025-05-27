#%% 

class CD:
    
    def __init__(self, autor, titulo, canciones):
        self.autor = autor # instance attributes
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self): # special method 
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__(self): # special method 
        return self.canciones
    
    def __del__(Self):
        print("Se ha eliminado el cd")
    

mi_cd = CD('Pink floyd','The wall',24) # this is an instance of the class CD

print(mi_cd)
print(len(mi_cd))
del mi_cd

# %%

# Practical excerices 
# 1 
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
    
# 2  
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

# 3 
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")