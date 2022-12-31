import Ejercicio5_1

p1 = Ejercicio5_1.Datos("datos.txt", "r")

p1.abrir()
p1.linea_a_linea()
print(p1.leer())
p1.cerrar()

p2 = Ejercicio5_1.Resultados("resultados.txt", "w")

p2.abrir()
p2.escribir("Esta es la cadena del fichero")
p2.cerrar()
