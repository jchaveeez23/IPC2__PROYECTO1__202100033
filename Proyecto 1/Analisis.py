class Analisis:
    def __init__(self,index, nombre, tiempo, amplitud, patron, datos):
        self.index = index
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.patron = patron
        self.analisis = None
        self.datos = datos

    def getIndex(self):
        return self.index
    
    def getNombre(self):
        return self.nombre
    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def getPatron(self):
        return self.patron
    
    def setIndex(self, index):
        self.index = index

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setAmplitud(self, amplitud):
        self.amplitud = amplitud

    def setPatron(self, patron):
        self.patron = patron