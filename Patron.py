class Patron:
    def __init__(self, tiempo, patron, datos):
        self.tiempo = tiempo
        self.patron = patron
        self.datos = datos

    def getTiempo(self):
        return self.tiempo
    
    def getPatron(self):
        return self.patron
    
    def getDatos(self):
        return self.datos
    
    def showDatos(self):
        temp = self.datos.head
        while temp != None:
            print("Tiempo: ", temp.dato.getTiempo(), "Amplitud: ", temp.dato.getAmplitud())
            temp = temp.next