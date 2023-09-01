class Dato:
    def __init__(self, nombre, tiempo, amplitud):
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud

    def getBinario(self):
        if int(self.nombre) > 0:
            binario = 1
        else:
            binario = 0

        return binario

    def getNombre(self):
        return int(self.nombre)
    
    def getTiempo(self):
        return int(self.tiempo)
    
    def getAmplitud(self):
        return int(self.amplitud)
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setAmplitud(self, amplitud):
        self.amplitud = amplitud
    