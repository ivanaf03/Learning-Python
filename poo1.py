class Coche():

    largo=250
    ancho=120
    ruedas=4
    enmovimiento=False

    def arrancar(self):
        self.enmovimiento=True

    def comprobarMovimiento(self):
        if self.enmovimiento:
            return "si"
        else:
            return "no"

miCoche=Coche()
print("El largo del coche es:", miCoche.largo)
print("El anrcho del coche es:", miCoche.ancho)
print("El coche está en movimiento?", miCoche.comprobarMovimiento())
miCoche.arrancar()
print("El coche está en movimiento?", miCoche.comprobarMovimiento())