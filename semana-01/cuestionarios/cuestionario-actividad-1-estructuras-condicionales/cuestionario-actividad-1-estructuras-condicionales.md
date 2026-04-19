# Cuestionario de Actividad 1 - Estructuras Condicionales

**Materia:** Programación 1
**Módulo:** Unidad 2 - Estructuras Condicionales
**Tema evaluado:** Operadores relacionales en Python
**Resultado:** 5/5 (100%) ✓

---

## Pregunta 1

**Complete el código para que la salida sea `True` y `True`:**

```python
palabra1 = "hola"
palabra2 = "gracias"
palabra3 = "Casa"
palabra4 = "casa"

print(palabra1 ___ palabra2)   # True
print(palabra3 ___ palabra4)   # True
```

**Opciones:** `<`, `>`, `==`

### Respuestas

| # | Operador | Expresión | Resultado |
|---|----------|-----------|-----------|
| Respuesta 1 | **`>`** | `"hola" > "gracias"` | `True` |
| Respuesta 2 | **`<`** | `"Casa" < "casa"` | `True` |

### Justificación

Python compara strings carácter por carácter usando los **valores Unicode** (que para los caracteres básicos coinciden con ASCII).

- **Respuesta 1:** se compara la primera letra. `'h'` (Unicode 104) vs `'g'` (Unicode 103). Como `104 > 103`, entonces `"hola" > "gracias"` es `True`.
- **Respuesta 2:** las **mayúsculas tienen códigos más bajos** que las minúsculas. `'C'` (Unicode 67) vs `'c'` (Unicode 99). Como `67 < 99`, entonces `"Casa" < "casa"` es `True`.

---

## Pregunta 2

**Complete el código para que la salida sea `True` y `False`:**

```python
c = 1
d = 5

print(d ___ c)   # True
print(c ___ d)   # False
```

**Opciones:** `<=`, `!=`, `==`

### Respuestas

| # | Operador | Expresión | Resultado |
|---|----------|-----------|-----------|
| Respuesta 1 | **`!=`** | `5 != 1` | `True` |
| Respuesta 2 | **`==`** | `1 == 5` | `False` |

### Justificación

- **Respuesta 1:** `5 != 1` es `True` porque 5 es distinto de 1. (`5 <= 1` daría `False`, `5 == 1` daría `False`.)
- **Respuesta 2:** `1 == 5` es `False` porque 1 no es igual a 5. (`1 <= 5` daría `True`, `1 != 5` daría `True`.)

---

## Pregunta 3

**Coloque "Verdadero" o "Falso" según el valor de cada comparación:**

| # | Comparación | Respuesta | Justificación |
|---|-------------|-----------|---------------|
| 1 | `1 != 0` | **Verdadero** | 1 es distinto de 0 |
| 2 | `1 == 0` | **Falso** | 1 no es igual a 0 |
| 3 | `-130 > 0` | **Falso** | Cualquier número negativo es menor que 0 |
| 4 | `-400 < -250` | **Verdadero** | -400 está más a la izquierda en la recta numérica que -250 |
| 5 | `"hola" >= "chau"` | **Verdadero** | `'h'` (Unicode 104) > `'c'` (Unicode 99) |

> 💡 **Tip números negativos:** pensalos como temperaturas. -400 °C es más frío (más bajo) que -250 °C, por eso `-400 < -250`.

---

## Pregunta 4

**¿Cómo compara Python 2 strings haciendo uso de operadores relacionales mayor que, menor que, mayor o igual que y menor o igual que?**

- [ ] a. Los ordena según el código ASCII y los compara según el orden resultante. ✓
- [ ] b. Los ordena según el nombre de la variable y los compara según el orden resultante.
- [ ] c. Los ordena por orden alfabético y los compara según el orden resultante.
- [ ] d. No se puede comparar dos strings con los operadores mencionados en Python.

### Respuesta correcta: **a**

### Justificación

Python compara strings **carácter por carácter** (lexicográficamente) usando el **valor Unicode** de cada carácter (que para los caracteres básicos del inglés coincide con el código **ASCII**).

