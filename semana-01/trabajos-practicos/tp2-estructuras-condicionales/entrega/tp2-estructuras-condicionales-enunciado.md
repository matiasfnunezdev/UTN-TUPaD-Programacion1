# Trabajo Práctico N.º 2: Estructuras Condicionales

**Materia:** Programación 1
**Carrera:** Tecnicatura Universitaria en Programación a Distancia
**Semana:** 01
**Unidad:** 2 - Estructuras Condicionales

## Objetivo

Comprender y aplicar las estructuras condicionales en la programación, desarrollando algoritmos que involucren tomas de decisiones.

## Resultados de aprendizaje

1. **Comprensión y aplicación de estructuras de control:** identificar y utilizar estructuras condicionales simples (`if-else`) y compuestas (`if-elif-else`) para controlar el flujo de un programa y tomar decisiones basadas en condiciones lógicas.
2. **Diseño y desarrollo de algoritmos con estructuras de control:** diseñar y desarrollar algoritmos que involucren estructuras condicionales anidadas para resolver problemas que requieran tomar decisiones basadas en múltiples condiciones.
3. **Resolución de problemas y pensamiento crítico:** analizar problemas, descomponerlos en subproblemas más sencillos y diseñar algoritmos eficientes para resolverlos.

## Actividades

1. Escribir un programa que solicite la **edad** del usuario. Si el usuario es **mayor de 18 años**, deberá mostrar un mensaje en pantalla que diga `Es mayor de edad`.

2. Escribir un programa que solicite su **nota** al usuario. Si la nota es **mayor o igual a 6**, deberá mostrar por pantalla un mensaje que diga `Aprobado`; en caso contrario deberá mostrar el mensaje `Desaprobado`.

3. Escribir un programa que permita ingresar **solo números pares**. Si el usuario ingresa un número par, imprimir el mensaje `Ha ingresado un número par`; en caso contrario, imprimir `Por favor, ingrese un número par`.
   > **Nota:** investigar el uso del operador de módulo (`%`) en Python para evaluar si un número es par o impar.

4. Escribir un programa que solicite al usuario su **edad** e imprima por pantalla a cuál de las siguientes categorías pertenece:
   - **Niño/a:** menor de 12 años.
   - **Adolescente:** mayor o igual que 12 años y menor que 18 años.
   - **Adulto/a joven:** mayor o igual que 18 años y menor que 30 años.
   - **Adulto/a:** mayor o igual que 30 años.

5. Escribir un programa que permita introducir **contraseñas de entre 8 y 14 caracteres** (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir el mensaje `Ha ingresado una contraseña correcta`; en caso contrario, imprimir `Por favor, ingrese una contraseña de entre 8 y 14 caracteres`.
   > **Nota:** investigue el uso de la función `len()` en Python para evaluar la cantidad de elementos que tiene un iterable.

6. Escribir un programa que solicite al usuario el **consumo mensual de energía eléctrica en kilovatios (kWh)** e indique la categoría del consumo según el siguiente criterio:
   - **Menor que 150 kWh:** `Consumo bajo`.
   - **Entre 150 y 300 kWh (inclusive):** `Consumo medio`.
   - **Mayor que 300 kWh:** `Consumo alto`.

   Además, si el consumo supera los **500 kWh**, mostrar un mensaje adicional que diga: `Considere medidas de ahorro energético`.

7. Escribir un programa que solicite una **frase o palabra** al usuario. Si el string ingresado **termina con vocal**, añadir un signo de exclamación al final e imprimir el resultado; en caso contrario, dejar el string tal cual e imprimirlo.

8. Escribir un programa que solicite al usuario que ingrese su **nombre** y el número **1, 2 o 3** dependiendo de la opción que desee:
   1. Si quiere su nombre en **mayúsculas** (Ejemplo: `PEDRO`).
   2. Si quiere su nombre en **minúsculas** (Ejemplo: `pedro`).
   3. Si quiere su nombre con la **primera letra mayúscula** (Ejemplo: `Pedro`).

   El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada e imprimir el resultado.
   > **Nota:** investigue el uso de las funciones `upper()`, `lower()` y `title()` de Python.

9. Escribir un programa que pida al usuario la **magnitud de un terremoto**, clasifique la magnitud según la escala de Richter e imprima el resultado:
   - **Menor que 3:** `Muy leve` (imperceptible).
   - **3 ≤ magnitud < 4:** `Leve` (ligeramente perceptible).
   - **4 ≤ magnitud < 5:** `Moderado` (sentido por personas, pero generalmente no causa daños).
   - **5 ≤ magnitud < 6:** `Fuerte` (puede causar daños en estructuras débiles).
   - **6 ≤ magnitud < 7:** `Muy Fuerte` (puede causar daños significativos).
   - **Mayor o igual que 7:** `Extremo` (puede causar graves daños a gran escala).

10. Escribir un programa que pregunte al usuario en cuál **hemisferio** se encuentra (`N`/`S`), qué **mes** del año es y qué **día** es. El programa deberá utilizar esa información para imprimir si el usuario se encuentra en **otoño**, **invierno**, **primavera** o **verano**.

    **Tabla de estaciones (referencia astronómica):**

    | Período | Hemisferio Norte | Hemisferio Sur |
    |---------|------------------|----------------|
    | 21 marzo - 20 junio | Primavera | Otoño |
    | 21 junio - 22 septiembre | Verano | Invierno |
    | 23 septiembre - 20 diciembre | Otoño | Primavera |
    | 21 diciembre - 20 marzo | Invierno | Verano |

---

## Sugerencia

Resolver primero los ejercicios por cuenta propia y luego comparar las respuestas con las soluciones propuestas. **No existe una única forma de resolver un problema.**
