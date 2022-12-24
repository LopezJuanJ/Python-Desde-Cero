# Funciones y Modulos

- Por supuesto, estaré feliz de ayudarte a entender mejor cómo funcionan las funciones y módulos en Python.

- Las funciones son bloques de código que realizan una tarea específica y pueden ser reutilizadas en diferentes partes de tu programa. Las funciones se definen con la palabra clave def, seguida del nombre de la función y una lista de parámetros entre paréntesis. Por ejemplo, podríamos definir una función llamada saludar que toma un parámetro llamado nombre de la siguiente manera:

```python
def saludar(nombre):
    print("Hola, " + nombre + "!")
```

- Para llamar a una función, simplemente escribimos su nombre seguido de paréntesis y, si la función toma algún parámetro, debemos proporcionar el valor del parámetro entre los paréntesis. Por ejemplo, podríamos llamar a la función saludar de la siguiente manera:

```python
saludar("Juan")
```

-  Las funciones también pueden devolver un valor mediante la instrucción return. Por ejemplo, podríamos definir una función llamada sumar que toma dos números como parámetros y devuelve su suma:

```python
    def sumar(a, b):
    return a + b
```
- Podríamos llamar a esta función y almacenar su resultado en una variable de la siguiente manera:

```python
resultado = sumar(3, 4)
print(resultado)  # Imprime 7
```
# Modulos
- Los módulos son archivos que contienen código Python y pueden ser importados en otros programas para utilizar su funcionalidad. Por ejemplo, podríamos tener un archivo llamado mi_modulo.py con el siguiente contenido:

```python
def saludar(nombre):
    print("Hola, " + nombre + "!")

def sumar(a, b):
    return a + b
```

- Para utilizar las funciones de este módulo en otro programa, podríamos importar el módulo con la instrucción import y luego acceder a las funciones utilizando el nombre del módulo como prefijo. Por ejemplo:

```python
import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola,
```

# Pregunta

- Hazme una explicación extensa con ejercicios sobre funciones y modulos en python