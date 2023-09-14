def suma(m,n):
    return m+n

def resta(m,n):
    return m-n

def mul(m,n):
    return m*n

def div(m,n):
    try:
        return m/n
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return("Error")

while(True):  # Captura de excepciones con un bucle infinito
    try:
        m=(int(input("Introduce el primer número:")))
        n=(int(input("Introduce el segundo número:")))
        break
    except ValueError:
        print("Error")

operacion=input("Introduce la operacion(+,-,*,/):")

if operacion=="+":
    print(suma(m,n))
elif operacion=="-":
    print(resta(m,n))
elif operacion=="*":
    print(mul(m,n))
elif operacion=="/":
    print(div(m,n))
else:
    print("Operación inexistente")

# El programa sigue funcionando...