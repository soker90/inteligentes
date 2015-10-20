class  nodoBusqueda():
    def __init__(self, id, padre, estado, costo, accion,  profundidad, valor):
        self.id = id
        self.padre = padre
        self.estado = estado
        self.costo = costo
        self.accion = accion
        self.profundidad = profundidad
        self.valor = valor


    def __str__(self):
        return(" Id: "+str(self.id)+" Padre: "+"\n")
