from Nodo import Nodo
from Dato import Dato


class ListDatos:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, cell):
        new = Nodo(cell) 

        if self.head == None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def searchDatoAmplitud(self, amplitud):
        temp = self.head
        while temp != None:
            if temp.dato.getAmplitud() == amplitud:
                return temp.dato
            temp = temp.next
        return None

    def searchDato(self, tiempo, amplitud):
        temp = self.head
        while temp != None:
            if temp.dato.getTiempo() == tiempo and temp.dato.getAmplitud() == amplitud:
                return temp.dato
            temp = temp.next
        return None
    
    def searchPatron(self, patron):
        temp = self.head
        while temp != None:
            if temp.dato.getPatron() == patron:
                return temp.dato
            temp = temp.next
        return None
    
    def showDatos(self):
        temp = self.head
        while temp != None:
            print("Tiempo: ", temp.dato.getTiempo(), "Amplitud: ", temp.dato.getAmplitud(), "Nombre", temp.dato.getNombre())
            temp = temp.next

    def showTuplas(self):
        temp = self.head
        while temp != None:
            print("Patron: ", temp.dato.getPatron(), "Amplitud: ", temp.dato.getAmplitud(), "Patron: ", temp.dato.getPatron())
            temp.dato.getDatos().showDatos()
            temp.dato.showTiempos()
            temp = temp.next

    def showPatrones(self):
        temp = self.head
        while temp != None:
            print("Tiempo: ", temp.dato.getTiempo(), "Patron: ", temp.dato.getPatron(), "Datos: ", temp.dato.getDatos())
            temp = temp.next
