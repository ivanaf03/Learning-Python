def division():
    try:
        m=(float(input("Introduce el primer número:")))
        n=(float(input("Introduce el segundo número:")))
        print(f"{m} / {n} = {m/n}")
    except ValueError:
        print("Valor erróneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    finally:  # Se ejecuta cuando no se dan excepciones
        print("División exitosa")

division()