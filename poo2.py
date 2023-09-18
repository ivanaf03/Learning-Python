class Coche():

    def __init__(self):  # Contructor de clase
        self.__largo=250 # Encapsulación, atributos privados
        self.__ancho=120
        self.__ruedas=4  
        self.__enmovimiento=False

    def arrancar(self, arrancada):
        self.enmovimiento=arrancada
        
    def estado(self):
        print("El largo del coche es:", self.__largo)
        print("El anrcho del coche es:", self.__ancho)
        print("El coche tiene ", self.__ruedas, " ruedas")
        if self.__enmovimiento:
            print("El coche está en movimiento")
        else:
            print("El coche no está en movimiento")

miCoche=Coche()
miCoche2=Coche()
miCoche.arrancar(True)
miCoche.estado()
miCoche2.estado()
