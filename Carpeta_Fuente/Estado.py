class Estado:
    def __init__(self, localizacion, objetivos, lat, lon):
        self.localizacion = localizacion
        self.objetivos = objetivos
        self.lat=lat
        self.lon=lon

    def __str__(self):
        return( "(" +str(self.localizacion) + "," + str(self.objetivos) + ")")
