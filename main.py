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
    elif op  == 2:
        # PROCESAMIENTO DEL ARCHIVO
        print('------------------PROCESAMIENTO-----------------')
    elif op == 3:
        # SALIDA DE DATOS EN UN ARCHIVO
        print('-------------------SALIDA----------------------')
    elif op == 4:
        # MOSTRAR INFORMACION DEL ESTUDIANTE
        print('> Josue Daniel Chavez Portillo')
        print('> 202100033')
        print('> Introduccion a la programacion y computacion 2 seccion "C"')
        print('> Ingenieria en ciencias y sistemas')
        print('> 6to Semestre :(')
    elif op == 5:
        # GRAFICA GENERADA
        print('> Elija la grafica que desea ver')
        print('> 1. Señales Emitidas')
        print('> 2. Señales Reducidas')
    elif op == 6:
        # REINICIO DEL PROGRAMA
        print('> Reiniciando el sistema...')
    elif op == 7:
        # Salir
        print('Hasta la proxima...')
        break