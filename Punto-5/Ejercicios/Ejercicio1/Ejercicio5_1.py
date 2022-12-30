class Gestion:
    def __init__(self, nombre, fichero, modo):
        self.nombre = nombre
        self.fichero = None
        self.modo = modo

    
    def abrir(self):
        self.fichero = open(self.nombre, self.modo)

    def cerrar(self):
        self.fichero.close
