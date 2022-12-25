#Primera parte
mi_lista = [1, 2, "tres", 4.0, True]

#Segunda parte
mi_diccionario = {
    "edad" :25,
    "altura": 1.80,
    "nombre":"Juan",
    "soltero":True
}

#Tercera Parte
print(type(mi_lista))
print(type(mi_diccionario))

#Cuarta parte
print(mi_lista[2])
print(mi_diccionario["nombre"])

#Quinta parte
#Con el metodo .append añadimos lo que hay entre parentesis a mi_lista
mi_lista.append(False)
print(mi_lista)

#Sexta Parte
mi_diccionario["trabajo"] = "ingeniero"
print(mi_diccionario)