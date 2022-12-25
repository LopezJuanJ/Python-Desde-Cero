def suma(a, b):
    result = a+b
    return result

def resta(a, b):
    result = a-b
    return result

def multiplicacion(a, b):
    result = a*b
    return result

def division(a, b):
    result = a/b
    return result

def saludar():
    nombre = input("Damee tu nombre: ")
    result = "Hola " + nombre 
    return result    

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
def es_primo(numero):
    if numero < 2: 
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True
