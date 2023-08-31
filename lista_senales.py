from nodo_senal import nodo_senal
from grupo import grupo
import xml.etree.ElementTree as ET

class lista_senales:
    def __init__(self):
        self.primero = None
        contador_senales = 0

    def insertar_datos(self,senal):
        if self.primero is None:
            self.primero = nodo_senal(senal = senal)
            self.contador_senales += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_senal(senal = senal)
        self.contador_senales += 1

    def recorrer_e_imprimir(self):
        print('Total de Señales Almacenadas: ',self.contador_senales)
        print('')
        print('')
        print('')
        print('*********************************************************************')
        actual = self.primero
        while actual != None:
            print('Nombre de la Señal: ',actual.senal.nombre,'t: ',actual.senal.t,'A: ',actual.senal.A)
            actual.senal.lista_dato.recorrer_e_imprimir()
            actual.senal.lista_patrones_dato.recorrer_e_imprimir()
            actual = actual.siguiente   
            print('')
            print('')
            print('')
            print('*********************************************************************')
            print('')
            print('')
            print('')

    def calcular_los_patrones(self,nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre == nombre_senal:
                actual.senal.lista_patrones_dato = actual.senal.lista_patrones_dato.devolver_patrones_por_t(actual.senal.lista_patrones_dato)
                actual.senal.lista_patrones_dato.recorrer_e_imprimir()
                lista_patrones_temporal = actual.senal.lista_patrones_dato
                grupos_sin_analizar = lista_patrones_temporal.encontrar_coincidencias()
                print('Grupos sin analizar: ',grupos_sin_analizar)
                buffer = ''
                for digito in grupos_sin_analizar:
                    if digito.isdigit or digito == '.':
                        buffer += digito
                    elif digito == '-'or buffer != '':
                        cadena_grupo = actual.senal.lista_datos.devolver_cadena_de_grupo(buffer)
                        actual.senal.lista_grupos.insertar_grupo(grupo=grupo(buffer,cadena_grupo))
                        buffer = ''
                    else:
                        buffer = ''
                actual.senal.lista_grupos.recorrer_e_imprimir()
                return
            actual = actual.siguiente
            print('No se encontro la señal')

    