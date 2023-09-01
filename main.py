from time import sleep
from ListSenales import ListSenales

listSenales = ListSenales()
def main():
    global listSenales

    print("Bienvenido al programa de analisis de señales!")
    input("Press Enter to continue...")

    flag = True
    while flag:
        imprimirTitulo("Menu Principal")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Inicializar sistema")
        print("7. Salida")

        imprimirTitulo("")
        option = input("Seleccione una opción: ")
        if option == "1":
            cargarArchivo()
        elif option == "2":
            listSenales.analizarSenales()
        elif option == "3":
            escribirArchivo()
        elif option == "4":
            mostrarDatos()
        elif option == "5":
            listSenales.generarGrafica()
        elif option == "6":
            listSenales = ListSenales()
        elif option == "7":
            flag = False
        else:
            imprimirTitulo("Opción no válida")
            input("Press Enter to continue...")

def imprimirTitulo(title):
    print("------------------------------------------------")
    print(f'{title}')

def cargarArchivo():
    global listSenales
    imprimirTitulo("Cargar Archivo")
    path = input("Ingrese la ruta del archivo: ")
    if listSenales.leerArchivo(path):
        imprimirTitulo("Archivo cargado con éxito")
    else:
        imprimirTitulo("Error al cargar el archivo")
    input("Press Enter to continue...")

def procesarArchivo():
    global listSenales
    imprimirTitulo("Procesando archivo...")
    listSenales.analizarSenales()
    input("Press Enter to continue...")

def escribirArchivo():
    global listSenales
    path = input("Ingrese la ruta del archivo: ")
    listSenales.escribirArchivo(path)        
    imprimirTitulo("Archivo escrito con éxito")
    input("Press Enter to continue...")

def mostrarDatos():
    imprimirTitulo("Datos del estudiante")
    print("Josue Daniel Chavez Portillo")
    print("Carnet: 202100033")
    print("Introduccion a la Programación y computación 2 seccion 'C'")
    print("Ingenieria en Ciencias y Sistemas")
    print("6to Semestre")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()