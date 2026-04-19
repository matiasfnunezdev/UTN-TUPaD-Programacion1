# UTN-TUPaD-Programacion1

Repositorio de la materia **Programación 1** de la **Tecnicatura Universitaria en Programación a Distancia (TUPaD)** de la **Universidad Tecnológica Nacional (UTN)**.

> Año académico: **2026** · Estudiante: **Matías Núñez**

## Contenido por unidades

| Unidad | Tema | Estado |
|--------|------|--------|
| 1 | Estructuras Secuenciales | ✓ Completa |
| 2 | Estructuras Condicionales (operadores relacionales y lógicos) | ✓ Completa |
| 3 | Estructuras Repetitivas (`while` y `for`) | ✓ Completa |
| 4 | Trabajo colaborativo con Git y GitHub | ✓ Completa (este repositorio) |
| 5 | Listas (indexación, slicing, métodos, listas anidadas) | ✓ Completa |

## Estructura del repositorio

```
UTN-TUPaD-Programacion1/
├── README.md                                 # Este archivo
└── semana-01/
    ├── apuntes/                              # Material teórico (PDFs, notebooks, .md)
    │   ├── unidad-2-estructuras-condicionales.md
    │   ├── unidad-2-operadores-logicos.md
    │   └── ... (PDFs y notebooks de la cátedra)
    ├── cuestionarios/                        # Respuestas y justificaciones
    │   ├── cuestionario-actividad-1-estructuras-condicionales/
    │   └── cuestionario-actividad-2-operadores-logicos/
    └── trabajos-practicos/                   # Resoluciones de TPs
        ├── tp1-estructuras-secuenciales/
        ├── tp2-estructuras-condicionales/
        ├── tp3-integrador-estructuras-repetitivas/
        └── tp5-integrador-listas/
```

## Trabajos prácticos incluidos

### TP1 - Estructuras Secuenciales (Unidad 1)
10 ejercicios de entrada/salida, operaciones aritméticas y manipulación básica de variables.
📁 [`semana-01/trabajos-practicos/tp1-estructuras-secuenciales/`](./semana-01/trabajos-practicos/tp1-estructuras-secuenciales/)

### TP2 - Estructuras Condicionales (Unidad 2)
10 ejercicios con `if`, `elif`, `else`, operadores relacionales y lógicos.
📁 [`semana-01/trabajos-practicos/tp2-estructuras-condicionales/`](./semana-01/trabajos-practicos/tp2-estructuras-condicionales/)

### TP3 Integrador - Estructuras Repetitivas (Unidad 3)
5 ejercicios complejos que integran secuenciales, condicionales y repetitivas:
1. Caja del Kiosco — validaciones con `.isalpha()` / `.isdigit()` y `for`
2. Acceso al Campus + Menú Seguro — login con intentos limitados
3. Agenda de Turnos sin listas — manejo con variables individuales
4. Escape Room: La Bóveda — mecánica de juego con anti-spam
5. Arena del Gladiador — combate por turnos con tipado int/float/str/bool

📁 [`semana-01/trabajos-practicos/tp3-integrador-estructuras-repetitivas/`](./semana-01/trabajos-practicos/tp3-integrador-estructuras-repetitivas/)

### TP5 Integrador - Listas (Unidad 5)
13 ejercicios sobre listas: indexación, slicing, métodos integrados (`sorted`, `append`, `remove`, `index`, `reverse`), listas anidadas y matrices. Incluye Ta-Te-Ti, matriz de ventas y ranking de puntajes.

📁 [`semana-01/trabajos-practicos/tp5-integrador-listas/`](./semana-01/trabajos-practicos/tp5-integrador-listas/)

## Cuestionarios

| # | Tema | Resultado |
|---|------|-----------|
| 1 | Estructuras Condicionales (operadores relacionales) | 5/5 |
| 2 | Operadores Lógicos | 5/5 |

## Cómo ejecutar los ejercicios

Requiere **Python 3.10 o superior**.

```bash
# Ejecutar un ejercicio individual
python semana-01/trabajos-practicos/tp1-estructuras-secuenciales/ejercicio-01.py

# Ejecutar el TP3 integrador (con menú interactivo)
python semana-01/trabajos-practicos/tp3-integrador-estructuras-repetitivas/entrega/tp3-integrador-estructuras-repetitivas.py

# Ejecutar el TP5 integrador de Listas (con menú interactivo)
python semana-01/trabajos-practicos/tp5-integrador-listas/entrega/tp5-integrador-listas.py
```

## Tecnologías

- **Python 3.10+** — lenguaje principal
- **Markdown** — documentación
- **Jupyter Notebooks** (.ipynb) — material teórico de la cátedra
- **Git + GitHub** — control de versiones y colaboración

## Licencia

Material educativo desarrollado como parte de la cursada. Libre para consulta con fines académicos.
