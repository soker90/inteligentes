class Estado:
    def __init__(self, localizacion, objetivos):
        self.localizacion = localizacion
        self.objetivos = objetivos

    def __str__(self):
        return( "(" +str(self.localizacion) + "," + str(self.objetivos) + ")")
