# Cuestionario de Actividad 2 - Operadores Lógicos

**Materia:** Programación 1
**Módulo:** Unidad 2 - Estructuras Condicionales
**Tema evaluado:** Operadores lógicos en Python (`and`, `or`, `not`)
**Resultado:** 5/5 (100%) ✓

---

## Pregunta 1

**Complete el código para que la salida sea `False` y `True`:**

```python
x = 10 > 5     # True
y = 3 == 4     # False
z = 7 <= 7     # True

print(not (x ___ y))         # False
print((x ___ y) and z)       # True
```

**Opciones:**
- Respuesta 1: `==`, `or`, `and`
- Respuesta 2: `and`, `or`, `==`

### Respuestas

| # | Operador | Expresión | Resultado |
|---|----------|-----------|-----------|
| Respuesta 1 | **`or`** | `not (True or False)` → `not True` | `False` ✓ |
| Respuesta 2 | **`or`** | `(True or False) and True` → `True and True` | `True` ✓ |

### Justificación

Primero calculo las variables:
- `x = 10 > 5` → `True`
- `y = 3 == 4` → `False`
- `z = 7 <= 7` → `True`

**Pregunta 1 - Respuesta 1** (debe dar `False`):

| Operador | Cálculo | Resultado |
|----------|---------|-----------|
| `not (x == y)` | `not (True == False)` → `not False` | `True` ❌ |
| **`not (x or y)`** | `not (True or False)` → `not True` | **`False`** ✓ |
| `not (x and y)` | `not (True and False)` → `not False` | `True` ❌ |

**Pregunta 1 - Respuesta 2** (debe dar `True`):

| Operador | Cálculo | Resultado |
|----------|---------|-----------|
| `(x and y) and z` | `(True and False) and True` → `False` | `False` ❌ |
| **`(x or y) and z`** | `(True or False) and True` → `True` | **`True`** ✓ |
| `(x == y) and z` | `(True == False) and True` → `False` | `False` ❌ |

---

## Pregunta 2

**Complete el código para que la salida sea `Puede conducir ambulancias` con las entradas `edad = 22` y `categoria = "d"`:**

```python
EDAD_MINIMA = ___

edad = int(input("Ingrese su edad: "))
categoria = input("Ingrese su categoría (A, B, C, D, E, F, G): ")

if edad >= EDAD_MINIMA and (categoria == "D" ___ categoria == "d"):
    print("Puede conducir ambulancias")
else:
    print("No puede conducir ambulancias")
```

**Opciones:**
- Respuesta 1: `25`, `21`, `30`
- Respuesta 2: `or`, `not`, `and`

### Respuestas

| # | Valor | Justificación |
|---|-------|---------------|
| Respuesta 1 | **`21`** | En Argentina la edad mínima para la categoría D (ambulancias, taxis, transporte de pasajeros) es 21 años. Con `EDAD_MINIMA = 21`: `22 >= 21` → `True` ✓ |
| Respuesta 2 | **`or`** | Como el usuario ingresa `"d"` (minúscula), hay que aceptar ambas variantes: `(False or True)` → `True` ✓ |

### Justificación detallada

**Respuesta 1** - Análisis de cada opción con `edad = 22`:

| Valor | `22 >= EDAD_MINIMA` | ¿Pasa? |
|-------|---------------------|--------|
| 25 | `22 >= 25` → `False` | ❌ |
| **21** | `22 >= 21` → `True` | ✓ |
| 30 | `22 >= 30` → `False` | ❌ |

**Respuesta 2** - Análisis con `categoria = "d"`:

| Operador | Cálculo | Resultado |
|----------|---------|-----------|
| **`or`** | `False or True` | **`True`** ✓ |
| `not` | `False not True` | ❌ Error de sintaxis |
| `and` | `False and True` | `False` ❌ |

### Código final funcionando

```python
EDAD_MINIMA = 21

edad = int(input("Ingrese su edad: "))
categoria = input("Ingrese su categoría (A, B, C, D, E, F, G): ")

if edad >= EDAD_MINIMA and (categoria == "D" or categoria == "d"):
    print("Puede conducir ambulancias")
else:
    print("No puede conducir ambulancias")
```

**Ejecución:**
```
Ingrese su edad: 22
Ingrese su categoría (A, B, C, D, E, F, G): d
Puede conducir ambulancias
```

---

## Pregunta 3

**Coloque "True" o "False" según el valor de verdad de cada expresión, sabiendo que `a = True` y `b = False`:**

| # | Expresión | Cálculo paso a paso | Resultado |
|---|-----------|---------------------|-----------|
| 1 | `a and b` | `True and False` | **`False`** |
| 2 | `a or b` | `True or False` | **`True`** |
| 3 | `not a` | `not True` | **`False`** |
| 4 | `not a or b` | `(not True) or False` → `False or False` | **`False`** |
| 5 | `not (a or b)` | `not (True or False)` → `not True` | **`False`** |
| 6 | `not a or (b or a)` | `(not True) or (False or True)` → `False or True` | **`True`** |

### Resumen

| Pregunta | Respuesta |
|----------|-----------|
| Respuesta 1 (`a and b`) | **False** |
| Respuesta 2 (`a or b`) | **True** |
| Respuesta 3 (`not a`) | **False** |
| Respuesta 4 (`not a or b`) | **False** |
| Respuesta 5 (`not (a or b)`) | **False** |
| Respuesta 6 (`not a or (b or a)`) | **True** |

### Concepto clave: precedencia

Recordá que la **precedencia** es: **`not` > `and` > `or`**.

