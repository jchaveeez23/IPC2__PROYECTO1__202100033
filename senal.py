from ListDatos import ListDatos
from Dato import Dato
from Patron import Patron
from Tupla import Tupla
from time import sleep

class Senal:
    def __init__(self, index, nombre, tiempo, amplitud, datos):
        self.index = index
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.datos = datos
        self.patrones = None
        self.tuplas = None

    def analizar(self):
        listDatos = ListDatos()
        listPatrones = ListDatos()
        print("Recorriendo datos...")
        print("Calculando la matriz binaria...")
        sleep(1)
        patron = ""
        for i in range(1, self.tiempo + 1):
            patron = ""
            listDatos = ListDatos()
            for x in range(1, self.amplitud + 1):
                binario = 0
                nombre = 0
                buscar = self.datos.searchDato(i, x)
                if buscar:
                    binario = buscar.getBinario()
                    nombre = buscar.getNombre()

                listDatos.insert(Dato(nombre, i, x))
                patron = patron + str(binario) + ","
            listPatrones.insert(Patron(i, patron, listDatos))
        self.patrones = listPatrones
        print("Realizando suma de tuplas...")
        sleep(1)
        listTupla = ListDatos()
        temp = self.patrones.head

        while temp != None:
            patron = listTupla.searchPatron(temp.dato.getPatron())
            if patron == None:
                tupla = Tupla(
                    self.amplitud, temp.dato.getPatron(), temp.dato.getDatos()
                )
                tupla.setTiempo(temp.dato.getTiempo())
                listTupla.insert(tupla)
            else:
                patron.sumaDatos(temp.dato.getDatos())
                patron.setTiempo(temp.dato.getTiempo())

            temp = temp.next

        self.tuplas = listTupla
        print("Analisis finalizado...")
        listTupla.showTuplas()

        return True

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

    def getXML(self):
        index = 1
        xml = f'   <senal nombre="{self.nombre}" A="{self.amplitud}">\n'
        temp = self.tuplas.head
        while temp != None:
            xml += f'        <grupo g="{str(index)}">\n'
            xml += f"            <tiempos>"
            temp2 = temp.dato.tiempos.head
            tiempos = ""
            while temp2 != None:
                tiempos += str(temp2.dato) + ","
                temp2 = temp2.next
            xml += tiempos[:-1]
            xml += "</tiempos>\n"

            xml += f"            <datosGrupos>\n"
            temp2 = temp.dato.datos.head
            while temp2 != None:
                xml += f'                <dato A="{str(temp2.dato.getAmplitud())}">{str(temp2.dato.getAmplitud())}</dato>\n'
                temp2 = temp2.next
            xml += f"            </datosGrupos>\n"
            xml += f"        </grupo>\n"
            temp = temp.next
            index += 1
        xml += "    </senal>\n"
        return xml
