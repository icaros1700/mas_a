def mas_a (C1, C2, C3, C4):
    letra = 'a'
    cadena_mas = C1
    cantidad_mas = C1.lower().count(letra)

    if C2.lower().count(letra) > cantidad_mas:
        cadena_mas = C2
    elif C3.lower().count(letra) > cantidad_mas:
        cadena_mas = C3
    elif C4.lower().count(letra) > cantidad_mas:
        cadena_mas = C4
        cantidad_mas = C4.lower().count(letra)
    
    return cadena_mas

gab = mas_a("arroz", "arjona", "antonamatona", "antilope")
print("La palabra que tiene mas a es: ", gab)