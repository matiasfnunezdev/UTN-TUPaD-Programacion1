# TP2 - Estructuras Condicionales

**Materia:** Programación 1
**Carrera:** Tecnicatura Universitaria en Programación a Distancia
**Semana:** 01
**Unidad:** 2 - Estructuras Condicionales
**Alumno:** Matias Fernando Nuñez

## Contenido del proyecto

| Archivo | Descripción |
|---------|-------------|
| `tp2-estructuras-condicionales.py` | Código fuente con los 10 ejercicios resueltos y un menú interactivo |
| `tp2-estructuras-condicionales-enunciado.md` | Enunciado original del trabajo práctico |
| `README.md` | Este archivo (instrucciones de ejecución) |

## Cómo ejecutar el proyecto

### Requisitos

- **Python 3.x** instalado (recomendado 3.10 o superior).
- Una terminal con soporte UTF-8 (PowerShell, terminal de VSCode, IDLE, etc.).

### Ejecución

Desde una terminal posicionada en esta carpeta:

```bash
python tp2-estructuras-condicionales.py
```

El programa muestra un **menú interactivo** del 1 al 10. Ingresar el número del ejercicio que se quiere ejecutar (o `0` para salir).

```
============================================================
  TP2 - Estructuras Condicionales - Programación 1
============================================================
   1. Mayor de edad
   2. Aprobado / Desaprobado
   3. Número par o impar
   4. Categorías de edad
   5. Validación de contraseña (8-14 caracteres)
   6. Consumo eléctrico
   7. Frase que termina en vocal
   8. Transformación de nombre (upper/lower/title)
   9. Magnitud de terremoto (escala de Richter)
  10. Estación del año (hemisferio, mes, día)
   0. Salir
============================================================
Elegí un ejercicio (0 para salir):
```

## Ejercicios resueltos

| # | Ejercicio | Concepto principal |
|---|-----------|--------------------|
| 1 | Mayor de edad | `if` simple |
| 2 | Aprobado / Desaprobado | `if/else` |
| 3 | Número par o impar | Operador módulo (`%`) |
| 4 | Categorías de edad (4 rangos) | `if/elif/else` |
| 5 | Validación de contraseña (8-14 caracteres) | Función `len()` y comparación encadenada |
| 6 | Consumo eléctrico + advertencia de ahorro | `if/elif/else` + `if` adicional |
| 7 | Frase que termina en vocal | Indexado `[-1]`, `lower()` y `in` |
| 8 | Transformación de nombre | `upper()`, `lower()`, `title()` |
| 9 | Magnitud de terremoto (Richter) | `if/elif/else` con 6 ramas |
| 10 | Estación del año (hemisferio, mes, día) | Condicionales anidadas |
