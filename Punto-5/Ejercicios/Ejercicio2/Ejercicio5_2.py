class Usuario_Gestion:
    def __init__(self, nombre, modo, archivo):
        self.nombre = nombre
        self.modo = modo
        self.archivo = archivo

    def pedir_modo(self):
        pregunta = input("Dime el modo de apertura: ")
        self.modo = pregunta

    def pedir_nombre(self):
        pregunta = input("Dime el nombre del fichero con su extension: ")
        self.nombre = pregunta
        
    def abrir(self):
        self.archivo = open(self.nombre, self.modo)
    
    def contar_lineas(self):
        contador = 0
        for linea in self.archivo:
            contador = contador + 1
        return contador
