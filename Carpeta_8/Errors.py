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

# 1
def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")

# 2

def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
        
# 3 

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

