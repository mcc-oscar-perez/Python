# serie = "N-02"

# match serie:
#     case "N-01":
#         print("Samsung")
#     case "N-02":
#         print("Nokia")
#     case "N-03":
#         print("Motorola")
#     case _:
#         print("No match")

cliente = {"nombre": "federico",
            "edad": 45, 
            "ocupacion": "instrutor"}  

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reeves",
                                "director": "Lana Wachowski",}}

elemento = [cliente,pelicula,"libro"]

for e in elemento:
    match e:
        case {"nombre": nombre, "edad":edad, "ocupacion": ocupacion}:
            print("Cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director}}:
            print("Pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No match")