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
class senal:
    def __init__(self,nombre,t,A):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.matriz = self.Matriz()

    class Matriz:
        def __init__(self):
            self.filas = ListaMatriz()

        def agregar_fila(self,fila):
            self.filas.agregar(fila)
    




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
        input()
    elif op  == 2:
        # PROCESAMIENTO DEL ARCHIVO
        print('------------------PROCESAMIENTO-----------------')
        input()
    elif op == 3:
        # SALIDA DE DATOS EN UN ARCHIVO
        print('-------------------SALIDA----------------------')
        input()
    elif op == 4:
        # MOSTRAR INFORMACION DEL ESTUDIANTE
        print('> Josue Daniel Chavez Portillo')
        print('> 202100033')
        print('> Introduccion a la programacion y computacion 2 seccion "C"')
        print('> Ingenieria en ciencias y sistemas')
        print('> 6to Semestre :(')
        input()
    elif op == 5:
        # GRAFICA GENERADA
        print('> Elija la grafica que desea ver')
        print('> 1. Señales Emitidas')
        print('> 2. Señales Reducidas')
        input()
    elif op == 6:
        # REINICIO DEL PROGRAMA
        print('> Reiniciando el sistema...')
        input()
    elif op == 7:
        # Salir
        print('Hasta la proxima...')
        input()
        break