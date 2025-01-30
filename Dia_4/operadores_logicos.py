# AND
mi_bool = 4 < 5 and 5 < 6
print(mi_bool)

# OR
mi_bool2 = (4 < 5) or (5 > 6)
print(mi_bool2)

#ejemplo practico
texto = "Este texto es solo para probar"
mi_bool3 = ("texto" in texto) and ("PROBAR".lower() in texto)
print(mi_bool3)

#ejemlo practico 2
mi_bool4 = not (4 < 5)
print(mi_bool4)