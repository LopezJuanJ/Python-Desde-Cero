# Diccionarios

- Los diccionarios son un tipo de datos en Python que se utilizan para almacenar pares de valores clave-valor. Cada valor se puede acceder mediante una clave única, que es una cadena o un número.

- Por ejemplo, puedes crear un diccionario que almacena información sobre diferentes personas, donde las claves son los nombres de las personas y los valores son sus edades:

```python
personas = {
  "Juan": 25,
  "Ana": 30,
  "Pedro": 35
}
```
- Para acceder a un valor en un diccionario, puedes usar la sintaxis de corchetes y la clave correspondiente. Por ejemplo, para obtener la edad de Ana, puedes escribir:

```python
edad_ana = personas["Ana"]
```
- También puedes modificar los valores en un diccionario utilizando la misma sintaxis:

```python
personas["Juan"] = 26
```

- Los diccionarios son muy útiles para almacenar y acceder a datos de manera eficiente, ya que las claves se utilizan para acceder directamente a los valores correspondientes sin tener que recorrer todo el diccionario.

- Es importante tener en cuenta que los diccionarios no están ordenados y que las claves deben ser únicas. Si tratas de acceder a un valor mediante una clave que no existe, obtendrás un error. También puedes usar el método get() para obtener un valor de un diccionario de manera segura, especificando un valor predeterminado que se devolverá si la clave no se encuentra en el diccionario.


