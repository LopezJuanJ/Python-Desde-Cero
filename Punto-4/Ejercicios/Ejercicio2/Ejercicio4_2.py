class Coche:
    def __init__(self, marca, modelo, anho, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.anho = anho
        self.kilometros = kilometros
    
    def get_descripcion(self):
        res = "El coche es de la marca " + self.marca + ", su modelo es " + self.modelo + ", fue creado en el año " + str(self.anho) + " y tiene " + str(self.kilometros) + " kilometros"
        return res 

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, anho, kilometros, tamaño_bateria):
        super().__init__(marca, modelo, anho, kilometros)
        self.tamaño_bateria = tamaño_bateria
    def get_autonomia(self):
        res = "Este coche puede recorrer " + str(self.tamaño_bateria) + " kilometros con la bateria con carga completa"   
        return res
