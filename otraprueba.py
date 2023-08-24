import os
import xml.etree.ElementTree as ET
from graphviz import Digraph

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None

class ListaMatriz:
    def __init__(self):
        self.cabeza = None
        
    def agregar(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def encontrar(self,dato):
        actual = self.cabeza
        index = 0
        while actual:
            if actual.dato.iguales(dato):
                return index
            actual = actual.next
            index +=1
        return -1
    
    def obtener(self,index):
        actual = self.cabeza
        for x in range(index):
            actual = actual.next
        return actual.dato
    
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador+=1
            actual = actual.next
        return contador
    
class Senal:
    def __init__(self,nombre,t,A):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.matriz = [[0]*A for x in range(t)]

    def agregar_dato(self,fila,col,valor):
        self.matriz[fila][col] = valor

class Senalreducida:
    def __init__(self,nombre,A):
        self.nombre = nombre
        self.A = A
        self.grupos = ListaMatriz()

    def agregar_grupo(self,grupo):
        self.grupos.agregar(grupo)

class Patron:
    def __init__(self,datos):
        self.datos = datos

    def iguales(self,patron):
        return self.datos == patron.datos
    
    


def Cargar_Archivo(nombrearchivo):
    senales = []
    tree = ET.parse(nombrearchivo)
    root = tree.getroot()
    for senal_elem in root.findall('./senales/senal'):
        nombre = senal_elem.get('nombre')
        t = int(senal_elem.get('t'))
        A = int(senal_elem.get('A'))
        senal = Senal(nombre,t,A)
        for dato_elem in senal_elem.findall('/dato'):
            fila = int(dato_elem.get('t'))
            col = int(dato_elem.get('A'))
            valor = float(dato_elem.text)
            senal.matriz[fila][col] = valor
        senales.append(senal)
    print(senales)
    return senales

def Procesar_Archivo(senales):
    senales_reducidas = []
    for senal in senales:
        senal_reducida = Senalreducida(senal.nombre,senal.A)
        for fila in senal.matriz:
            patron = Patron(fila)
            index = senal_reducida.grupos.encontrar(patron)
            if index == -1:
                senal_reducida.agregar_grupo(patron)
        senales_reducidas.append(senal_reducida)
    return senales_reducidas

def Escribir_Archivo(senales_reducidas):
    archivo = open('salida.txt','w')
    for senal_reducida in senales_reducidas:
        archivo.write(senal_reducida.nombre+'\n')
        for grupo in senal_reducida.grupos:
            for dato in grupo:
                archivo.write(str(dato)+' ')
            archivo.write('\n')
        archivo.write('\n')
    archivo.close()

def Generar_Grafica(senales_reducidas):
    dot = Digraph(comment='Grafica de la señal')
    dot.node('A', 'Nombre: '+senal_reducida.nombre)
    dot.node('B', 'A: '+senal_reducida.A)
    dot.edges(['AB'])
    dot.render('test-output/round-table.gv', view=True)



def mostrar_datos():
    print('Josue Daniel Chavez Portillo')
    print('202100033')
    print('Introduccion a la programacion y computacion 2 seccion "C"')
    print('Ingenieria en ciencias y sistemas')
    print('6to Semestre :(')

def reiniciar():
    os.system('cls' if os.name == 'nt' else 'clear')
    Menu()

def Menu():
    senales = None
    senales_reducidas = None
    while True:
        print('1. Cargar Archivo')
        print('2. Procesar Archivo')
        print('3. Escribir Archivo de Salida')
        print('4. Mostrar Datos del Estudiante')
        print('4. Generar Gráfica')
        print('6. Reiniciar Sistema')
        print('7. Salir')
        opcion = input('Ingrese una opción: ')
        if opcion == '1':
            nombrearchivo = input('Ingrese el nombre del archivo: ')
            senales = Cargar_Archivo(nombrearchivo)
        elif opcion == '2':
            senales_reducidas = Procesar_Archivo(senales)
        elif opcion == '3':
            Escribir_Archivo(senales_reducidas)
        elif opcion == '4':
            mostrar_datos()
        elif opcion == '5':
            Generar_Grafica(senales_reducidas)
        elif opcion == '6':
            reiniciar()
        elif opcion == '7':
            break
        else:
            print('Opción inválida')

Menu()


