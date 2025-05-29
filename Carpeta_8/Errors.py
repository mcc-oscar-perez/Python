#%%

def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1+n2)
    print("Gracias por sumar" +n1)
    


try:
    #Code we want to test
    suma()
    
except TypeError:
    #Code to execute if there is an error 
    print("Estas haciendo mal una concatenacion")
    
except ValueError:
    print("Ese no es un numero")
    
else:
    #Code to execute if there is no error
    print("Hiciste todo bien")

finally:
    #Code that is going to be executed anyway
    print("Eso fue todo")
    
#%%

def pedir_numero():
    
    while True:
        try: 
            numero = int(input("Dame un numero"))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresa el numero {numero}")
            break
    print("Gracias")
    
    

pedir_numero()
    
# %%
#Practical ecercises 