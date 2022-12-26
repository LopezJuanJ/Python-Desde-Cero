def odenar_lista(numero1, numero2, numero3, numero4, numero5):
    lista = [numero1, numero2, numero3, numero4, numero5]
    print(lista)
    lista.sort()
    return lista

def calcular_media(numero1, numero2, numero3, numero4, numero5):
    lista = [numero1, numero2, numero3, numero4, numero5]
    longitud = len(lista)
    suma = sum(lista)
    media = suma / longitud
    return media