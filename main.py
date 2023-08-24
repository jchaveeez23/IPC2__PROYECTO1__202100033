import xml.etree.ElementTree as ET
from graphviz import Digraph
import os

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
                self.filas.cabeza = Nodo([0]*self.A)

            actual = self.filas.cabeza
            for x in range(nfila):
                if actual.next:
                    actual = actual.next
                else:
                    nueva_fila = [0]*self.A
                    actual.next = Nodo(nueva_fila)
                    actual = actual.next
            fila = actual.dato
            fila[ncol] = 1


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
    print('si las guarda xd')
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
                    dato = {'A':col_m, 'value': 0}
                    patron_dato['datos'].agregar(dato)
        
        for patron_dato in patrones:
            senalreducida.agregar_grupo(patron_dato)

        senalesreducidas.agregar(senalreducida)
        actual = actual.next
    print('las procesa')
    return senalesreducidas

    
def Escritura_Salida(nombrearchivo,senalesreducidas):
    root = ET.Element('senalesReducidas')
    actual = senalesreducidas.cabeza
    while actual:
        senalreducida = actual.dato
        elemen_senal = ET.SubElement(root,'senal',{'nombre': senalreducida.nombre, 'A': str(senalreducida.A)})
        grupo_actual = senalreducida.grupos.cabeza
        while grupo_actual:
            grupo = grupo_actual.dato
            grupo_elem = ET.SubElement(elemen_senal,'grupo',{'g':str(grupo['g'])})
            tiempo_elem = ET.SubElement(grupo_elem,'tiempos')
            for tiempo in grupo['tiempos']:
                ET.SubElement(tiempo_elem,'tiempo').text = str(tiempo)
            dato_elemen = ET.SubElement(grupo_elem,'datosGrupo')
            dato_actual = grupo['datos'].cabeza
            while dato_actual:
                dato = dato_actual.dato
                ET.SubElement(dato_elemen,'dato',{'A':str(dato['A'])}).text = str(dato['valor'])
                dato_actual = dato_actual.next
            grupo_actual = grupo_actual.next
        actual = actual.next
    tree = ET.ElementTree(root)
    tree.write(nombrearchivo,encoding='utf-8',xml_declaration=True)

def graficar(senal):
    dot = Digraph(format='png')
    dot.node(senal.nombre)

    grupo_actual = senal.grupos.cabeza
    while grupo_actual:
        grupo = grupo_actual.dato
        group_nombre = f"Grupo {grupo['g']}"
        dot.node(group_nombre)
        dot.edge(senal.nombre, group_nombre)

        for tiempo in grupo['tiempos']:
            dot.node(f"Tiempo {tiempo}")
            dot.edge(group_nombre, f"Tiempo {tiempo}")

        dato_actual = grupo['datos'].cabeza
        while dato_actual:
            dato = dato_actual.dato
            dot.node(f"Dato A{dato['A']}", label=f"A{dato['A']}:{dato['value']}")
            dot.edge(f"Tiempo {dato['A']}", f"Dato A{dato['A']}")
            dato_actual = dato_actual.next
        
        grupo_actual = grupo_actual.next

    dot.render(senal.nombre, cleanup=True)

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
            senales = cargar_senal(archivo)
            actual = senales.cabeza
            while actual:
                Lista.agregar(actual.dato.nombre)
                actual = actual.next
            print('Archivo Cargado exitosamente...')
            input()
        elif op  == 2:
            # PROCESAMIENTO DEL ARCHIVO
            print('------------------PROCESAMIENTO-----------------')
            if not senales.cabeza:
                print('No hay datos para procesar.')
                input()
                continue
            senales_reducidas = procesar_senales(senales)
            print('Señales procesadas con exito...')
            input()
        elif op == 3:
            # SALIDA DE DATOS EN UN ARCHIVO
            print('-------------------SALIDA----------------------')
            if not senales_reducidas:
                print('Se deben procesar datos primero...')
                continue
            output = input('Ingrese el nombre del archivo de salida: ')
            Escritura_Salida(output,senales_reducidas)
            print('Archivo de salida creado con exito...')
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
            if not senales.cabeza:
                print('Debe Cargar un Archivo primero...')
                continue
            nombre_senal = input('Ingrese el nombre de la señal para generar la grafica: ')
            actual = Lista.cabeza
            while actual:
                if actual.dato == nombre_senal:
                    senal = actual.dato
                    break
                actual = actual.next
            if senal:
                graficar(senal)
                print(f'Grafica Generada con Exito para la señal {nombre_senal}')
            else:
                print(f'No se enconto la señal {nombre_senal}')

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
    