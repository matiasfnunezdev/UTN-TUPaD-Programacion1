"""
Ejercicio 3 - "Agenda de Turnos con Nombres (sin listas)"
---------------------------------------------------------
Dos días de atención: Lunes (4 turnos) y Martes (3 turnos).

RESTRICCIONES:
- ❌ Sin listas, diccionarios, sets ni tuplas.
- ✅ Cada turno se guarda en una variable individual.
- ✅ Se usa "" para indicar que un turno está libre.
- ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).
"""

print("=== AGENDA DE TURNOS ===\n")

operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: el nombre solo puede contener letras.")
    operador = input("Nombre del operador: ").strip()

print(f"\nBienvenido/a, {operador}.\n")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

salir = False
while not salir:
    print("--- MENÚ ---")
    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    opcion = input("Opción: ").strip()

    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida (1 a 5).\n")
        continue

    opcion = int(opcion)

    if opcion == 5:
        print("Sistema cerrado. Hasta luego.")
        salir = True
        continue

    if opcion in (1, 2, 3):
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while not dia.isdigit() or int(dia) not in (1, 2):
            print("Error: ingrese 1 (Lunes) o 2 (Martes).")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()
        dia = int(dia)
    else:
        dia = None

    if opcion == 1:
        nombre = input("Nombre del paciente: ").strip()
        while not nombre.isalpha():
            print("Error: solo letras.")
            nombre = input("Nombre del paciente: ").strip()

        if dia == 1:
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print(f"[!] {nombre} ya tiene turno el lunes.\n")
                continue
            if lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("[!] No hay turnos disponibles el lunes.\n")
                continue
            print(f"[OK] Turno reservado para {nombre} el lunes.\n")
        else:
            if nombre in (martes1, martes2, martes3):
                print(f"[!] {nombre} ya tiene turno el martes.\n")
                continue
            if martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("[!] No hay turnos disponibles el martes.\n")
                continue
            print(f"[OK] Turno reservado para {nombre} el martes.\n")

    elif opcion == 2:
        nombre = input("Nombre del paciente a cancelar: ").strip()
        while not nombre.isalpha():
            print("Error: solo letras.")
            nombre = input("Nombre del paciente a cancelar: ").strip()

        cancelado = False
        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                cancelado = True
            elif lunes2 == nombre:
                lunes2 = ""
                cancelado = True
            elif lunes3 == nombre:
                lunes3 = ""
                cancelado = True
            elif lunes4 == nombre:
                lunes4 = ""
                cancelado = True
        else:
            if martes1 == nombre:
                martes1 = ""
                cancelado = True
            elif martes2 == nombre:
                martes2 = ""
                cancelado = True
            elif martes3 == nombre:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"[OK] Turno de {nombre} cancelado.\n")
        else:
            print(f"[!] No se encontró un turno a nombre de {nombre}.\n")

    elif opcion == 3:
        if dia == 1:
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 else '(libre)'}")
            print()
        else:
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 else '(libre)'}")
            print()

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes:  ocupados = {ocupados_lunes}, libres = {libres_lunes}")
        print(f"Martes: ocupados = {ocupados_martes}, libres = {libres_martes}")
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: LUNES")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: MARTES")
        else:
            print("Día con más turnos: EMPATE")
        print()
