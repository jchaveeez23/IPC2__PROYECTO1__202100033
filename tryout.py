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
                for x in range(nfila):
                    self.filas.agregar(ListaMatriz())
            else:
                for x in range(nfila-self.filas.tamano()):
                    self.filas.agregar(ListaMatriz())
            actual = self.filas.cabeza
            for x in range(nfila):
                actual.dato.agregar(ncol)
                actual = actual.next

        def agregar(self,fila,columna,dato):
            self.filas.obtener(fila).agregar(dato)

        def obtener(self,fila,columna):
            return self.filas.obtener(fila).obtener(columna)

        def tamano(self):
            return self.filas.tamano()

        def imprimir(self):
            actual = self.filas.cabeza
            while actual:
                actual.dato.imprimir()
                actual = actual.next

    def iguales(self,senal):
        if self.nombre == senal.nombre:
            return True
        return False

    def imprimir(self):
        print('Nombre: ',self.nombre)
        print('T: ',self.t)
        print('A: ',self.A)
        print('Matriz: ')
        self.matriz.imprimir()

    def graficar(self):
        dot = Digraph(comment='Grafica de la señal')
        dot.node('A', 'Nombre: '+self.nombre)
        dot.node('B', 'T: '+self.t)
        dot.node('C', 'A: '+self.A)
        dot.edges(['AB','BC'])
        dot.render('test-output/round-table.gv', view=True)

senales = ListaMatriz()

def cargar_archivo(archivo):
    global senales
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        for senal in root:
            nombre = senal.attrib['nombre']
            t = senal.attrib['t']
            A = senal.attrib['A']
            nueva_senal = Senal(nombre,t,A)
            for fila in senal:
                nueva_senal.matriz.agregar_fila(int(fila.attrib['n']),int(fila.attrib['m']))
                for dato in fila:
                    nueva_senal.matriz.agregar(int(fila.attrib['n']),int(dato.attrib['n']),int(dato.text))
            senales.agregar(nueva_senal)
    except:
        print('Error al cargar el archivo...')
        input()
        return
    
'''Utilizando listas dinamicas convertir las señales en señales binarias, si su valores son mayores a 0 se convierten en 1 de lo contrario seguiran siendo 0'''
def procesar_archivo(senales):
    actual = senales.cabeza
    while actual:
        senal = actual.dato
        for fila_m, fila in enumerate(senal.matriz.filas):
            for columna_m, columna in enumerate(fila.dato):
                if columna > 0:
                    senal.matriz.agregar(fila_m,columna_m,1)
        actual = actual.next

'''Utilizando listas dinamicas encontrar las filas de la matriz binaria que tengan el mismo patron y agruparlas'''
def agrupar_patrones(senales):
    actual = senales.cabeza
    while actual:
        senal = actual.dato
        senalreducida = Senalreducida(senal.nombre,senal.A)
        patrones = ListaMatriz()
        for fila_m, fila in enumerate(senal.matriz.filas):
            patron = Patron(fila)
            patron_m = patrones.encontrar(patron)

            if patron_m == -1:
                patrones.agregar(patron)
                patron_m = patrones.tamano()-1

            patron_dato = patrones.obtener(patron_m)
            patron_dato.agregar_fila(fila_m,0)
        actual = actual.next

'''Utilizando listas dinamicas los grupos hechos anteriormente, sumar cada uno de los valores de las filas y columnas de la matriz sin procesar'''
def sumar_filas_columnas(senales):
    actual = senales.cabeza
    while actual:
        senal = actual.dato
        senalreducida = Senalreducida(senal.nombre,senal.A)
        for fila_m, fila in enumerate(senal.matriz.filas):
            for columna_m, columna in enumerate(fila.dato):
                if columna > 0:
                    senal.matriz.agregar(fila_m,columna_m,1)
        actual = actual.next







def mostrar_datos():
    print('Josue Daniel Chavez Portillo')
    print('202100033')
    print('Introduccion a la programacion y computacion 2 seccion "C"')
    print('Ingenieria en ciencias y sistemas')
    print('6to Semestre :(')

    

def reiniciar():
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


def main():
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
    








