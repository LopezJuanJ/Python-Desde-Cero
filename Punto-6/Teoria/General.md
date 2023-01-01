# Expresiones regulares

- Las expresiones regulares son una herramienta muy útil para buscar y reemplazar patrones en cadenas de texto. Por ejemplo, podemos usar una expresión regular para buscar todas las palabras que empiezan con "a" en una cadena de texto:

```python
import re

texto = "Aquí hay una lista de palabras que empiezan con la letra a: aburrido, apagar, abierto"
pattern = r"\b[aA]\w+"
resultado = re.findall(pattern, texto)

print(resultado)
```
- El resultado sería: ['aburrido', 'apagar', 'abierto']

- También podemos usar una expresión regular para reemplazar todas las palabras que empiezan con "a" por "***":

```python
import re

texto = "Aquí hay una lista de palabras que empiezan con la letra a: aburrido, apagar, abierto"
pattern = r"\b[aA]\w+"
nuevo_texto = re.sub(pattern, "***", texto)

print(nuevo_texto)
```
- El resultado sería: "Aquí hay una lista de palabras que empiezan con la letra a: ***, ***, ***"

# Pregunta
- Hazme un resumen extenso sobre expresiones regulares con ejemplos en Python

