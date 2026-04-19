"""
Ejercicio 9 - Tablero de Ta-Te-Ti (lista de listas 3x3)
-------------------------------------------------------
- Inicializar con "-" en cada casilla.
- Dos jugadores ingresan posiciones (fila, columna) para colocar "X" o "O".
- Mostrar el tablero después de cada jugada.
- El juego termina cuando se completan las 9 casillas.
"""

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


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

    columna = input("  Columna (0-2): ").strip()
    while not columna.isdigit() or int(columna) not in (0, 1, 2):
        print("  Error: ingrese 0, 1 o 2.")
        columna = input("  Columna (0-2): ").strip()

    fila = int(fila)
    columna = int(columna)

    if tablero[fila][columna] != "-":
        print("  [!] Casilla ocupada, intente otra.\n")
        continue

    tablero[fila][columna] = jugador
    jugadas += 1
    mostrar(tablero)

    jugador = "O" if jugador == "X" else "X"

print("=== FIN DEL JUEGO ===")
