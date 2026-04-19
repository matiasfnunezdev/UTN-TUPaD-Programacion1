# TP2 - Estructuras Condicionales

**Materia:** Programación 1
**Semana:** 01
**Unidad:** 2 - Estructuras Condicionales

## Contenido

| Archivo | Descripción |
|---------|-------------|
| [`tp2-estructuras-condicionales-enunciado.md`](./tp2-estructuras-condicionales-enunciado.md) | Enunciado del trabajo práctico |
| [`ejercicio-01.py`](./ejercicio-01.py) | Mayor de edad (`if` simple) |
| [`ejercicio-02.py`](./ejercicio-02.py) | Aprobado / Desaprobado (`if/else`) |
| [`ejercicio-03.py`](./ejercicio-03.py) | Número par o impar (operador `%`) |
| [`ejercicio-04.py`](./ejercicio-04.py) | 4 categorías de edad (`if/elif/else`) |
| [`ejercicio-05.py`](./ejercicio-05.py) | Validación de contraseña (función `len()`) |
| [`ejercicio-06.py`](./ejercicio-06.py) | Consumo eléctrico + advertencia de ahorro |
| [`ejercicio-07.py`](./ejercicio-07.py) | Frase que termina en vocal |
| [`ejercicio-08.py`](./ejercicio-08.py) | Transformación de nombre (`upper()`, `lower()`, `title()`) |
| [`ejercicio-09.py`](./ejercicio-09.py) | Magnitud de terremoto (escala de Richter) |
| [`ejercicio-10.py`](./ejercicio-10.py) | Estación del año (hemisferio, mes, día) |

## Cómo ejecutar los ejercicios individuales

Desde esta carpeta, en la terminal:

```bash
python ejercicio-01.py
```

Reemplazar `01` por el número del ejercicio que se quiera ejecutar (`01` a `10`).

## Entrega final

La carpeta [`entrega/`](./entrega/) contiene el **proyecto completo** para subir al aula virtual.

A diferencia del TP1, esta consigna pide comprimir **todo el proyecto** (no solo el `.py`).

| Archivo dentro de la carpeta `entrega/` | Descripción |
|---------|-------------|
| [`tp2-estructuras-condicionales.py`](./entrega/tp2-estructuras-condicionales.py) | Código fuente con los 10 ejercicios y menú interactivo |
| [`tp2-estructuras-condicionales-enunciado.md`](./entrega/tp2-estructuras-condicionales-enunciado.md) | Enunciado del trabajo práctico |
| [`README.md`](./entrega/README.md) | Instrucciones de ejecución del proyecto |
| [`tp2-estructuras-condicionales.zip`](./entrega/tp2-estructuras-condicionales.zip) | ⭐ **Proyecto comprimido listo para subir al aula virtual** |

El `.zip` incluye los 3 archivos del proyecto (código + enunciado + README).

Para ejecutar el proyecto:

```bash
cd entrega
python tp2-estructuras-condicionales.py
```

El programa muestra un menú del 1 al 10 para elegir qué ejercicio ejecutar (0 para salir).

## Conceptos aplicados

- **Estructuras condicionales:** `if`, `if/else`, `if/elif/else`.
- **Operadores relacionales:** `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Operadores lógicos:** `and`, `or`, `not`.
- **Operadores aritméticos:** `%` (módulo) para detectar paridad.
- **Funciones de string:** `upper()`, `lower()`, `title()`, indexado `[-1]`.
- **Función `len()`** para validar longitud de un string.
- **Operador `in`** para chequear pertenencia a un conjunto de caracteres (vocales).

## Requisitos

- Python 3.x
