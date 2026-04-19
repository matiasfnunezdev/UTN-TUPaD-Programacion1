# Trabajo Práctico Integrador 5: Listas

**Materia:** Programación 1
**Carrera:** Tecnicatura Universitaria en Programación a Distancia
**Unidad:** 5 - Listas

## Objetivo

Desarrollar la comprensión y la capacidad de manipular **listas en Python** mediante la aplicación de conceptos fundamentales como **indexación**, **modificación de elementos**, **uso de métodos integrados** y **manejo de listas anidadas**.

## Resultados de aprendizaje

1. Reconocer y aplicar correctamente la **indexación y el slicing** para acceder a elementos individuales o subconjuntos dentro de una lista.
2. Utilizar los **métodos básicos** de listas para crear, modificar y gestionar estructuras de datos simples.
3. Modificar listas mediante la actualización de valores y el manejo de **listas anidadas**, comprendiendo cómo acceder a datos en estructuras más complejas.

> ⚠️ **Nota general:** siempre que se pida mostrar una lista o sus elementos, utilizar **estructuras repetitivas** (`for`, `while`).

---

## Actividades

### 1) Notas de 10 estudiantes

Crear una lista con las notas de 10 estudiantes.
- Mostrar la lista completa.
- Calcular y mostrar el promedio.
- Indicar la nota más alta y la más baja.

### 2) 5 productos

Pedir al usuario que cargue 5 productos en una lista.
- Mostrar la lista ordenada alfabéticamente (investigar `sorted()`).
- Preguntar al usuario qué producto desea eliminar y actualizar la lista.

### 3) 15 números aleatorios entre 1 y 100

Generar una lista con 15 enteros al azar entre 1 y 100.
- Crear una lista con los pares y otra con los impares.
- Mostrar cuántos números tiene cada lista.

### 4) Sin duplicados

Dada una lista con valores repetidos:
- Crear una nueva lista sin elementos repetidos.
- Mostrar el resultado.

### 5) Estudiantes presentes

Crear una lista con los nombres de 8 estudiantes.
- Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
- Mostrar la lista final actualizada.

### 6) Rotación a la derecha

Dada una lista con 7 números, rotar todos los elementos **una posición hacia la derecha** (el último pasa a ser el primero).

### 7) Temperaturas semanales (matriz 7x2)

Crear una matriz (lista anidada) de **7×2** con las temperaturas mínimas y máximas de una semana.
- Calcular el promedio de las mínimas y el de las máximas.
- Mostrar en qué día se registró la **mayor amplitud térmica**.

### 8) Notas de 5 estudiantes en 3 materias (matriz 5x3)

Crear una matriz con las notas de 5 estudiantes en 3 materias.
- Mostrar el promedio de cada estudiante.
- Mostrar el promedio de cada materia.

### 9) Tablero de Ta-Te-Ti

Representar un tablero como lista de listas (3×3).
- Inicializar con guiones `"-"` para casillas vacías.
- Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar `"X"` o `"O"`.
- Mostrar el tablero después de cada jugada.

### 10) Ventas de 4 productos en 7 días (matriz 4x7)

Una tienda registra las ventas de 4 productos durante 7 días.
- Mostrar el total vendido por cada producto.
- Mostrar el día con mayores ventas totales.
- Indicar cuál fue el producto más vendido en la semana.

### 11) Buscar nombre

Crear una lista con los nombres de 10 estudiantes.
- Solicitar al usuario que ingrese un nombre a buscar.
- Indicar si el nombre se encuentra en la lista.
- Mostrar la posición en la que aparece.
- Si no se encuentra, informar que no está en la lista.

### 12) Ordenar 8 enteros

Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
- Mostrar la lista original.
- Mostrar la lista ordenada de menor a mayor.
- Mostrar la lista ordenada de mayor a menor.
- Investigar el uso de `sorted()` y del parámetro `reverse`.

### 13) Ranking de puntajes

Dada la siguiente lista de puntajes de un videojuego:

```python
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
```

- Mostrar el puntaje más alto y el más bajo.
- Mostrar la lista ordenada de mayor a menor (ranking).
- Indicar en qué posición del ranking se encuentra el puntaje **990**.
