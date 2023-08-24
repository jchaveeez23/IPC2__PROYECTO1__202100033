import xml.etree.ElementTree as ET
from graphviz import Digraph
import os
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nuevo_nodo

    def existe(self, nombre):
        current = self.head
        while current:
            if current.nombre == nombre:
                return True
            current = current.next
        return False

    def obtener(self, index):
        current = self.head
        for x in range(index):
            current = current.next
        return current.nombre
    
    def tamano(self):
        current = self.head
        contador = 0
        while current:
            contador+=1
            current = current.next
        return contador
    
    def imprimir(self):
        current = self.head
        while current:
            print(current.nombre)
            current = current.next

class Senal:
    def __init__(self, nombre, t, A):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.matriz = self.Matriz()

    class Matriz:
        def __init__(self):
            self.filas = ListaEnlazada()

        def agregar_fila(self, nfila, ncol):
            if not self.filas.head:
                self.filas.agregar(nfila)
            else:
                if not self.filas.existe(nfila):
                    self.filas.agregar(nfila)

        def agregar_columna(self, nfila, ncol):
            current = self.filas.head
            while current:
                if current.nombre == nfila:
                    if not current.next:
                        current.next = ListaEnlazada()
                        current.next.agregar(ncol)
                    else:
                        if not current.next.existe(ncol):
                            current.next.agregar(ncol)
                current = current.next

        def imprimir(self):
            current = self.filas.head
            while current:
                print(current.nombre)
                current.next.imprimir()
                current = current.next

        def existe_fila(self, nfila):
            current = self.filas.head
            while current:
                if current.nombre == nfila:
                    return True
                current = current.next
            return False

        def existe_columna(self, nfila, ncol):
            current = self.filas.head
            while current:
                if current.nombre == nfila:
                    return current.next.existe(ncol)
                current = current.next
            return False

        def obtener(self, nfila, ncol):
            current = self.filas.head
            while current:
                if current.nombre == nfila:
                    return current.next.obtener(ncol)
                current = current.next
            return None

        def tamano(self):
            current = self.filas.head
            contador = 0
            while current:
                contador += 1
                current = current.next
            return contador
        
        def imprimir(self):
            current = self.filas.head
            while current:
                print(current.nombre)
                current.next.imprimir()
                current = current.next

class ListaMatriz:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo

    def encontrar(self, dato):
        actual = self.cabeza
        index = 0
        while actual:
            if actual.dato.iguales(dato):
                return index
            actual = actual.next
            index += 1
        return -1

    def obtener(self, index):
        actual = self.cabeza
        for x in range(index):
            actual = actual.next
        return actual.dato

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.next
        return contador
    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato.nombre)
            actual = actual.next

class Matriz:
    def __init__(self):
        self.filas = ListaMatriz()

    def agregar_fila(self, nfila, ncol):
        if not self.filas.cabeza:
            self.filas.cabeza = Nodo([0] * self.A)

        actual = self.filas.cabeza
        while actual:
            if actual.dato[0] == nfila:
                actual.dato[ncol] = 1
                break
            actual = actual.next

    def agregar_columna(self, nfila, ncol):
        if not self.filas.cabeza:
            self.filas.cabeza = Nodo([0] * self.A)

        actual = self.filas.cabeza
        while actual:
            if actual.dato[0] == nfila:
                actual.dato[ncol] = 1
                break
            actual = actual.next

    def imprimir(self):
        actual = self.filas.cabeza
        while actual:
            print(actual.dato)
            actual = actual.next

    def existe_fila(self, nfila):
        actual = self.filas.cabeza
        while actual:
            if actual.dato[0] == nfila:
                return True
            actual = actual.next
        return False
    
    def existe_columna(self, nfila, ncol):
        actual = self.filas.cabeza
        while actual:
            if actual.dato[0] == nfila:
                return actual.dato[ncol] == 1
            actual = actual.next
        return False
    
    def obtener(self, nfila, ncol):
        actual = self.filas.cabeza
        while actual:
            if actual.dato[0] == nfila:
                return actual.dato[ncol]
            actual = actual.next
        return None
    
    def tamano(self):
        actual = self.filas.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.next
        return contador
    
    def imprimir(self):
        actual = self.filas.cabeza
        while actual:
            print(actual.dato)
            actual = actual.next

