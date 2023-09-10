lista = ["gato", "perro", "elefante", "delfín"]

print(lista)
print(lista[:])
# Son equivalentes estas dos formas de mostrar la lista

print(lista[0])  # Imprime el primero
print(lista[-1])  # Imprime el último

print(lista[0:3])
print(lista[:3])
# Imprime los 3 primeros

print(lista[2:])
# Imprime los 2 últimos

lista.append("macaco")
print(lista)
# Añade un macaco al final

lista.insert(2, "vaca")
print(lista)
# Añade una vaca en la posición 2

lista.extend(["rinoceronte", "oso"])
print(lista)
# Añade un rinoceronte y un oso

print(lista.index("elefante"))
# Devuelve el índice del elefante

print("oso" in lista)
# Devuelve True si hay un oso en la lista

mixto = [5, "gato", 7.3, False]
print(mixto)
# Lista de valores mixtos

mixto.remove(5)
print(mixto)
# Elimina el 5

mixto.pop()
print(mixto)
# Elimina el último elemento

print(lista+mixto)
print(lista*3)
