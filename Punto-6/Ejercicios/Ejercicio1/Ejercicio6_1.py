import re
class Remplazar:
    def __init__(self, texto, palabra, filtro):
        self.texto = texto
        self.palabra = palabra
        self.filtro = filtro
    
    def pedir_cadena(self):
        self.texto = input("Dame Una Cadena De Texto: ")
    
    def pedir_palabra(self):
        new_palabra = input("Dame Una letra/numero (especifica mayus y minus): ")
        self.palabra = new_palabra
    
    def generar_filtro(self):
        parte1 = "r"
        parte2 = "\""
        parte3 = "\\b"
        corchete1 = "["
        corchete2 = "]"
        parte5 = self.palabra
        parte6 = "\\w+"

        res = parte1 + parte2 + parte3 + corchete1+ parte5 +corchete2 + parte6 + parte2
        return res