```python
not a or b      # → (not a) or b      (no es: not (a or b))
```

Para negar una expresión completa hay que usar paréntesis: `not (a or b)`.

---

## Pregunta 4

**Indique si las siguientes afirmaciones son verdaderas o falsas:**

| # | Afirmación | Respuesta | Justificación |
|---|------------|-----------|---------------|
| 1 | Para que la **conjunción** sea verdadera, basta con que una de las variables sea verdadera | **Falso** | La conjunción (`and`) requiere que **TODAS** las variables sean verdaderas. Si una sola es falsa, el resultado es `False`. |
| 2 | Para que la **disyunción** sea verdadera, basta con que una de las variables sea verdadera | **Verdadero** | La disyunción (`or`) devuelve `True` si **al menos una** variable es verdadera. |
| 3 | El operador `not` invierte el valor de verdad de una variable booleana | **Verdadero** | `not True` → `False` y `not False` → `True`. |

### Aclaración

La afirmación 1 describe el comportamiento de la **disyunción** (`or`), no de la conjunción. Es un clásico "trampa" de cuestionarios.

| Operador | Nombre | Es verdadero cuando... |
|----------|--------|------------------------|
| **`and`** | **Conjunción** | **Todas** las condiciones son verdaderas |
| **`or`** | **Disyunción** | **Al menos una** condición es verdadera |
| **`not`** | **Negación** | Invierte el valor (`True` ↔ `False`) |

> 💡 **Regla mnemotécnica:**
> - **Y** (conjunción `and`) → exige **todo** ("café **y** medialunas" requiere las dos cosas).
> - **O** (disyunción `or`) → se conforma con **uno** ("café **o** té" alcanza con una bebida).

---

## Pregunta 5

**¿Cuál de las siguientes afirmaciones NO es cierta sobre los operadores lógicos de Python?**

- [ ] a. Los operadores `and` y `or` se usan para comparar dos variables. El operador `not` solo requiere de una variable.
- [ ] b. Están basados en la lógica proposicional.
- [x] **c. Todos los operadores lógicos se usan para comparar dos variables.** ✓
- [ ] d. Siempre retornan un booleano.

### Respuesta correcta: **c**

### Justificación

Los operadores lógicos en Python **no todos** son binarios. Específicamente:

| Operador | Tipo | Cantidad de operandos |
|----------|------|----------------------|
| `and` | **Binario** | 2 (`a and b`) |
| `or` | **Binario** | 2 (`a or b`) |
| `not` | **Unario / monádico** | **1** (`not a`) |

El operador **`not`** es **unario**: opera sobre un solo valor booleano, no compara dos. Por eso la afirmación "todos los operadores lógicos se usan para comparar dos variables" es **falsa**.

### Por qué las otras SÍ son ciertas

| Opción | Afirmación | Justificación |
|--------|-----------|---------------|
| **a** | `and` y `or` se usan con dos variables; `not` solo requiere una | ✅ Describe exactamente la cantidad de operandos de cada uno. |
| **b** | Están basados en la lógica proposicional | ✅ Provienen del **álgebra de Boole** y la **lógica proposicional**. |
| **d** | Siempre retornan un booleano | ✅ El resultado es siempre `True` o `False`. |

### Truco de detección

Las opciones **a** y **c** son **contradictorias** entre sí:
- **a** dice que `not` solo requiere una variable.
- **c** dice que **todos** los operadores comparan dos variables.

Cuando dos opciones se contradicen, una de las dos es la respuesta. Como **a** es técnicamente correcta, **c** es la falsa.

---

## Resumen del cuestionario

| Pregunta | Tema | Respuesta | Estado |
|----------|------|-----------|--------|
| 1 | Operadores lógicos en expresiones (`or` para dos huecos) | `or` y `or` | ✓ |
| 2 | Aplicación práctica (categoría D - ambulancias) | `21` y `or` | ✓ |
| 3 | Tablas de verdad de 6 expresiones lógicas | F, V, F, F, F, V | ✓ |
| 4 | Afirmaciones sobre conjunción, disyunción y negación | F, V, V | ✓ |
| 5 | Afirmación falsa sobre operadores lógicos | c (no todos son binarios) | ✓ |

**Total:** 5/5 - 100% ✓

---

## Conceptos clave repasados

### Operadores lógicos

| Operador | Tipo | Verdadero cuando... |
|----------|------|---------------------|
| **`and`** (conjunción) | Binario | **Todas** las condiciones son `True` |
| **`or`** (disyunción) | Binario | **Al menos una** condición es `True` |
| **`not`** (negación) | Unario | Invierte el valor (`True` ↔ `False`) |

### Precedencia

`not` > `and` > `or`

Para alterar el orden o mejorar legibilidad → **paréntesis**.

### Diferencia entre `not a or b` y `not (a or b)`

```python
a = True
b = False

not a or b      # → (not a) or b → False or False → False
not (a or b)    # → not (a or b) → not True       → False

# Caso donde sí difieren:
b = True
not a or b      # → False or True → True
not (a or b)    # → not True      → False
```

### Aplicación práctica

```python
# Validar acceso de un usuario:
if edad >= 18 and registrado:
    print("Acceso permitido")

# Aceptar mayúsculas o minúsculas en la entrada:
if categoria == "D" or categoria == "d":
    ...

# Negar una condición:
if not es_invitado:
    print("Bienvenido usuario registrado")
```

---

*Cuestionario - Unidad 2 - Programación 1 - Tecnicatura UTN 2026*
