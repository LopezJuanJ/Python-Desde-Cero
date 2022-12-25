# Ejercicio 

- Sí, puedes importar un archivo con un nombre diferente al nombre que quieres darle al módulo que importas. Para hacer esto, puedes usar la instrucción import seguida del nombre del archivo y luego usar la palabra clave as seguida del nombre que quieres darle al módulo.

- Por ejemplo, supongamos que tienes un archivo llamado mi_modulo.py con el siguiente contenido

```python
# archivo mi_modulo.py

def saludar(nombre):
    print("Hola, " + nombre + "!")
```

- Para importar este módulo en otro programa con el nombre modulo_saludo, podrías hacer lo siguiente:

```python
    import mi_modulo as modulo_saludo

modulo_saludo.saludar("Juan")  # Imprime "Hola, Juan!"
```

- De esta manera, puedes importar un archivo con un nombre diferente al nombre que le quieres dar al módulo en tu programa.

- Espero que esto te haya ayudado a entender cómo importar un archivo con un nombre diferente al nombre del módulo que quieres usar. Si tienes más preguntas, no dudes en preguntar.

# Pregunta
- Puedo importar un fichero con un nombre diferente?

