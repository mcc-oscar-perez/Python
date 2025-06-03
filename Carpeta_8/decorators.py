"""Here we put into practice how to use decorators"""

def cambiar_letras(tipo):
    """This function allows us to choise what type of action we want to do, upper or lwer"""
    def mayusculas(texto):
        print(texto.upper())
    def minusculas(texto):
        print(texto.lower())
    if tipo == "may":
        return mayusculas
    if tipo == "min":
        return minusculas
operacion = cambiar_letras("may")

operacion("palabra")

#%%
"""We create a decorator function"""

def decorar_saludo(funcion):
    """This function decorates another function"""
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion        
@decorar_saludo
def mayusculas(texto):
    """This function changes letters to uppercase"""
    print(texto.upper())
@decorar_saludo
def minusculas(texto):
    """This function changes letters to lowecase"""
    print(texto.lower())
minusculas("Python")

# %%
"""Another way to do it"""

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion        

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())
    
mayusculas_decorada = decorar_saludo(mayusculas)
minusculas_decorada = decorar_saludo(minusculas)

mayusculas("kevin")
mayusculas_decorada("kevin")
print("")
minusculas("KEVIN")
minusculas_decorada("KEVIN")

# %%
