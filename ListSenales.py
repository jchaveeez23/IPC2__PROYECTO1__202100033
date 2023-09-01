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

                #print("Leyendo senal...", attributes["nombre"], attributes["t"], attributes["A"])
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
                    attributes["nombre"],
                    int(attributes["t"]),
                    int(attributes["A"]),
                    listDatos,
                )
                self.insert(senal)
                self.index += 1
            return True
        except:
            return False
        

    def analizarSenales(self):
        temp = self.head
        while temp != None:
            print("Analizando senal: ", temp.dato.getNombre())
            sleep(1)
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