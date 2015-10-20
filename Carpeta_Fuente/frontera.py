#Implementar una lista ordenada de nodos del  árbol de búsqueda.
# El orden será de menor a mayor valor de 'Valor' de los nodos y con las siguientes operaciones:

#    CreaFrontera: Crea la frontera vacia y establece el criterio de ordenación.
#    Insertar(nodoArbol): Añada un nodo nuevo a la frontera.
#    Elimina(): Devuelve el primer nodo de la frontera y lo elimina de la misma.
#    EsVacia(): Si o No
import Queue
class Frontera():
    def __init__(self):
        self.lista = None;

    def CrearFrontera(self):
        self.lista = Queue.PriorityQueue()

    def Insertar(self,nodoArbol):
        self.lista.put()