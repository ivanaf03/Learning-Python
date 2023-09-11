import math

for i in [1, 2, 3]:
    print("El elemento de la lista es", i, end=" ")
# end sirve para evitar saltos de línea, por ejemplo


print("\n")
for i in "buenos días":
    print(i, end="")

print("\n")
verify = False
mail = input("Dime tu email:\n")
for i in mail:
    if i == "@":
        verify = True

if verify:
    print("Email válido")
else:
    print("Email inválido")

print("\n")
for i in range(5):
    print(f"iteración {i}")
# La f sirve para opciones de formato, por ejemplo, que la i si va entre llaves sea una variable. Nos evita,
# por ejemplo, usar operadores de concatenación

for i in range(10, 50, 5):
    print(i)
# Imprime los números del 10 (incluído) al 50 (sin incluírlo) de 5 en 5


print("Raíces infinitas")
while 1:
    num = int(input("Introduce un número:\n"))
    if num < 0:
        print("Inválido")
    else:
        print("La raíz de ", num, "es ", math.sqrt(num))
