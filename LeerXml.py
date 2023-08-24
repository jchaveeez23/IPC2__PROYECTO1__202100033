'''Leer un archivo de entrada xml'''
import xml.etree.ElementTree as ET
from graphviz import Digraph
import os
'''Utilizando listas dinamicas almacenar los datos de las señales de un archivo xml'''
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
        self.matriz = self.Matriz()

    class Matriz:
        def __init__(self):
            self.filas = ListaMatriz()

        def agregar_fila(self,nfila,ncol):
            if not self.filas.cabeza:
                self.filas.agregar(ncol)
            else:
                actual = self.filas.cabeza
                while actual.next:
                    actual = actual.next
                actual.next = Nodo(ncol)

        def agregar_dato(self,fila,col,valor):
            actual = self.filas.cabeza
            for x in range(fila):
                actual = actual.next
            actual.dato.matriz[fila][col] = valor

    def agregar_dato(self,fila,col,valor):
        self.matriz.agregar_dato(fila,col,valor)

    def agregar_fila(self,nfila,ncol):
        self.matriz.agregar_fila(nfila,ncol)

    def iguales(self,senal):
        if self.nombre == senal.nombre:
            return True
        return False
    
    def imprimir(self):
        print(self.nombre)
        print(self.t)
        print(self.A)
        actual = self.matriz.filas.cabeza
        while actual:
            print(actual.dato.matriz)
            actual = actual.next

'''Leer un archivo de entrada xml'''
def leerxml(nombre):
    tree = ET.parse(nombre)
    root = tree.getroot()
    senales = ListaMatriz()
    for senal in root:
        nombre = senal.attrib['nombre']
        t = int(senal.attrib['t'])
        A = int(senal.attrib['A'])
        nueva_senal = Senal(nombre,t,A)
        for datos in senal:
            fila = int(datos.attrib['t'])
            columna = int(datos.attrib['A'])
            valor = int(datos.attrib['valor'])
            nueva_senal.agregar_fila(t,A)
            nueva_senal.agregar_dato(fila,columna,valor)
        senales.agregar(nueva_senal)
    print(senales)   
    return senales
    

archivo = input('Ingrese el nombre del archivo: ')






