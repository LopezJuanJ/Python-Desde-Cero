import re
class Remplazar:
    def filtra():
        texto = "Hoy es lunes 20 de marzo de 2020. Mañana será martes 21 de marzo de 2020."
        numeros = re.findall(r'\d+', texto)
        numeros = [int(x) for x in numeros]
        print(numeros)  # El resultado debería ser: [20, 21, 2020, 2020]
