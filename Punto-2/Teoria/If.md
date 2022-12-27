# If

- Los *if* son una estructura de control de flujo en Python que te permite ejecutar ciertas instrucciones solo si se cumple una condición específica. La sintaxis básica de una declaración if es la siguiente:

```python
if condición:
    # código a ejecutar si se cumple la condición
```

- La condición puede ser cualquier expresión que devuelva un valor booleano (True o False). Si la condición se evalúa como True, se ejecutará el código indentado debajo del if. Si se evalúa como False, se saltará ese código y se continuará con la siguiente línea de código después del bloque indentado.

- Aquí tienes un ejemplo de una declaración if en acción:

```python
x = 10
if x > 5:
    print("x es mayor que 5")
```

- En este caso, se imprimiría "x es mayor que 5" porque la condición x > 5 se evalúa como True.

- Además de la declaración if básica, también puedes utilizar declaraciones if anidadas y declaraciones if-else para ejecutar código en función de múltiples condiciones. Aquí tienes un ejemplo de una declaración if-else:
```python
x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")
```

- En este caso, se imprimiría "x es mayor que 5" porque la condición x > 5 se evalúa como True. Si la condición se hubiera evaluado como False, se habría ejecutado el código indentado debajo del else en lugar del código indentado debajo del if.

- También puedes usar una declaración if-elif-else para comprobar múltiples condiciones. La sintaxis para una declaración if-elif-else es la siguiente:

```python
if condición1:
    # código a ejecutar si se cumple la condición1
elif condición2:
    # código a ejecutar si se cumple la condición2
else:
    # código a ejecutar si ninguna de las condiciones anteriores se cumple
``` 

- En este caso, se evalúa la primera condición. Si se evalúa como True, se ejecuta el código indentado debajo del if