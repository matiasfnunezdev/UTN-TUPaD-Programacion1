"""
Trabajo Práctico Integrador 5 - Listas
======================================
Tecnicatura Universitaria en Programación a Distancia (UTN)
Materia: Programación 1 - Unidad 5

Resolución consolidada de los 13 ejercicios propuestos.
Cada ejercicio está implementado en una función independiente.
Un menú interactivo permite seleccionar y ejecutar cualquiera.
"""

import random


# ---------------------------------------------------------------------------
# Ejercicio 1
# ---------------------------------------------------------------------------
def ejercicio_01():
    """Notas de 10 estudiantes: lista, promedio, máxima y mínima."""
    notas = [7.5, 8.0, 6.0, 9.5, 4.0, 10.0, 5.5, 7.0, 8.5, 6.5]

    print("Notas de los estudiantes:")
    for i, nota in enumerate(notas, start=1):
        print(f"  Estudiante {i}: {nota}")

    promedio = sum(notas) / len(notas)
    print(f"\nPromedio: {promedio:.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")


# ---------------------------------------------------------------------------
# Ejercicio 2
# ---------------------------------------------------------------------------
def ejercicio_02():
    """5 productos: cargar, ordenar alfabéticamente, eliminar uno."""
    productos = []
    print("Cargá 5 productos:")
    for i in range(1, 6):
        nombre = input(f"  Producto {i}: ").strip()
        productos.append(nombre)

    ordenados = sorted(productos)
    print("\nLista ordenada alfabéticamente:")
    for p in ordenados:
        print(f"  - {p}")

    a_eliminar = input("\n¿Qué producto desea eliminar?: ").strip()
    if a_eliminar in productos:
        productos.remove(a_eliminar)
        print(f"\nProducto '{a_eliminar}' eliminado.")
    else:
        print(f"\nEl producto '{a_eliminar}' no se encontró en la lista.")

    print("\nLista final actualizada:")
    for p in productos:
        print(f"  - {p}")


# ---------------------------------------------------------------------------
# Ejercicio 3
# ---------------------------------------------------------------------------
def ejercicio_03():
    """15 enteros aleatorios entre 1 y 100, separar pares e impares."""
    numeros = [random.randint(1, 100) for _ in range(15)]

    print("Lista generada:")
    for n in numeros:
        print(f"  {n}", end="")
    print()

    pares, impares = [], []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("\nPares:")
    for p in pares:
        print(f"  {p}", end="")
    print(f"\nTotal pares: {len(pares)}")

    print("\nImpares:")
    for i in impares:
        print(f"  {i}", end="")
    print(f"\nTotal impares: {len(impares)}")


# ---------------------------------------------------------------------------
# Ejercicio 4
# ---------------------------------------------------------------------------
def ejercicio_04():
    """Eliminar duplicados preservando el orden de aparición."""
    original = [1, 3, 5, 3, 7, 1, 9, 5, 11, 7, 13, 9, 15]

    print("Lista original:")
    for x in original:
        print(f"  {x}", end="")
    print()

    sin_duplicados = []
    for x in original:
        if x not in sin_duplicados:
            sin_duplicados.append(x)

    print("\nLista sin duplicados:")
    for x in sin_duplicados:
        print(f"  {x}", end="")
    print()


