# Clases

- Clases son una forma de organizar y estructurar el código en Python. Una clase es una plantilla para crear objetos. Los objetos tienen características (llamadas atributos) y métodos (funciones) asociadas con ellos.

- Por ejemplo, si estuviéramos creando un juego de aventuras, podríamos crear una clase llamada "Personaje" que almacene información sobre el personaje, como su nombre, puntos de vida y poder de ataque. También podríamos definir métodos para el personaje, como "atacar" o "recibir daño", que permitirían al personaje interactuar con otros elementos del juego.

- Aquí hay un ejemplo de cómo se podría crear una clase en Python:

```python
class Personaje:
  def __init__(self, nombre, vida, ataque):
    self.nombre = nombre
    self.vida = vida
    self.ataque = ataque
    
  def atacar(self, objetivo):
    objetivo.vida -= self.ataque
    
  def recibir_daño(self, daño):
    self.vida -= daño
``` 

- La palabra clave "class" se utiliza para definir una clase en Python, seguida del nombre de la clase. El método especial "init" es un constructor de la clase, que se utiliza para inicializar los atributos del objeto cuando se crea. "self" se refiere al objeto en sí y es necesario para acceder a los atributos y métodos del objeto desde dentro de la clase.

- Para utilizar esta clase, podríamos crear un objeto "personaje" asignándolo a una variable:

```python
p1 = Personaje("Goku", 100, 30)
```
- Luego, podríamos acceder a los atributos del objeto usando el punto (.) y podríamos llamar a sus métodos de la misma manera:

```python
print(p1.nombre)  # imprime "Goku"
p1.atacar(p2)
```

- Las clases son una herramienta poderosa para organizar y reutilizar código en Python. También se pueden heredar de otras clases, lo que permite crear clases más específicas a partir de clases más generales.

# Pregunta

- Hazme una explicacion sobre clases python