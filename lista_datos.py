import sys
import os
from nodo_dato import nodo_dato
from Patron import Patron

class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos = 0

    def insertar_dato(self,dato):
        if self.primero is None:
            self.primero = nodo_dato(dato = dato)
            self.contador_datos += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_dato(dato = dato)
        self.contador_datos += 1
        
    def insertar_dato_ordenado(self,dato):
        nuevo_dato = nodo_dato(dato = dato)
        self.contador_datos += 1
        #Si la lista esta vacia solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nuevo_dato
            return
        #Caso especial
        if dato.t < self.primero.dato.t or(
                dato.t == self.primero.dato.t and dato.A <= self.primero.dato.A):
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                dato.t > actual.siguiente.dato.t or (
                        dato.t == actual.siguiente.dato.t and dato.A > actual.siguiente.dato.A)):
            actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    def recorrer_e_imprimir(self):
        print('=====================================================================')
        actual = self.primero
        while actual != None:
            print('t: ',actual.dato.t,'A: ',actual.dato.A)
            actual = actual.siguiente
            print('=====================================================================')

    #Devolver los patrones por t
    def devolver_patrones_por_t(self,lista_patrones_t):
        actual = self.primero
        sentinela_de_filas = actual.dato.t
        fila_iniciada = False
        recolector_patron = ''
        while actual != None:
            if sentinela_de_filas != actual.dato.t:
                fila_iniciada = False
                lista_patrones_t.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
                recolector_patron = ''
                sentinela_de_filas = actual.dato.t

            if fila_iniciada == False:
                fila_iniciada = True
                recolector_patron += str(actual.dato.valor) + '-'
            else:
                recolector_patron += str(actual.dato.valor) + '-'
            actual = actual.siguiente
            lista_patrones_t.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
            return lista_patrones_t
        
    def generar_grafica(self,nombre_senal,t,A):
        f = open('lectura_xml/bb.dot','w')
        text = """
            digraph G {"t=""" + str(t) + """A=""" + str(A) + """->""" + nombre_senal +  """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    
        actual = self.primero
        sentinela_de_filas=actual.dato.t #iniciaria en 1
        fila_iniciada=False

        while actual != None:
            if  sentinela_de_filas!=actual.dato.t:
                print(sentinela_de_filas,actual.dato.t,"hola")
                sentinela_de_filas=actual.dato.t
                fila_iniciada=False
                # Cerramos la fila
                text +="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.valor+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+actual.dato.valor+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng Lectura_xml/bb.dot -o Lectura_xml/grafo2.png')
        print("terminado") 
        

    def devolver_cadena_del_grupo(self,grupo):
        string_resultado = ''
        string_temporal = ''
        buffer = ''
        for digito in grupo:
            if digito.isdigit():
                buffer += digito
            else:
                string_temporal = ''
                actual = self.primero
                while actual:
                    if actual.dato.t == int(buffer):
                        string_temporal += actual.dato.valor + ','
                    actual = actual.siguiente
                string_resultado += string_temporal + "\n"
                buffer = ''
        return string_resultado