# ---------------------------------------------------------------------------
# Ejercicio 5
# ---------------------------------------------------------------------------
def ejercicio_05():
    """8 estudiantes: agregar o eliminar."""
    estudiantes = ["Ana", "Bruno", "Carla", "Diego",
                   "Elena", "Fernando", "Gabriela", "Hugo"]

    print("Lista inicial:")
    for i, nombre in enumerate(estudiantes, start=1):
        print(f"  {i}. {nombre}")

    print("\n¿Qué desea hacer?")
    print("  1) Agregar un estudiante")
    print("  2) Eliminar un estudiante")
    opcion = input("Opción: ").strip()
    while opcion not in ("1", "2"):
        print("Error: ingrese 1 o 2.")
        opcion = input("Opción: ").strip()

    if opcion == "1":
        nuevo = input("Nombre del nuevo estudiante: ").strip()
        estudiantes.append(nuevo)
        print(f"\n'{nuevo}' agregado.")
    else:
        a_eliminar = input("Nombre del estudiante a eliminar: ").strip()
        if a_eliminar in estudiantes:
            estudiantes.remove(a_eliminar)
            print(f"\n'{a_eliminar}' eliminado.")
        else:
            print(f"\n'{a_eliminar}' no se encontró en la lista.")

    print("\nLista final actualizada:")
    for i, nombre in enumerate(estudiantes, start=1):
        print(f"  {i}. {nombre}")


# ---------------------------------------------------------------------------
# Ejercicio 6
# ---------------------------------------------------------------------------
def ejercicio_06():
    """Rotar una posición a la derecha (el último pasa al inicio)."""
    numeros = [10, 20, 30, 40, 50, 60, 70]

    print("Lista original:")
    for n in numeros:
        print(f"  {n}", end="")
    print()

    ultimo = numeros[-1]
    rotada = [ultimo]
    for i in range(len(numeros) - 1):
        rotada.append(numeros[i])

    print("\nLista rotada a la derecha:")
    for n in rotada:
        print(f"  {n}", end="")
    print()


# ---------------------------------------------------------------------------
# Ejercicio 7
# ---------------------------------------------------------------------------
def ejercicio_07():
    """Temperaturas semanales (matriz 7x2): promedios y mayor amplitud."""
    dias = ["Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"]
    temperaturas = [
        [12, 22], [10, 19], [13, 25], [14, 28],
        [11, 23], [9, 20], [8, 17],
    ]

    print("Temperaturas de la semana:")
    for i in range(len(dias)):
        print(f"  {dias[i]:<10} | mín: {temperaturas[i][0]}°C | máx: {temperaturas[i][1]}°C")

    suma_min = suma_max = 0
    for fila in temperaturas:
        suma_min += fila[0]
        suma_max += fila[1]

    print(f"\nPromedio mínimas: {suma_min / len(temperaturas):.2f}°C")
    print(f"Promedio máximas: {suma_max / len(temperaturas):.2f}°C")

    mayor_amp = -1
    dia_amp = ""
    for i in range(len(temperaturas)):
        amp = temperaturas[i][1] - temperaturas[i][0]
        if amp > mayor_amp:
            mayor_amp = amp
            dia_amp = dias[i]

    print(f"\nMayor amplitud térmica: {dia_amp} ({mayor_amp}°C)")


# ---------------------------------------------------------------------------
# Ejercicio 8
# ---------------------------------------------------------------------------
def ejercicio_08():
    """Notas 5 estudiantes x 3 materias: promedios por estudiante y materia."""
    estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
    materias = ["Matemática", "Programación", "Inglés"]
    notas = [
        [8, 9, 7],
        [6, 7, 8],
        [10, 9, 9],
        [5, 6, 7],
        [9, 8, 10],
    ]

    print("Notas:")
    print(f"  {'Estudiante':<12}", end="")
    for m in materias:
        print(f"{m:<14}", end="")
    print()
    for i in range(len(estudiantes)):
        print(f"  {estudiantes[i]:<12}", end="")
        for nota in notas[i]:
            print(f"{nota:<14}", end="")
        print()

    print("\nPromedio por estudiante:")
    for i in range(len(estudiantes)):
        print(f"  {estudiantes[i]}: {sum(notas[i]) / len(notas[i]):.2f}")

    print("\nPromedio por materia:")
    for j in range(len(materias)):
        suma = 0
        for i in range(len(estudiantes)):
            suma += notas[i][j]
        print(f"  {materias[j]}: {suma / len(estudiantes):.2f}")


