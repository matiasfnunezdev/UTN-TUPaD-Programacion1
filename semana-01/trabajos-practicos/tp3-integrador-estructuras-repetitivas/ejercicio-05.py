"""
Ejercicio 5 - "Escape Room: La Arena del Gladiador"
---------------------------------------------------
Simulador de batalla por turnos: Gladiador (jugador) vs Enemigo (CPU).

Tipos de datos obligatorios:
- String:  nombre del jugador.
- Int:     HP, cantidad de pociones, daño base.
- Float:   cálculo de daño (golpe crítico × 1.5).
- Boolean: estado del juego, turno.

Validaciones (sin try/except):
- Texto con .isalpha() en while.
- Números con .isdigit() en while.
"""

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_jugador = 15
dano_enemigo = 12
turno_jugador = True
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0 and juego_activo:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ").strip()
    while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: opción fuera de rango (1 a 3).")
        opcion = input("Opción: ").strip()
    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            dano_final = float(dano_jugador) * 1.5
            print(f">> ¡GOLPE CRÍTICO! Atacaste al enemigo por {dano_final:.1f} puntos de daño.")
        else:
            dano_final = float(dano_jugador)
            print(f">> ¡Atacaste al enemigo por {dano_final:.1f} puntos de daño!")
        vida_enemigo -= dano_final

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("   > Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f">> Te curaste 30 puntos de vida. Pociones restantes: {pociones}")
        else:
            print(">> ¡No quedan pociones! Pierdes el turno.")

    if vida_enemigo <= 0:
        break

    vida_jugador -= dano_enemigo
    print(f">> ¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"*** ¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"XXX DERROTA. Has caído en combate, {nombre}.")
print(f"Estado final -> {nombre}: {max(vida_jugador, 0)} HP | Enemigo: {max(vida_enemigo, 0)} HP")
