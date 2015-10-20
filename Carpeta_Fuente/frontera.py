import Queue
class Frontera():
    def __init__(self):
        self.lista = None

    def CrearFrontera(self):
        self.lista = Queue.PriorityQueue()

    def Insertar(self,nodoArbol,valor):
        self.lista.put(valor,nodoArbol)

    def Elimina(self):
        return self.lista.pop(0)

    def EsVacia(self):
        if(self.lista.qsize() == 0):
            return 0;
        else:
            return 1