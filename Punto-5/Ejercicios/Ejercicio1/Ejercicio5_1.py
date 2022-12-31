class Datos:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        #Defino archivo para poder usarlo mas veces
        self.archivo = None

    def abrir(self):
        self.archivo = open(self.nombre, self.modo)

    def linea_a_linea(self):
        for linea in self.archivo:
            print(linea)

    def cerrar(self):
        self.archivo.close()
    
    def leer(self):
        res = self.archivo.read()
        return res

class Resultados:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        #Defino archivo para poder usarlo mas veces
        self.archivo = None

    def abrir(self):
        self.archivo = open(self.nombre, self.modo)
    
    def cerrar(self):
        self.archivo.close()

    def escribir(self, cadena):
        res = self.archivo.write(cadena)
        print("Ficchero Modificado")
        return res