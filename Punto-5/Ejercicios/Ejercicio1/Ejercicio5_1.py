class Gestion:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo

    def abrir(self):
        f = open(self.nombre, self.modo)
        return f

    def linea_a_linea(self):
        archivo = open(self.nombre, self.modo)
        for linea in archivo:
            print(linea)

    def cerrar(self):
        archivo = open(self.nombre, self.modo)
        archivo.close() 

    
    