```python
"abc" < "abd"    # True  → 'c' (99) < 'd' (100)
"Casa" < "casa"  # True  → 'C' (67) < 'c' (99)
"hola" > "chau"  # True  → 'h' (104) > 'c' (99)
```

**Por qué las otras son incorrectas:**

- **b.** ❌ Python no mira el **nombre** de la variable, sino su **contenido**.
- **c.** ❌ El "orden alfabético" humano no distingue mayúsculas/minúsculas; Python sí: para Python `"Z" < "a"` es `True` porque compara códigos numéricos, no alfabeto.
- **d.** ❌ Falso: los strings sí se pueden comparar con `<`, `>`, `<=`, `>=`, `==`, `!=`.

> 💡 Estrictamente Python usa **Unicode** (no solo ASCII), pero ASCII es un subconjunto de Unicode y los códigos coinciden para los primeros 128 caracteres. La opción **a** es la única conceptualmente correcta entre las cuatro.

---

## Pregunta 5

**¿Cuál de las siguientes afirmaciones NO es cierta sobre los operadores relacionales de Python?**

- [ ] a. Siempre retornan un booleano.
- [ ] b. Sirven para comparar dos variables.
- [ ] c. Es posible aplicarlos para comparar strings.
- [ ] d. Se pueden aplicar únicamente para comparar dos variables numéricas. ✓

### Respuesta correcta: **d**

### Justificación

Los operadores relacionales en Python (`==`, `!=`, `<`, `>`, `<=`, `>=`) **no se limitan a números**. También se pueden usar con:

- **Strings** (orden lexicográfico por código Unicode): `"hola" > "chau"` → `True`
- **Listas y tuplas** (comparan elemento por elemento): `[1, 2] < [1, 3]` → `True`
- **Booleanos**: `True > False` → `True`
- **Conjuntos** (subconjunto / superconjunto): `{1, 2} < {1, 2, 3}` → `True`

**Por qué las otras SÍ son ciertas:**

| Opción | Afirmación | Justificación |
|--------|-----------|---------------|
| **a** | Siempre retornan un booleano | Devuelven `True` o `False` |
| **b** | Sirven para comparar dos variables | Es exactamente su propósito |
| **c** | Es posible aplicarlos para comparar strings | Lo vimos en preguntas anteriores: `"hola" > "chau"` funciona |

> 💡 **Tip de cuestionarios:** cuando aparecen palabras como **"únicamente"**, **"siempre"** o **"nunca"**, sospechá. Suelen ser las afirmaciones falsas porque imponen una restricción que el lenguaje no tiene.

---

## Resumen del cuestionario

| Pregunta | Tema | Respuesta | Estado |
|----------|------|-----------|--------|
| 1 | Comparación de strings | `>` y `<` | ✓ |
| 2 | Comparación numérica | `!=` y `==` | ✓ |
| 3 | Valor de verdad de 5 expresiones | V, F, F, V, V | ✓ |
| 4 | Cómo compara Python los strings | a (código ASCII/Unicode) | ✓ |
| 5 | Afirmación falsa sobre relacionales | d (no se limitan a numéricas) | ✓ |

**Total:** 5/5 - 100% ✓

---

## Conceptos clave repasados

### Operadores relacionales en Python

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Distinto de | `5 != 3` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<=` | Menor o igual que | `5 <= 5` | `True` |
| `>=` | Mayor o igual que | `5 >= 3` | `True` |

### Comparación de strings (orden lexicográfico)

- Se comparan **carácter por carácter** usando el **código Unicode** (compatible con ASCII para caracteres básicos).
- Mayúsculas (`A-Z`: 65-90) son **menores** que minúsculas (`a-z`: 97-122).
- Reglas útiles: `"A" < "Z" < "a" < "z"`.

### Funcionan también con

- Listas y tuplas (elemento a elemento)
- Booleanos (`False = 0`, `True = 1`)
- Conjuntos (subconjunto/superconjunto)

---

*Cuestionario - Unidad 2 - Programación 1 - Tecnicatura UTN 2026*
