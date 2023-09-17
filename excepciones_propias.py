import math

def evaluaEdad(edad):
    if edad<0:
        raise ValueError("No se permiten edades negativas")
    if edad<20:
        return "tas chikito"
    elif edad<40:
        return "te haces mayor"
    else:
        return "estás muriendo"

def calculaRaiz(num):
    if num<0:
        raise ValueError("No se puede calcular una raíz de un negativo")
    else:
        return math.sqrt(num)
try:
    print(calculaRaiz(-10))
except ValueError as numerosNegativos:
    print(numerosNegativos)

try:
    print(evaluaEdad(-19))
except ValueError as numerosNegativos:
    print(numerosNegativos)
