class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def esHoja(self):
        return not (self.i)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def hijosDeUnNodo(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            if nodo.izquierda == None and nodo.derecha == None:
                print("No tiene hijos")
            elif nodo.izquierda == None and nodo.derecha != None:
                dato = nodo.derecha
                print(dato.dato)
            elif nodo.izquierda != None and nodo.derecha == None:
                dato = nodo.izquierda
                print(dato.dato)
            else:
                datoIz = nodo.izquierda
                datoDe = nodo.derecha
                print(datoIz.dato)
                print(datoDe.dato)
        if busqueda < nodo.dato:
            return self.hijosDeUnNodo(nodo.izquierda, busqueda)
        else:
            return self.hijosDeUnNodo(nodo.derecha, busqueda)

    def nietosDeUnNodo(self, nodo, value):
        if nodo == None:
            return
        if nodo.dato == value:
          # TODO:IZQUIERDA Y DERECHA TIENEN DATOS
            if nodo.izquierda != None and nodo.derecha != None:
                if nodo.izquierda.izquierda != None and nodo.izquierda.derecha == None:
                    print(nodo.izquierda.izquierda.dato)
                elif nodo.izquierda.izquierda == None and nodo.izquierda.derecha != None:
                    print(nodo.izquierda.derecha.dato)
                elif nodo.izquierda.izquierda != None and nodo.izquierda.derecha != None:
                    print(nodo.izquierda.izquierda.dato)
                    print(nodo.izquierda.derecha.dato)
                if nodo.derecha.izquierda != None and nodo.derecha.derecha == None:
                    print(nodo.derecha.izquierda.dato)
                elif nodo.derecha.izquierda == None and nodo.derecha.derecha != None:
                    print(nodo.derecha.derecha.dato)
                elif nodo.derecha.izquierda != None and nodo.derecha.derecha != None:
                    print(nodo.derecha.izquierda.dato)
                    print(nodo.derecha.derecha.dato)
            # TODO:IZQUIERDA TIENE DATOS
            elif nodo.izquierda != None:
                if nodo.izquierda.izquierda != None and nodo.izquierda.derecha == None:
                    print(nodo.izquierda.izquierda.dato)
                elif nodo.izquierda.izquierda == None and nodo.izquierda.derecha != None:
                    print(nodo.izquierda.derecha.dato)
                elif nodo.izquierda.izquierda != None and nodo.izquierda.derecha != None:
                    print(nodo.izquierda.izquierda.dato)
                    print(nodo.izquierda.derecha.dato)
            # TODO:DERECHA TIENE DATOS
            elif nodo.derecha != None:
                if nodo.derecha.izquierda != None and nodo.derecha.derecha == None:
                    print(nodo.derecha.izquierda.dato)
                elif nodo.derecha.izquierda == None and nodo.derecha.derecha != None:
                    print(nodo.derecha.derecha.dato)
                elif nodo.derecha.izquierda != None and nodo.derecha.derecha != None:
                    print(nodo.derecha.izquierda.dato)
                    print(nodo.derecha.derecha.dato)

        if value < nodo.dato:
            return self.nietosDeUnNodo(nodo.izquierda, value)
        else:
            return self.nietosDeUnNodo(nodo.derecha, value)

    def hermanoNodo(self, nodo, value):
        if nodo is None:
            return None
        if nodo.izquierda != None and nodo.izquierda.dato == value:
            nodoDer = nodo.derecha
            if nodoDer != None:
                print("El nodo " + str(value) +
                      " es hermano del nodo : " + str(nodoDer.dato))
            else:
                print("El nodo " + str(value) + " no tiene hermano")
        elif nodo.derecha != None and nodo.derecha.dato == value:
            nodoIzq = nodo.izquierda
            if nodoIzq != None:
                print("El nodo " + str(value) +
                      " es hermano del nodo : " + str(nodoIzq.dato))
            else:
                print("El nodo " + str(value) + " no tiene hermano")
        if value < nodo.dato:
            return self.hermanoNodo(nodo.izquierda, value)
        else:
            return self.hermanoNodo(nodo.derecha, value)

    def papaNodo(self, nodo, value):
        if nodo is None:
            return False
        if nodo.izquierda != None and nodo.izquierda.dato == value:
            print("El papá del nodo " + str(value) + " es: " + str(nodo.dato))
        elif nodo.derecha != None and nodo.derecha.dato == value:
            print("El papá del nodo " + str(value) + " es: " + str(nodo.dato))
        if value < nodo.dato:
            return self.papaNodo(nodo.izquierda, value)
        else:
            return self.papaNodo(nodo.derecha, value)

    def nivel(self, nodo, value, level):
        if nodo == None:
            return 0

        if nodo.dato == value:
            return level

        nivel = self.nivel(nodo.izquierda, value, level + 1)

        if nivel != 0:
            return nivel

        nivel = self.nivel(nodo.derecha, value, level + 1)

        return nivel

   # la raíz inicia en 0 para determinar el nivel
    def getNivelNodo(self, nodo, value):
        return self.nivel(nodo, value, 0)

    # la raíz inicia en 1 para determinar la altura o profundidad
    def alturaNodo(self, nodo):
        if nodo == None:
            return -1
        else:
            return 1 + max(self.alturaNodo(nodo.izquierda), self.alturaNodo(nodo.derecha))

    def abueloNodo(self, nodo, padre, abuelo, value):
        if nodo is None:
            return None
        if nodo.dato == value:
            if abuelo == None:
                return -1
            else:
                return abuelo.dato

        if value < nodo.dato:
            return self.abueloNodo(nodo.izquierda, nodo, padre, value)
        else:
            return self.abueloNodo(nodo.derecha, nodo, padre, value)

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    def numeroNodos(self, raiz):
        if raiz is None:
            return 0
        return (1 + self.numeroNodos(raiz.izquierda) + self.numeroNodos(raiz.derecha))

    def esHoja(self, nodo):
        return not (nodo.izquierda or nodo.derecha)

    def valorMenor(self, raiz):
        actual = raiz
        if actual.izquierda == None:
            return actual.dato
        return self.valorMenor(actual.izquierda)

    def valorMayor(self, raiz):
        if raiz == None:
            return float('-inf')
        mayor = raiz.dato
        izq = self.valorMayor(raiz.izquierda)
        der = self.valorMayor(raiz.derecha)
        if izq > der:
            mayor = izq
        if der > mayor:
            mayor = der
        return mayor

    def eliminarNodo(self, raiz, dato):
        if raiz == None:
            return
        if dato < raiz.dato:
            raiz.izquierda = self.eliminarNodo(raiz.izquierda, dato)
        elif dato > raiz.dato:
            raiz.derecha = self.eliminarNodo(raiz.derecha, dato)
        else:
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp
            temp = self.valorMenor(raiz.derecha)
            raiz.dato = temp.dato
            raiz.derecha = self.eliminarNodo(raiz.derecha, temp.dato)
        return raiz

# TODO: EL DE LOS HIJOS PREGUNTAR.SI TIENE.IZQUIERDA Y DERECHA


class Main:

    def __init__(self):
        self.menu()

    def pedirOpcion(self):
        bien = False
        op = 0
        while (not bien):
            try:
                op = int(input("Teclea opción: "))
                bien = True
                print("\n")
            except ValueError:
                print('Error, introduce un numero entero')
        return op

    def menu(self):
        salir = False
        opc = 0
        while (not salir):
            print("")
            print("1. Agregar raíz")
            print("2. Agregar nodos")
            print("3. Imprimir inorden")
            print("4. Imprimir postoren")
            print("5. Imprimir preorden")
            print("6. Buscar dato")
            print("7. Número de nodos")
            print("8. Eliminar nodo")
            print("9. Mostrar hijos de un nodo")
            print("10. Mostrar hermano de un nodo")
            print("11. Papá de un nodo")
            print("12. Nivel de un nodo")
            print("13. Altura árbol")
            print("14. Nietos de un nodo")
            print("15. Abuelo de un nodo")
            print("16. Salir")
            opc = self.pedirOpcion()
            if opc == 1:
                dato = int(input("Ingresar raíz del árbol: "))
                arbol = Arbol(dato)
                print("\n")
            elif opc == 2:
                dato = int(input("Ingresar dato: "))
                arbol.agregar(dato)
                print("\n")
            elif opc == 3:
                arbol.inorden()
                print("\n")
            elif opc == 4:
                arbol.postorden()
                print("\n")
            elif opc == 5:
                arbol.preorden()
                print("\n")
            elif opc == 6:
                dato = int(input("Ingresar el dato a buscar: "))
                bus = arbol.buscar(23)
                if bus == True:
                    print(" *** El dato: " + str(dato) + " si existe ***")
                else:
                    print("**** El dato ingresado no existe ****")
                print("\n")
            elif opc == 7:
                numeroNodos = arbol.numeroNodos(arbol.raiz)
                print("El árbol tiene : " + str(numeroNodos) + " nodos")
                print("\n")
            elif opc == 8:
                dato = int(input("Ingrese el nodo a eliminar: "))
                arbol.eliminarNodo(arbol.raiz, dato)
                arbol.inorden()
            elif opc == 9:
                dato = int(input("Ingresar dato: "))
                arbol.hijosDeUnNodo(arbol.raiz, dato)
            elif opc == 10:
                dato = int(input("Ingresar dato: "))
                arbol.hermanoNodo(arbol.raiz, dato)
            elif opc == 11:
                dato = int(input("Ingresar dato: "))
                arbol.papaNodo(arbol.raiz, dato)
            elif opc == 12:
                dato = int(input("Ingresar dato: "))
                nivel = arbol.getNivelNodo(arbol.raiz, dato)
                print("El nivel del nodo " + str(dato) + " es: " + str(nivel))
            elif opc == 13:
                altura = arbol.alturaNodo(arbol.raiz)
                print("La altura del árbol es: " + str(altura))
            elif opc == 14:
                dato = int(input("Ingresar dato: "))
                arbol.nietosDeUnNodo(arbol.raiz, dato)
            elif opc == 15:
                dato = int(input("Ingresar dato: "))
                abuelo = arbol.abueloNodo(arbol.raiz, None, None, dato)
                print("El abuelo del nodo " + str(dato) + " es: " + str(abuelo))
            elif opc == 16:
                salir = True
            else:
                print("Introduce una opción entre 1 y 11")


main = Main()
