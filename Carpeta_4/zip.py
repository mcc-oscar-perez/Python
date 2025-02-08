nombres = ['Ana', 'Carlos', 'Beatriz', 'David']
edades = [23, 45, 34, 32]  
ciudades = ['Madrid', 'Barcelona', 'Bilbao', 'Valencia']

combinados = zip(nombres, edades, ciudades)  


for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
    
    