def cargar_archivo(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()
    senales = ListaMatriz()
    for senal in root:
        nombre = senal.attrib['nombre']
        t = int(senal.attrib['t'])
        A = int(senal.attrib['A'])
        senales.agregar(Senal(nombre, t, A))
    return senales

def procesar_archivo(senales):
    for senal in senales:
        for fila in senal.matriz.filas:
            for col in fila:
                senal.matriz.agregar_fila(fila, col)
                senal.matriz.agregar_columna(fila, col)
    return senales

def escribir_archivo(senales):
    #Escribir un archivo xml con las señales procesadas

    #Crear el archivo xml
    archivo = open('salida.xml', 'w')
    archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    archivo.write('<data>\n')
    for senal in senales:
        archivo.write('\t<senal nombre="'+senal.nombre+'" t="'+str(senal.t)+'" A="'+str(senal.A)+'">\n')
        for fila in senal.matriz.filas:
            for col in fila:
                archivo.write('\t\t<dato t="'+str(fila)+'" A="'+str(col)+'"/>\n')
        archivo.write('\t</senal>\n')
    archivo.write('</data>')
    archivo.close()

def mostrar_datos():
    print('Josue Daniel Chavez Portillo')
    print('202100033')
    print('Introduccion a la programacion y computacion 2 seccion "C"')
    print('Ingenieria en ciencias y sistemas')
    print('6to Semestre :(')

def generar_grafica(senales):
    #Generar una grafica con graphviz
    dot = Digraph(comment='Grafica de Señales')
    for senal in senales:
        dot.node(senal.nombre, senal.nombre)
    for senal in senales:
        for fila in senal.matriz.filas:
            for col in fila:
                if senal.matriz.obtener(fila, col) == 1:
                    dot.edge(fila, col)
    dot.render('grafica.gv', view=True)



    

def reiniciar():
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


def main():
    Lista = ListaMatriz()
    senales = ListaMatriz()

    op = 0
    while op != 7:
        print('---------------------------------------')
        print("MENU PRINCIPAL")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Inicializar Sistema")
        print("7. Salir")
        print('---------------------------------------')
        print("Elija una opcion de 1 a 7:")
        op = int(input())
        if op == 1:
            # CARGA DE ARCHIVOS
            print('----------------CARGA DE ARCHIVOS---------------')
            archivo = input('Ingrese la ruta del archivo XML: ')
            cargar_archivo(archivo)
            print('Archivo Cargado exitosamente...')
            input()
        elif op  == 2:
            # PROCESAMIENTO DEL ARCHIVO
            print('------------------PROCESAMIENTO-----------------')
            if not senales.cabeza:
                print('No hay datos para procesar.')
                input()
                continue
            procesar_archivo(senales)
            print('Señales procesadas con exito...')
            input()
        elif op == 3:
            # SALIDA DE DATOS EN UN ARCHIVO
            print('-------------------SALIDA----------------------')
            if not senales:
                print('No hay datos para escribir.')
                input()
                continue
            escribir_archivo(senales)
            print('Archivo de salida creado con exito...')
            input()
        elif op == 4:
            # MOSTRAR INFORMACION DEL ESTUDIANTE
            mostrar_datos()
            input()
        elif op == 5:
            # GRAFICA GENERADA
            print('-------------------GRAFICA----------------------')
            if not senales:
                print('No hay datos para graficar.')
                input()
                continue
            generar_grafica(senales)
            input()
        elif op == 6:
            # REINICIO DEL PROGRAMA
            print('> Reiniciando el sistema...')
            print('> Sistema Reiniciado...')
            reiniciar()
            input()
        elif op == 7:
            # Salir
            print('Hasta la proxima...')
            input()
            break

if __name__ == "__main__":
    main()
    








