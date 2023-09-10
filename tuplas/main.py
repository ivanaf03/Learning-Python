tupla = ("azul", "rojo", 1, 1, 2, 3)

print(tupla[0])

lista = list(tupla)  # Convierte la tupla en una lista

tupla2 = tuple(lista)  # Convierte la lista en tupla

print("azul" in tupla)  # Devuelve un boolean verificando si el elemento está en la tupla

print(tupla.count(1))  # Cuenta cuantas veces aparece el '1' en la tupla

print(len(tupla))  # Cuenta la cantidad de elementos de la tupla

tuplaunitaria = ("Hola",)  # Necesaria la coma

# En las tuplas los paréntesis no son necesarios
tupla3 = "Joel", "5", "5", "1999"

nombre, dia, mes, anho = tupla3  # Esto se llama desempaquetado de tuplas

print(tupla3)