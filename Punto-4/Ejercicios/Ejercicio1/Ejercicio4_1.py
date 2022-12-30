class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def saludar(self):
        resultado = "Hola mi nombre es " + self.nombre + "y tengo " + str(self.edad) + "años"
        return resultado