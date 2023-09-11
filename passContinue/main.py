for letra in "buenos dias":
    if letra == "s":
        continue  # Vuelve al inicio del bucle
    print(letra, end="")

print("\n")
nombre = "Iván Álvarez Fernández"
contador = 0
for i in nombre:
    if i == " ":
        continue  # Vuelve al inicio del bucle
    contador += 1
print(contador)

print("\n")
email = input("Dime tu email:\n")
for i in email:
    if i == "@":
        arroba = True
        break
else:  # Se ejecuta SOLO si el bucle realiza todas sus iteraciones
    arroba = False
print("¿El correo tiene arroba?", arroba)


while True:
    pass  # Se utiliza cuando quieres dejar un fragmento de código vacío para programar en el futuro
