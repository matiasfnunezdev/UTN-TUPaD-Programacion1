# TP Integrador - Estructuras Repetitivas, Condicionales y Secuenciales

**Materia:** Programación 1 · **Unidad:** 3 · **Semana:** 01

## Estructura

```
tp3-integrador-estructuras-repetitivas/
├── tp3-integrador-estructuras-repetitivas-enunciado.md   # Enunciado completo
├── ejercicio-01.py     # Caja del Kiosco
├── ejercicio-02.py     # Acceso al Campus y Menú Seguro
├── ejercicio-03.py     # Agenda de Turnos (sin listas)
├── ejercicio-04.py     # Escape Room: La Bóveda
├── ejercicio-05.py     # Arena del Gladiador
├── README.md           # Este archivo
└── entrega/
    ├── tp3-integrador-estructuras-repetitivas.py        # Consolidado con menú
    ├── tp3-integrador-estructuras-repetitivas-enunciado.md
    ├── README.md                                        # Instrucciones de uso
    └── tp3-integrador-estructuras-repetitivas.zip       # Archivo final a subir
```

## Ejercicios

| # | Título | Conceptos clave |
|---|--------|------------------|
| 1 | [Caja del Kiosco](./ejercicio-01.py) | `for` + validaciones `.isalpha()` y `.isdigit()` |
| 2 | [Acceso al Campus](./ejercicio-02.py) | login con intentos + menú con `while` |
| 3 | [Agenda de Turnos sin listas](./ejercicio-03.py) | menú repetitivo con variables individuales |
| 4 | [Escape Room: La Bóveda](./ejercicio-04.py) | mecánica con anti-spam, `for`, alarma |
| 5 | [Arena del Gladiador](./ejercicio-05.py) | combate por turnos, tipado int/float/str/bool |

## Cómo ejecutar un ejercicio individual

```bash
python ejercicio-01.py
```

## Cómo ejecutar todos juntos (consolidado)

```bash
cd entrega
python tp3-integrador-estructuras-repetitivas.py
```

## Entrega

El archivo final para subir al aula virtual es:

[`entrega/tp3-integrador-estructuras-repetitivas.zip`](./entrega/tp3-integrador-estructuras-repetitivas.zip)

Contiene:
- El código consolidado con menú interactivo (`.py`)
- El enunciado del TP (`.md`)
- Un README con instrucciones de ejecución

## Restricciones cumplidas

- ❌ Sin `try`/`except`.
- ✅ Validaciones con `.isalpha()` y `.isdigit()` dentro de `while`.
- ✅ Estructuras secuenciales, condicionales y repetitivas (`while`/`for`).
- ✅ Ejercicio 3: sin listas, diccionarios, sets ni tuplas.
- ✅ Ejercicio 5: uso explícito de `int`, `float`, `str` y `bool`.
