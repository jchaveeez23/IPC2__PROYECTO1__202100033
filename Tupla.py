from ListDatos import ListDatos

class Tupla:
    def __init__(self, amplitud, patron, datos):
        self.tiempos = ListDatos()
        self.amplitud = amplitud
        self.patron = patron
        self.datos = datos

    def getGrupo(self):
        return self.grupo
    
    def getTiempos(self):
        return self.tiempos
    
    def getAmplitud(self):
        return self.amplitud
    
    def getPatron(self):
        return self.patron
    
    def getDatos(self):
        return self.datos

    def setTiempo(self, tiempo):
        self.tiempos.insert(tiempo)

    def showTiempos(self):
        temp = self.tiempos.head
        while temp != None:
            print("Tiempo - grupo: ", temp.dato)
            temp = temp.next

    def sumaDatos(self, datos):
        patron = ""
        for i in range(1, self.amplitud + 1):
            tuplaDato = self.datos.searchDatoAmplitud(i)
            dato = datos.searchDatoAmplitud(i)
            tuplaDato.setNombre(tuplaDato.getNombre() + dato.getNombre())
            patron = patron + str(tuplaDato.getNombre()) + ","