class Estado():
    def __init__(self, localizacion, objetivos):
        self.localizacion=localizacion
        self.objetivos=objetivos

    def __str__(self):
        return("Localizacion: " + str(self.localizacion) + " Debemos visitar: " + str(self.objetivos))
