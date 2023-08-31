import xml.etree.ElementTree as ET
from senal import senal
from lista_senales import lista_senales
from lista_datos import lista_datos
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
from dato import dato

def cargar_senal():
    route = input('Ingrese la ruta del archivo xml: ')
    archive = open(route,'r')
    archive.close()
    tree = ET.parse(route)
    root = tree.getroot()

    lista_senales_temporal = lista_senales()
    for senal_temporal in root.findall('senal'):
        nombre_senal = senal_temporal.get('nombre')
        t_temporal = senal_temporal.get('t')
        A_temporal = senal_temporal.get('A')
        lista_datos_temporal = lista_datos()
        lista_datos_patrones_temporal = lista_datos()
        lista_patrones_temporal = lista_patrones()
        lista_grupos_temporal = lista_grupos()
        for dato_senal in senal_temporal.findall('dato'):
            t = dato_senal.get('t')
            A = dato_senal.get('A')
            valor = dato_senal.text
            nuevo = dato(int(t),int(A),int(valor))
            lista_datos_temporal.insertar_dato_ordenado(nuevo)

            if valor != 'NULL':
                nuevo = dato(int(t),int(A),1)
                lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
            else:
                nuevo = dato(int(t),int(A),0)
                lista_datos_patrones_temporal.insertar_dato_ordenado(nuevo)
        lista_senales_temporal.insertar_datos(senal(nombre_senal,int(t_temporal),int(A_temporal),lista_datos_temporal,lista_datos_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal)) 
    lista_senales_temporal.recorrer_e_imprimir()
    lista_senales_temporal.calcular_los_patrones('Señales')

cargar_senal()