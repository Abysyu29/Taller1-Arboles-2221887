"""
Taller de arbol
Andrés Sebastián Pinzón Gutiérrez 2221887
Nota: El código permite ingresar cualquier tipo de valor para los nodos (números, letras, etc.)
nota 2: La documentación fue sugerida o con ayuda de copilot bajo una redacción para enteder el código.
nota 3: Cuando se ingresa un nodo padre, este debe haber sido ingresado previamente como raíz o hijo de otro nodo padre
        y para cuando se agrega un hijo, este no debe existir previamente en el árbol, de lo contrario se sobreescribe el nodo.
"""

class Nodo:
    #Función constructor de la clase Nodo
    def __init__(self, valor):
        self.valor = valor
        self.hijos = [] # Lista para almacenar los hijos del nodo

class Arbol:

    #Función constructor de la clase Arbol
    def __init__(self, raiz):
        self.raiz = Nodo(raiz) # Crea el nodo raíz del árbol

    # Función para agregar un hijo a un nodo dado
    def agregar_hijo(self, nodo_padre, valor_hijo): # Agrega un nuevo hijo al nodo padre especificado
        nuevo_hijo = Nodo(valor_hijo)   
        nodo_padre.hijos.append(nuevo_hijo) 
        return nuevo_hijo   # Retorna el nuevo nodo hijo para referencia futura

    # a) Función del Peso del árbol (número total de nodos)
    def peso(self, nodo=None):
        # Si no se proporciona un nodo, se usa la raíz
        if nodo is None:
            nodo = self.raiz 
        total = 1   # Cuenta el nodo actual

        # Recorre los hijos y suma sus pesos
        for hijo in nodo.hijos: 
            total += self.peso(hijo)
        return total    # Retorna el peso total

    # b) Función para el Orden del árbol (máximo número de hijos que tiene un nodo)
    def orden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz    # Usa la raíz si no se proporciona un nodo
        max_hijos = len(nodo.hijos) # Cuenta los hijos del nodo actual
        
        # Recorre los hijos para encontrar el máximo orden
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self.orden(hijo))
        return max_hijos    # Retorna el orden máximo

    # c) Función de la Altura del árbol (número máximo de niveles)
    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz # Usa la raíz si no se proporciona un nodo
        
        # Si el nodo no tiene hijos, su altura es 1
        if not nodo.hijos:
            return 1
        alturas_hijos = [self.altura(hijo) for hijo in nodo.hijos] # Alturas de los hijos
        return 1 + max(alturas_hijos)   # Altura es 1 + altura máxima de los hijos

# Creación del árbol
if __name__ == "__main__":
    valor_raiz = input("Ingrese el valor de la raíz: ") #valor de la raíz pueden ser números o letras
    arbol = Arbol(valor_raiz)   # Crear el árbol con la raíz dada

    nodos = {valor_raiz: arbol.raiz}

    while True: # Bucle para agregar nodos hasta que el usuario decida terminar
        padre = input("Ingrese el nodo padre (o 'fin' para terminar): ")    
        """Solicita el nodo padre, tener en cuenta que el nodo padre debe existir,
           ej si el nodo padre es 'A', 'A' debe haber sido ingresado previamente 
           como raíz o hijo de otro nodo padre."""
        
        if padre.lower() == "fin": 
            break # Termina el bucle si el usuario ingresa 'fin'
        if padre not in nodos:  # Verifica si el nodo padre existe
            print("El nodo padre no existe.")
            continue # Continúa al siguiente ciclo si el padre no existe
        hijo = input(f"Ingrese el hijo de {padre}: ")   # Solicita el valor del hijo
        nuevo_hijo = arbol.agregar_hijo(nodos[padre], hijo) # Agrega el hijo al árbol
        nodos[hijo] = nuevo_hijo    # Guarda el nuevo nodo en el diccionario para referencia futura

    print("\n=== Resultados ===")   # Muestra los resultados
    print("Peso del árbol:", arbol.peso())  # Peso total de nodos tenidos en el árbol
    print("Orden del árbol:", arbol.orden())    # Máximo número de hijos que tiene un nodo del árbol
    print("Altura del árbol:", arbol.altura())  # Número máximo de niveles del árbol