# ---------------------------------------------------------------------------
# Ejercicio 9
# ---------------------------------------------------------------------------
def ejercicio_09():
    """Tablero Ta-Te-Ti 3x3, dos jugadores, 9 jugadas."""
    tablero = [["-"] * 3 for _ in range(3)]

    def mostrar(t):
        print()
        print("    0   1   2")
        for i in range(3):
            print(f"  {i} ", end="")
            for j in range(3):
                print(f" {t[i][j]} ", end="")
                if j < 2:
                    print("|", end="")
            print()
            if i < 2:
                print("    ---+---+---")
        print()

    print("=== TA-TE-TI ===")
    mostrar(tablero)

    jugador = "X"
    jugadas = 0
    while jugadas < 9:
        print(f"Turno del jugador '{jugador}'")
        fila = input("  Fila (0-2): ").strip()
        while not fila.isdigit() or int(fila) not in (0, 1, 2):
            print("  Error: ingrese 0, 1 o 2.")
            fila = input("  Fila (0-2): ").strip()

        col = input("  Columna (0-2): ").strip()
        while not col.isdigit() or int(col) not in (0, 1, 2):
            print("  Error: ingrese 0, 1 o 2.")
            col = input("  Columna (0-2): ").strip()

        fila, col = int(fila), int(col)

        if tablero[fila][col] != "-":
            print("  [!] Casilla ocupada, intente otra.\n")
            continue

        tablero[fila][col] = jugador
        jugadas += 1
        mostrar(tablero)
        jugador = "O" if jugador == "X" else "X"

    print("=== FIN DEL JUEGO ===")


# ---------------------------------------------------------------------------
# Ejercicio 10
# ---------------------------------------------------------------------------
def ejercicio_10():
    """Ventas 4 productos x 7 días: total por producto, mejor día y producto."""
    productos = ["Café", "Té", "Galletas", "Jugo"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"]
    ventas = [
        [12, 15, 10, 8, 20, 25, 18],
        [5, 7, 6, 4, 9, 10, 8],
        [20, 22, 18, 15, 30, 35, 28],
        [10, 12, 11, 9, 14, 18, 16],
    ]

    print("Matriz de ventas:")
    print(f"  {'Producto':<10}", end="")
    for d in dias:
        print(f"{d[:3]:>5}", end="")
    print(f"{'TOTAL':>8}")
    for i in range(len(productos)):
        print(f"  {productos[i]:<10}", end="")
        for v in ventas[i]:
            print(f"{v:>5}", end="")
        print(f"{sum(ventas[i]):>8}")

    totales_prod = []
    print("\nTotal vendido por producto:")
    for i in range(len(productos)):
        total = sum(ventas[i])
        totales_prod.append(total)
        print(f"  {productos[i]}: {total}")

    totales_dia = []
    print("\nVentas totales por día:")
    for j in range(len(dias)):
        suma = 0
        for i in range(len(productos)):
            suma += ventas[i][j]
        totales_dia.append(suma)
        print(f"  {dias[j]}: {suma}")

    mayor_dia = 0
    for j in range(1, len(totales_dia)):
        if totales_dia[j] > totales_dia[mayor_dia]:
            mayor_dia = j
    print(f"\nDía con mayores ventas: {dias[mayor_dia]} ({totales_dia[mayor_dia]} unidades)")

    mayor_prod = 0
    for i in range(1, len(totales_prod)):
        if totales_prod[i] > totales_prod[mayor_prod]:
            mayor_prod = i
    print(f"Producto más vendido: {productos[mayor_prod]} ({totales_prod[mayor_prod]} unidades)")


# ---------------------------------------------------------------------------
# Ejercicio 11
# ---------------------------------------------------------------------------
def ejercicio_11():
    """Buscar nombre dentro de una lista de 10 estudiantes."""
    estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena",
                   "Fernando", "Gabriela", "Hugo", "Inés", "Julián"]

    print("Lista de estudiantes:")
    for i, nombre in enumerate(estudiantes):
        print(f"  [{i}] {nombre}")

    buscado = input("\nIngrese el nombre a buscar: ").strip()

    if buscado in estudiantes:
        posicion = estudiantes.index(buscado)
        print(f"\n[OK] '{buscado}' se encuentra en la posición {posicion}.")
    else:
        print(f"\n[!] '{buscado}' no está en la lista.")


