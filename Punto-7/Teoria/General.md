Claro, aquí te dejo un ejemplo para cada una de las librerías NumPy y Pandas en Python:

# NumPy

- Supongamos que tenemos un conjunto de datos en forma de lista de Python y queremos realizar algunos cálculos estadísticos. Podemos usar NumPy para convertir esta lista en un arreglo y realizar operaciones numéricas sobre él.

```python
Copy code
import numpy as np

# Crear una lista de datos
data = [5, 6, 7, 8, 9, 10]

# Convertir la lista en un arreglo de NumPy
arr = np.array(data)

# Calcular la media y desviación estándar del arreglo
mean = np.mean(arr)
std = np.std(arr)

# Imprimir los resultados
print("Media:", mean)
print("Desviación estándar:", std)
```
Este código toma una lista de números y la convierte en un arreglo de NumPy usando np.array(). Luego, calcula la media y la desviación estándar del arreglo usando np.mean() y np.std(), respectivamente. Finalmente, se imprimen los resultados.

# Pandas

- Supongamos que tenemos un conjunto de datos en forma de archivo CSV y queremos leerlo en Python para realizar algunas manipulaciones. Podemos usar Pandas para leer el archivo CSV en un DataFrame y luego realizar operaciones de limpieza y filtrado de datos.

```python
Copy code
import pandas as pd

# Leer un archivo CSV en un DataFrame de Pandas
df = pd.read_csv('datos.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Seleccionar solo las filas donde la columna "edad" es mayor a 30
filtro = df['edad'] > 30
df_filtrado = df[filtro]

# Mostrar las primeras filas del DataFrame filtrado
print(df_filtrado.head())

# Calcular la media de la columna "puntaje"
media_puntaje = df['puntaje'].mean()

# Imprimir la media de la columna "puntaje"
print("Media de puntaje:", media_puntaje)
```
- Este código lee un archivo CSV llamado "datos.csv" en un DataFrame de Pandas usando pd.read_csv(). Luego, muestra las primeras filas del DataFrame con df.head(). Después, filtra el DataFrame para seleccionar solo las filas donde la columna "edad" es mayor a 30 y lo guarda en un nuevo DataFrame llamado df_filtrado. Luego, calcula la media de la columna "puntaje" del DataFrame original y lo guarda en media_puntaje. Finalmente, se imprime la media de la columna "puntaje" con print().

# Pregunta

- Hazme una explicacion con ejemplos de  Manipulación de datos: Uso de librerías como NumPy y Pandas para trabajar con arreglos y conjuntos de datos en python
