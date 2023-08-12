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
        self.matriz = self.Matriz()

    class Matriz:
        def __init__(self):
            self.filas = ListaMatriz()

        def agregar_fila(self,fila):
            self.filas.agregar(fila)

class Senalreducida:
    def __init__(self,nombre,A):
        self.nombre = nombre
        self.A = A
        self.grupos = ListaMatriz()
    
    def agregar_grupo(self,grupo):
        self.grupos.agregar(grupo)

class Patron:
    def __init__(self,fila):
        self.fila = fila
    
    def iguales(self,otros):
        return self.fila == otros.fila
    
def cargar_senal(archivo):
    senales = ListaMatriz()
    tree = ET.parse(archivo)
    root = tree.getroot()
    for senal_elemento in root.findall('./senales/senal'):
        nombre = senal_elemento.get('nombre')
        t = int(senal_elemento.get('t'))
        A = int(senal_elemento.get('A'))
        senal = Senal(nombre,t,A)
        matriz = senal.matriz
        for dato_elemento in senal_elemento.findall('./dato'):
            fila_m = int(dato_elemento.get('t'))
            columna_m = int(dato_elemento.get('A'))
            matriz.agregar_fila(fila_m,columna_m)
        senales.agregar(senal)
    return senales

def procesar_senales(senales):
    senalesreducidas = ListaMatriz()
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
            patron_dato['tiempos'].agregar(fila_m)

            for col_m,valor in enumerate(fila):
                if valor == 1:
                    dato = {'A':col_m, 'Valor': 1}
                    patron_dato['datos'].agregar(dato)
        
        for patron_dato in patrones:
            senalreducida.agregar_grupo(patron_dato)

        senalesreducidas.agregar(senalreducida)
        actual = actual.next
    return senalesreducidas

    




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