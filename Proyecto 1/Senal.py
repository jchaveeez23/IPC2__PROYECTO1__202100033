from ListDatos import ListDatos
from Dato import Dato
from Patron import Patron
from Tupla import Tupla
from time import sleep
import os
import subprocess

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
        sleep(0.5)
        listTupla = ListDatos()
        temp = self.patrones.head

        while temp != None:
            patron = listTupla.searchPatron(temp.dato.getPatron())
            if patron == None:
                nuevosDato = ListDatos()
                temp2 = temp.dato.datos.head
                while temp2 != None:
                    nuevosDato.insert(
                        Dato(
                            temp2.dato.getNombre(),
                            temp2.dato.getTiempo(),
                            temp2.dato.getAmplitud(),
                        )
                    )
                    temp2 = temp2.next

                tupla = Tupla(self.amplitud, temp.dato.getPatron(), nuevosDato)
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

    def generarGraficas(self):
        print("Generando de señales ingresadas...")
        sleep(0.5)
        self.generarGraficaDatos()
        input("Presione enter para continuar...")
        sleep(0.5)
        self.generarGraficaTuplas()

    def generarGraficaDatos(self):
        print("Generando grafica de datos...")
        dot = f"graph {self.getNombre()} {{\n"
        dot += f"node [color=black];\n"
        dot += f"nn00;\n"
        dot += f'nn00 [label = "{self.getNombre()}";];\n'
        dot += f'nnt [label = "t={self.getTiempo()}";];\n'
        dot += f'nna [label = "A={self.getAmplitud()}";];\n'
        dot += f"nn00 -- nnt;\n"
        dot += f"nn00 -- nna;\n"

        temp = self.patrones.head
        position = "nn00"
        while temp != None:
            temp2 = temp.dato.datos.head
            while temp2 != None:
                if temp.dato.getTiempo() > 1:
                    position = (
                        "nn"
                        + str(temp.dato.getTiempo() - 1)
                        + str(temp2.dato.getAmplitud())
                    )

                nodePosition = (
                    "nn" + str(temp.dato.getTiempo()) + str(temp2.dato.getAmplitud())
                )

                dot += f"{position} -- {nodePosition};\n"
                dot += f'{nodePosition} [label = "{temp2.dato.getNombre()}";];\n'
                temp2 = temp2.next
            temp = temp.next

        dot += f"}}\n"

        self.generarDot(str(self.getNombre()) + "datos", dot)

    def generarGraficaTuplas(self):
        print("Generando grafica de tuplas...")
        dot = f"graph {self.getNombre()} {{\n"
        dot += f"node [color=black];\n"
        dot += f"nn00;\n"
        dot += f'nn00 [label = "{self.getNombre()} reducida";];\n'
        dot += f'nna [label = "A={self.getAmplitud()}";];\n'
        dot += f"nn00 -- nna;\n"

        temp = self.tuplas.head
        position = "nn00"
        tiempo = 1
        while temp != None:
            temp2 = temp.dato.tiempos.head
            tiempos = ""
            while temp2 != None:
                tiempos += str(temp2.dato) + ","
                temp2 = temp2.next
            tiempos = tiempos[:-1]

            if tiempo > 1:
                position = "gt" + str(tiempo - 1)

            dot += f'gt{tiempo} [label = "g={tiempo}(t={tiempos})";];\n'
            dot += f"{position} -- gt{tiempo};\n"

            position = "nn00"
            temp2 = temp.dato.datos.head
            while temp2 != None:
                if tiempo > 1:
                    position = "nn" + str(tiempo - 1) + str(temp2.dato.getAmplitud())

                nodePosition = "nn" + str(tiempo) + str(temp2.dato.getAmplitud())

                dot += f"{position} -- {nodePosition};\n"
                dot += f'{nodePosition} [label = "{temp2.dato.getNombre()}";];\n'
                temp2 = temp2.next
            tiempo += 1
            temp = temp.next

        dot += f"}}\n"

        self.generarDot(str(self.getNombre()) + "reducida", dot)

    def generarDot(self, nombre, dot):
        with open(f"graphs/{nombre}.dot", "w") as f:
            f.write(dot)

        command = f"dot -Tpng graphs/{nombre}.dot -o graphs/{nombre}.png"
        
        os.system(command)

        file = f"graphs/{nombre}.png"
        command = None

        if os.name == 'posix':
            command = f"xdg-open {file}"
        elif os.name == 'nt':
            command = f"start {file}"
        else:
            print("No se pudo abrir la gráfica...")
            return
        
        if command:
            subprocess.Popen(command, shell=True)

        print("Gráfica generada...")
