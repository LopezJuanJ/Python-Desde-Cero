def  contar_vocales(palabra):
    
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    contador_espacio = 0
    contador_consonates = 0
    
    
    for letra in palabra:
        if letra == "a":
            contador_a = contador_a + 1
        elif letra == "e":
            contador_e = contador_e + 1
        elif letra == "i":
            contador_i = contador_i + 1
        elif letra == "o":
            contador_o = contador_o + 1
        elif letra == "u":
            contador_u = contador_u + 1
        elif letra == " ":
            contador_espacio = contador_espacio + 1
        else:
            contador_consonates = contador_consonates + 1
   
    resultado_a = "a: " + str(contador_a)
    resultado_e = "e: " + str(contador_e)
    resultado_i = "i: " + str(contador_i)
    resultado_o = "o: " + str(contador_o)
    resultado_u = "u: " + str(contador_u)
    
    #Para concatenar hay que decir el tipo de la variable
    resultado_conso = "consonantes: " + str(contador_consonates)
    return resultado_a,  resultado_e, resultado_i, resultado_o, resultado_u, resultado_conso
