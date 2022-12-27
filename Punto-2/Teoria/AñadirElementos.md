# Añadir elemento a lista
- Para añadir un elemento a una lista en Python, puedes utilizar el método *append()* o la sintaxis de corchetes.

Por ejemplo, suponiendo que tienes una lista llamada numeros:

```python
numeros = [1, 2, 3, 4]
```
- Puedes añadir un elemento al final de la lista utilizando el método append() de la siguiente manera:

```python
numeros.append(5)
```
- Esto añadiría el número 5 al final de la lista numeros, quedando como:

```python
[1, 2, 3, 4, 5]
```

- También puedes utilizar la sintaxis de corchetes para añadir un elemento a una lista en una posición específica. Por ejemplo, para añadir el número 6 en la posición 2 de la lista numeros, puedes utilizar la siguiente sintaxis:

```python
numeros[2:2] = [6]
```
- Esto añadiría el número 6 a la lista numeros en la posición 2, quedando como:

```python
[1, 2, 6, 3, 4, 5]
```

- Es importante tener en cuenta que la sintaxis de corchetes también se puede utilizar para reemplazar un elemento existente en una lista. Por ejemplo, para reemplazar el número 3 por el número 7 en la lista numeros, puedes utilizar la siguiente sintaxis:

```python
numeros[3:4] = [7]
```
- Esto reemplazaría el número 3 por el número 7 en la lista numeros, quedando como:

```python
[1, 2, 6, 7, 4, 5]
```

# Añadir elementos a un diccionario

- Para añadir un elemento a un diccionario en Python, puedes utilizar la sintaxis de corchetes y asignar un valor a una nueva clave.

- Por ejemplo, suponiendo que tienes un diccionario llamado personas:

```python
personas = {
  "Juan": 25,
  "Ana": 30,
  "Pedro": 35
}
```
- Puedes añadir un elemento al diccionario utilizando la siguiente sintaxis:

```python
personas["Marcos"] = 40
```

- Esto añadiría un elemento al diccionario personas con la clave "Marcos" y el valor 40, quedando como:

```python
{
  "Juan": 25,
  "Ana": 30,
  "Pedro": 35,
  "Marcos": 40
}
```

- También puedes utilizar el método update() para añadir varios elementos a un diccionario de manera más eficiente. Por ejemplo:

```python
nuevos_elementos = {
  "Lucas": 45,
  "Sandra": 50
}

personas.update(nuevos_elementos)
```

- Esto añadiría los elementos con las claves "Lucas" y "Sandra" y los valores correspondientes al diccionario personas, quedando como:

```python
{
  "Juan": 25,
  "Ana": 30,
  "Pedro": 35,
  "Marcos": 40,
  "Lucas": 45,
  "Sandra": 50
}
```
- Es importante tener en cuenta que si tratas de asignar un valor a una clave que ya existe en el diccionario, se sobrescribirá el valor anterior.
