# Funciones con Kwargs
# Functions with kwargs

def suma(**kwargs):
    
    Total = 0 
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor} ")
        Total += valor
    return Total
        
print(suma(x=3 , y=5 , z=2))


def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}")
    for x,y in kwargs.items():
        print(f"{x}: {y}")

print(describir_persona("María", color_ojos="azules", color_pelo="rubio"))