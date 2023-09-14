def generador(*ciudades):  # El * sirve para aceptar varios parámetros en una función
    for i in ciudades:
        for j in i:
            yield j

def generador2(*ciudades):  # Hace lo mismo pero con yield from es más simple
    for i in ciudades:
        yield from i


ciudades_devueltas=generador("Lugo", "Ourense", "Pontevedra")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

ciudades_devueltas=generador2("Lugo", "Ourense", "Pontevedra")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))