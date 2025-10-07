"""
Ejemplo de uso de la librería bigtree para crear y mostrar un árbol no binario.
Crea un árbol con una raíz, varios hijos así sucecivamente.
Imprime la estructura del árbol.
Busca el nodo 'C' y muestra los nombres de sus hijos.
"""

from bigtree import Node, print_tree, find_child_by_name

# Crear la raíz y los nodos del árbol
raiz = Node("A")
Node("B", parent=raiz)
Node("C", parent=raiz)
Node("D", parent=raiz)
Node("E", parent=raiz.children[0])  # Hijo de B
Node("F", parent=raiz.children[0])  # Hijo de B
Node("G", parent=raiz.children[1])  # Hijo de C
Node("H", parent=raiz.children[1])  # Hijo de C
Node("I", parent=raiz.children[2])  # Hijo de D

# Imprimir la estructura del árbol
print_tree(raiz)

# Buscar el nodo 'C' y mostrar los nombres de sus hijos
nodo = find_child_by_name(raiz, "C")
if nodo:
    print([h.name for h in nodo.children])