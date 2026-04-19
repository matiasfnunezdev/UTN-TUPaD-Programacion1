# Trabajo Práctico Integrador: Repetitivas, Condicionales y Secuenciales

**Materia:** Programación 1
**Carrera:** Tecnicatura Universitaria en Programación a Distancia
**Semana:** 01
**Unidad:** 3 - Estructuras Repetitivas

## Objetivo

Aplicar de manera integrada los conceptos de **estructuras secuenciales**, **condicionales** y **repetitivas** (`while` y `for`), junto con **validaciones estrictas** usando `.isalpha()` y `.isdigit()` (sin `try/except`).

---

## Ejercicio 1 — "Caja del Kiosco"

**Objetivo:** Simular una compra con validaciones y cálculo de total.

### Requisitos

1. Pedir nombre del cliente (solo letras, validar con `.isalpha()` en `while`).
2. Pedir cantidad de productos (entero positivo, validar con `.isdigit()` en `while`).
3. Por cada producto (usar `for`):
   - Pedir precio (entero, validar `.isdigit()`).
   - Pedir si tiene descuento `S/N` (validar con `while`, aceptar mayúsculas o minúsculas).
   - Si tiene descuento: aplicar **10%** al precio del producto.
4. Al final mostrar:
   - Total sin descuentos
   - Total con descuentos
   - Ahorro total
   - Promedio por producto (formateado con `:.2f`)

### Validaciones obligatorias

- Sin `try/except`.
- No aceptar nombre vacío.
- Cantidad **> 0**.

---

## Ejercicio 2 — "Acceso al Campus y Menú Seguro"

**Objetivo:** Login con intentos + menú de acciones con validación estricta.

### Requisitos

1. Credenciales fijas:
   - Usuario: `alumno`
   - Clave: `python123`
2. **Máximo 3 intentos**. Si falla 3 veces: "Cuenta bloqueada" y termina.
3. Si ingresa bien: menú repetitivo (`while`) con:
   1. Ver estado de inscripción ("Inscripto")
   2. Cambiar clave (pedir nueva + confirmación; deben coincidir; mínimo 6 caracteres)
   3. Mostrar mensaje motivacional
   4. Salir
4. Validación del menú: número con `.isdigit()` y entre 1 y 4.

---

## Ejercicio 3 — "Agenda de Turnos con Nombres (sin listas)"

### Contexto

Dos días de atención:
- **Lunes:** 4 turnos
- **Martes:** 3 turnos

### Reglas

1. Pedir nombre del operador (solo letras).
2. Menú repetitivo:
   1. Reservar turno
   2. Cancelar turno (por nombre)
   3. Ver agenda del día
   4. Ver resumen general
   5. Cerrar sistema
3. **Reservar:** elegir día, pedir nombre del paciente (solo letras), verificar que no esté repetido en ese día, guardar en el primer espacio libre.
4. **Cancelar:** elegir día, pedir nombre, si existe dejar el espacio en `""`.
5. **Ver agenda:** mostrar turnos del día (Turno 1..N), indicando "(libre)" si está vacío.
6. **Resumen general:** turnos ocupados/disponibles por día y día con más turnos (o empate).

### Restricciones

- ❌ No listas, no diccionarios, no sets, no tuplas.
- ✅ Usar `""` como vacío.
- ✅ Validaciones con `.isalpha()` y `.isdigit()` (sin `try/except`).

---

## Ejercicio 4 — "Escape Room: La Bóveda"

### Historia

Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.

### Variables iniciales (NO se piden por teclado)

```python
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
```

### Validaciones obligatorias

- Sin `try/except`.
- Pedir nombre del agente con `.isalpha()` en `while`.
- Validar opciones del menú y números con `.isdigit()` en `while`.

### Regla anti-spam

Si el jugador elige **Forzar cerradura (opción 1) 3 veces seguidas**:
- Se cobra el costo (-20 energía, -2 tiempo).
- **NO** abre cerradura.
- Se activa la alarma (`alarma = True`).

Si elige opción 2 o 3, se corta la racha.

### Menú

1. **Forzar cerradura** (-20 energía, -2 tiempo)
   - Si energía < 40: "riesgo de alarma" → pedir 1-3, si elige 3 → `alarma=True`.
   - Si no hay alarma, abre 1 cerradura.
   - Aplica regla anti-spam.
2. **Hackear panel** (-10 energía, -3 tiempo)
   - `for` de 4 pasos mostrando progreso.
   - En cada paso suma una letra al `codigo_parcial`.
   - Si `len(codigo_parcial) >= 8`, abre 1 cerradura automáticamente.
3. **Descansar** (+15 energía, máx 100; -1 tiempo; si alarma ON: -10 energía extra)

### Bloqueo por alarma

Si `alarma == True` y `tiempo <= 3` y la bóveda no está abierta → bloqueo y derrota.

### Condiciones de fin

- `cerraduras_abiertas == 3` → **VICTORIA**
- `energia <= 0` o `tiempo <= 0` → **DERROTA**
- Bloqueo por alarma → **DERROTA**

---

## Ejercicio 5 — "Escape Room: La Arena del Gladiador"

### Descripción

Simulador de batalla por turnos. Gladiador (jugador) vs Enemigo (CPU). Reducir el HP del oponente a 0 antes de que él lo haga contigo.

### Tipos de datos obligatorios

- **String:** nombre del jugador.
- **Int:** HP, cantidad de pociones.
- **Float:** cálculo de daño (ej. crítico × 1.5).
- **Boolean:** estado del juego, turno.

### Reglas de validación

- Sin `try/except`.
- Texto: `.isalpha()` en `while`.
- Números: `.isdigit()` en `while`.

### Variables iniciales

- `vida_jugador = 100`
- `vida_enemigo = 100`
- `pociones = 3`
- `dano_jugador = 15`
- `dano_enemigo = 12`
- `turno_jugador = True`

### Ciclo de combate (mientras ambos tengan HP > 0)

#### Turno del jugador (menú):

1. **Ataque Pesado:** si vida del enemigo < 20 → crítico × 1.5 (float).
2. **Ráfaga Veloz:** `for` de 3 iteraciones, cada una resta 5 al enemigo.
3. **Curar:** si pociones > 0, suma 30 HP y resta 1 poción. Si no, "¡No quedan pociones!" (pierde el turno).

Validar: opción debe ser número (`.isdigit()`) y debe estar entre 1 y 3.

#### Turno del enemigo (automático):

- Resta `dano_enemigo` (12) a la vida del jugador.

### Fin del juego

- `vida_jugador > 0` → "¡VICTORIA! [Nombre] ha ganado la batalla."
- `vida_jugador <= 0` → "DERROTA. Has caído en combate."

---

## Sugerencia

Resolver primero los ejercicios por cuenta propia y luego comparar las respuestas con las soluciones propuestas.
