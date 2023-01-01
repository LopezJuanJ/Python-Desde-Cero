import re
class Remplazar:
    def __init__(self, texto, palabra, filtro):
        self.texto = texto
        self.palabra = palabra
        self.filtro = filtro
    
    def pedir_cadena(self):
        self.texto = input("Dame Una Cadena De Texto: ")
    
    def pedir_palabra(self):
        new_palabra = input("Dame Una Palabra/Numero De Filtro: ")
        self.palabra = new_palabra
    
    def generar_filtro(self):
        patron = "r\b" + re.escape(self.palabra) + "r\w+"
        self.filtro = patron
        print(self.filtro)