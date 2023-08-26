import xml.etree.ElementTree as ET

def lectura():
    archivo = ET.parse('C:/Users/cokei/OneDrive/Documentos/GitHub/IPC2__PROYECTO1__202100033/Entrada-Ejemplo.xml')
    raiz =  archivo.getroot()
    ListaSenales = []
    for elementos in raiz:
        Dato = []
        nombre_senal = elementos.get('nombre')
        print(nombre_senal)
        t = int(elementos.get('t'))
        A = int(elementos.get('A'))
        if t > 0 and t <= 3600:
            if A > 0 and A <= 130:
                for dato in elementos.findall('dato'):
                    t = dato.get('t')
                    A = dato.get('A')
                    Valor = dato.text
                    Dato.append([t,A,Valor])
            else:
                print("Rango de A no valido")
        else:
            print("Rango de t no valido")
        ListaSenales.append([nombre_senal,t,A,Dato])

    for Senal in ListaSenales:
        print(Senal[0])
        for dato in Senal[3]:
            print(dato[2])
    

lectura()
            







