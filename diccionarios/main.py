diccionario = {"Espanha": "Madrid", "Bulgaria": "Sofía", "México": "Ciudad de México"}

print(diccionario["Espanha"])  # Devuelve el valor que tiene esa clave

diccionario["Rusia"] = "Lima"  # Esto es falso, pero lo podremos sobreescribir

print(diccionario["Rusia"])

diccionario["Rusia"] = "Moscú"

print(diccionario["Rusia"])

del diccionario["Espanha"]

print(diccionario)

# Podemos hacer un diccionario con tuplas
tupla = ["Perú", "Argentina"]

diccionario2 = {tupla[0]: "Lima", tupla[1]: "Buenos Aires"}

print(diccionario2)

print(diccionario2.keys())  # Devuelve las claves

print(diccionario2.values())  # Devuelve los valores
