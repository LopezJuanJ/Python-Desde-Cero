def odenar_lista(numero1, numero2, numero3, numero4, numero5):
    lista = [numero1, numero2, numero3, numero4, numero5]
    lista.sort()
    return lista

def calcular_media(numero1, numero2, numero3, numero4, numero5):
    lista = [numero1, numero2, numero3, numero4, numero5]
    longitud = len(lista)
    suma = sum(lista)
    media = suma / longitud
    return media
def calcular_mediana(numero1, numero2, numero3, numero4, numero5):
    numeros = odenar_lista(numero1, numero2, numero3, numero4, numero5)
    if len(numeros) % 2 == 0:  
        mediana = (numeros[len(numeros) // 2 - 1] + numeros[len(numeros) // 2]) / 2
    else:
        mediana = numeros[len(numeros) // 2]
    return mediana
         