# ---------------------------------------------------------------------------
# Ejercicio 12
# ---------------------------------------------------------------------------
def ejercicio_12():
    """8 enteros: mostrar original, ascendente y descendente."""
    numeros = []
    print("Ingresá 8 números enteros:")
    for i in range(1, 9):
        valor = input(f"  Número {i}: ").strip()
        while not valor.lstrip("-").isdigit():
            print("  Error: ingrese un número entero válido.")
            valor = input(f"  Número {i}: ").strip()
        numeros.append(int(valor))

    print("\nLista original:")
    for n in numeros:
        print(f"  {n}", end="")
    print()

    print("\nOrdenada de menor a mayor:")
    for n in sorted(numeros):
        print(f"  {n}", end="")
    print()

    print("\nOrdenada de mayor a menor:")
    for n in sorted(numeros, reverse=True):
        print(f"  {n}", end="")
    print()


# ---------------------------------------------------------------------------
# Ejercicio 13
# ---------------------------------------------------------------------------
def ejercicio_13():
    """Ranking de puntajes de un videojuego."""
    puntajes = [450, 1200, 875, 990, 300, 1500, 640]

    print("Puntajes registrados:")
    for p in puntajes:
        print(f"  {p}", end="")
    print()

    print(f"\nPuntaje más alto: {max(puntajes)}")
    print(f"Puntaje más bajo: {min(puntajes)}")

    ranking = sorted(puntajes, reverse=True)
    print("\nRanking (de mayor a menor):")
    for i, p in enumerate(ranking, start=1):
        print(f"  {i}°: {p}")

    posicion = ranking.index(990) + 1
    print(f"\nEl puntaje 990 ocupa la posición {posicion}° del ranking.")


# ---------------------------------------------------------------------------
# Menú interactivo
# ---------------------------------------------------------------------------
EJERCICIOS = {
    "1": ("Notas de 10 estudiantes", ejercicio_01),
    "2": ("5 productos (ordenar/eliminar)", ejercicio_02),
    "3": ("15 aleatorios: pares e impares", ejercicio_03),
    "4": ("Eliminar duplicados", ejercicio_04),
    "5": ("8 estudiantes (agregar/eliminar)", ejercicio_05),
    "6": ("Rotación a la derecha", ejercicio_06),
    "7": ("Temperaturas semanales (7x2)", ejercicio_07),
    "8": ("Notas 5 estudiantes x 3 materias", ejercicio_08),
    "9": ("Tablero de Ta-Te-Ti", ejercicio_09),
    "10": ("Ventas 4 productos x 7 días", ejercicio_10),
    "11": ("Buscar nombre en lista", ejercicio_11),
    "12": ("Ordenar 8 enteros", ejercicio_12),
    "13": ("Ranking de puntajes", ejercicio_13),
}


def mostrar_menu():
    print("\n" + "=" * 60)
    print("  TP INTEGRADOR 5 - LISTAS")
    print("=" * 60)
    for clave in sorted(EJERCICIOS.keys(), key=int):
        titulo, _ = EJERCICIOS[clave]
        print(f"  {clave:>2}) {titulo}")
    print("   0) Salir")
    print("=" * 60)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione un ejercicio: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion not in EJERCICIOS:
            print("Error: opción inválida. Ingrese un número del 0 al 13.")
            continue

        titulo, funcion = EJERCICIOS[opcion]
        print(f"\n--- Ejercicio {opcion}: {titulo} ---\n")
        funcion()
        input("\nPresione ENTER para volver al menú...")


if __name__ == "__main__":
    main()
