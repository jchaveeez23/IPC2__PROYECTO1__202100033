from nodo_patron import nodo_patron

class lista_patrones:
    def __init__(self):
        self.primero= None
        self.contador_patrones = 0

    def insertar_dato(self,patron):
        if self.primero is None:
            self.primero = nodo_patron(patron = patron)
            self.contador_patrones += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_patron(patron = patron)
        self.contador_patrones += 1

    def recorrer_e_imprimir(self):
        print('=====================================================================')
        actual = self.primero
        while actual != None:
            print('t: ',actual.patron.t,'Cadena: ',actual.patron.cadena_patron)
            actual = actual.siguiente
            print('=====================================================================')

    def eliminar(self,t):
        actual = self.primero
        anterior = None
        while actual and actual.patron.t != t:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def encontar_coincidencias(self):
        print('')
        print('')
        print('')
        print('')
        resultado = ''
        while self.primero:
            actual = self.primero
            temp_string = ''
            temp_t = ''

            while actual:
                if actual.patron.cadena_patron == self.primero.patron.cadena_patron:
                    temp_t += (str(actual.patron.t)) + ','

                actual = actual.siguiente
            buffer = ''
            #print(temp_t)
            for digito in temp_t:
                if digito.isdigit():
                    buffer += digito
                else:
                    if buffer != '':
                        self.eliminar(int(buffer))
                        buffer = ''
                    else:   
                        buffer = ''
            resultado += temp_t + '--'
        return resultado