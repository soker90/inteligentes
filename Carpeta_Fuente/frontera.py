import Queue
class Frontera:
    def __init__(self):
        self.lista = None

    def CrearFrontera(self):
        self.lista = Queue.PriorityQueue()

    def Insertar(self,nodoArbol,valor):
        self.lista.put(valor,nodoArbol)

    def InsertarLista(self, lis):
        for x in lis:
            self.lista.put(x.valor,x)

    def Elimina(self):
        return self.lista.pop(0)

    def EsVacia(self):
        if(self.lista.qsize() == 0):
            return True
        else:
            return False