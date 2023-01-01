# Patron
```python
pattern = r"\b[aA]\w+"
```
- r indica que es una expresion regular

- El patrón utilizado en ambos ejemplos es r"\b[aA]\w+". Esta expresión regular tiene varios elementos que trabajan juntos para buscar y reemplazar patrones en una cadena de texto:

- \b indica un límite de palabra. Esto significa que la expresión regular sólo buscará palabras completas que empiecen con "a" o "A", y no sólo letras "a" o "A" dentro de palabras.

- [aA] indica que la expresión regular debe buscar tanto "a" como "A". Al usar corchetes con varias letras, estamos indicando que cualquiera de ellas puede ser aceptada.

- \w+ indica que debemos buscar una o más letras, números o guiones bajos. Al usar el símbolo +, estamos indicando que debemos buscar una o más ocurrencias de la expresión anterior (en este caso, cualquier letra, número o guion bajo).

- En resumen, este patrón busca palabras completas que empiecen con "a" o "A", seguidas de una o más letras, números o guiones bajos. Al usar esta expresión regular con la función re.findall(), podemos obtener una lista de todas las palabras que cumplan con este patrón en una cadena de texto. Al usarla con la función re.sub(), podemos reemplazar todas estas palabras por otra cadena de texto.


# Pregunta 
- Explicame paso a paso que hace el pattern