from time import sleep
import xml.etree.ElementTree as ET
from ListDatos import ListDatos

from Nodo import Nodo
from Senal import Senal
from Dato import Dato


class ListSenales:
    def __init__(self):
        self.head = None
        self.last = None
        self.index = 1

    def insert(self, senal):
        new = Nodo(senal)

        if self.head == None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.index += 1

    def leerArchivo(self, path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()

            for nodo in root.findall("senal"):
                attributes = nodo.attrib
                listDatos = ListDatos()
                tiempo = int(attributes["t"])
                amplitud = int(attributes["A"])
                nombre = attributes["nombre"]
                if tiempo > 0 and tiempo <= 3600:
                    if amplitud > 0 and amplitud <= 130:
                        for nodoDato in nodo.findall("dato"):
                            attributesDato = nodoDato.attrib
                            cell = Dato(
                                int(nodoDato.text),
                                int(attributesDato["t"]),
                                int(attributesDato["A"]),
                            )
                            #print("Dato: ", nodoDato.text, "A: ", attributesDato["A"], "t: ", attributesDato["t"])
                            listDatos.insert(cell)

                        senal = Senal(
                            self.index,
                            nombre,
                            tiempo,
                            amplitud,
                            listDatos,
                        )
                        self.insert(senal)
                        self.index += 1
                    else:
                        print(f'Error: Señal={nombre}, Amplitud "{amplitud}" fuera de rango')
                else:
                    print(f'Error: Señal={nombre}, Tiempo "{tiempo}" fuera de rango')

            return True
        except:
            return False
        
    def searchSenal(self, nombre):
        temp = self.head
        while temp != None:
            if temp.dato.getNombre() == nombre:
                return temp.dato
            temp = temp.next
        return None

    def analizarSenales(self):
        temp = self.head
        while temp != None:
            print("Analizando senal: ", temp.dato.getNombre())
            sleep(0.5)
            temp.dato.analizar()
            temp = temp.next

    def escribirArchivo(self, path):
        print("Escribiendo archivo..." + path)
        xml_data = '<?xml version="1.0"?>\n'
        xml_data = xml_data + "<senalesReducidas>\n"
        
        temp = self.head
        while temp != None:
            xml_data = xml_data + temp.dato.getXML()
            temp = temp.next

        xml_data = xml_data + "</senalesReducidas>"

        with open(path, "w") as f:
            f.write(xml_data)
        print("Archivo escrito...")
        sleep(1)

    def generarGraficas(self):
        print("Generando gráficas...")
        nombre = input("Ingrese el nombre de la señal: ")
        senal = self.searchSenal(nombre)
        sleep(1)
        if senal != None:
            senal.generarGraficas()
        else:
            print("Señal no encontrada...")