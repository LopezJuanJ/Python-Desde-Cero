# Pedimos al usuario informacion

#Uso un bucle para que el usuario pueda decir los numeros

print("Dime tu compra")

numero_objetos = input("Cuantas Cosas has comprado: ")
numero_objetos = int(numero_objetos)

total = 0
for i in range(numero_objetos):
    
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))

    importe = precio * cantidad
    total = total + importe

print("El total de la compra es", total)
   





  
 
