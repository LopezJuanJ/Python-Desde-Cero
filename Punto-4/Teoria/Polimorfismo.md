# Polimorfismo
- A continuación, te proporcionaré algunos ejemplos de polimorfismo en Python:

- Sobrecarga de operadores: La sobrecarga de operadores permite que un operador tenga diferentes comportamientos dependiendo del tipo de datos con el que esté trabajando. Por ejemplo:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

rect1 = Rectangle(2, 3)
rect2 = Rectangle(3, 4)

# Sumar dos rectángulos
rect3 = rect1 + rect2
print(rect3.area())  # Imprime 14

# El operador + tiene un comportamiento diferente dependiendo del tipo de datos con el que esté trabajando.
# Si se utiliza con dos números, realiza una suma aritmética.
# Si se utiliza con dos objetos de la clase Rectangle, devuelve un nuevo objeto de la clase Rectangle que es la suma de los dos rectángulos originales.

```
# Pregunta
- Hazme una explicacion de polimorfismo en python con ejemplos