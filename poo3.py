class Coche():

    def __init__(self):  # Contructor de clase
        self.__largo=250 # Encapsulación, atributos privados
        self.__ancho=120
        self.__ruedas=4  
        self.__enmovimiento=False

    def arrancar(self, arrancada):
        self.__enmovimiento=arrancada
        
    def estado(self):
        print("El largo del coche es:", self.__largo)
        print("El anrcho del coche es:", self.__ancho)
        print("El coche tiene ", self.__ruedas, " ruedas")
        if self.__enmovimiento and self.__comprobacion(True, True, True):
            print("El coche está en movimiento")
        else:
            print("El coche no está en movimiento")

    def __comprobacion(self, gasolina, aceite, puertasCerradas):  # Método privado encapsulado
        if gasolina and aceite and puertasCerradas:
            return True
        else:
            return False

miCoche=Coche()
miCoche2=Coche()
miCoche.arrancar(True)
miCoche.estado()
miCoche2.estado()