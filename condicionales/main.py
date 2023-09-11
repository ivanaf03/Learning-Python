def notas(nota):
    if nota < 5:
        valoracion = "suspenso"
    elif nota < 9:
        valoracion = "aprobado"
    elif nota > 10:
        valoracion = "matrícula"
    else:
        valoracion = "errónea"
    return valoracion


num = input("Dime tu nota :)\n")
print(notas(int(num)))
