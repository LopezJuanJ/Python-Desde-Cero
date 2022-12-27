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

- Puedes crear un diccionario con varios nombres en Python de varias maneras. Una forma es utilizar la sintaxis de llaves y asignar pares clave-valor a través de dos puntos. Por ejemplo, para crear un diccionario que almacene el nombre y la edad de varias personas, puedes hacer lo siguiente:

```python
personas = {
  "Juan": 25,
  "Ana": 30,
  "Pedro": 35
}
```

- Otra forma de crear un diccionario es utilizando el método dict(), que toma dos argumentos: una lista de claves y una lista de valores. Por ejemplo:

```python
nombres = ["Juan", "Ana", "Pedro"]
edades = [25, 30, 35]

personas = dict(zip(nombres, edades))
```
- En este caso, se creará un diccionario con las claves y los valores correspondientes enlazados por su posición en las listas.

- También puedes utilizar una comprensión de diccionario para crear un diccionario con varios nombres. Por ejemplo:

```python
nombres = ["Juan", "Ana", "Pedro"]
edades = [25, 30, 35]

personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
```

- En este caso, se creará un diccionario con las claves y los valores correspondientes enlazados por su posición en las listas.