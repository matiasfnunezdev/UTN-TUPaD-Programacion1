"""
Trabajo Práctico Integrador: Repetitivas, Condicionales y Secuenciales
=======================================================================
Materia : Programación 1
Carrera : Tecnicatura Universitaria en Programación a Distancia
Unidad  : 3 - Estructuras Repetitivas

Contiene los 5 ejercicios solicitados, cada uno encapsulado en una función
y un menú interactivo para ejecutarlos individualmente.

Restricciones generales aplicadas en todos los ejercicios:
- SIN try/except
- Validaciones con .isalpha() y .isdigit() dentro de while/for
"""


# =============================================================================
# Ejercicio 1 - Caja del Kiosco
# =============================================================================
def ejercicio_01():
    print("\n=== EJERCICIO 1: CAJA DEL KIOSCO ===\n")

    nombre = input("Nombre del cliente: ").strip()
    while not nombre.isalpha():
        print("Error: el nombre solo puede contener letras y no puede estar vacío.")
        nombre = input("Nombre del cliente: ").strip()

    cantidad_str = input("Cantidad de productos: ").strip()
    while not cantidad_str.isdigit() or int(cantidad_str) == 0:
        print("Error: ingrese un número entero mayor a 0.")
        cantidad_str = input("Cantidad de productos: ").strip()
    cantidad = int(cantidad_str)

    total_sin_descuento = 0
    total_con_descuento = 0.0

    for i in range(1, cantidad + 1):
        precio_str = input(f"Producto {i} - Precio: ").strip()
        while not precio_str.isdigit():
            print("Error: el precio debe ser un número entero positivo.")
            precio_str = input(f"Producto {i} - Precio: ").strip()
        precio = int(precio_str)

        descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
        while descuento not in ("s", "n"):
            print("Error: ingrese 'S' o 'N'.")
            descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()

        total_sin_descuento += precio
        if descuento == "s":
            total_con_descuento += precio * 0.9
        else:
            total_con_descuento += precio

    ahorro = total_sin_descuento - total_con_descuento
    promedio = total_con_descuento / cantidad

    print()
    print(f"Cliente: {nombre}")
    print(f"Cantidad de productos: {cantidad}")
    print(f"Total sin descuentos: ${total_sin_descuento}")
    print(f"Total con descuentos: ${total_con_descuento:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")


# =============================================================================
# Ejercicio 2 - Acceso al Campus y Menú Seguro
# =============================================================================
def ejercicio_02():
    print("\n=== EJERCICIO 2: ACCESO AL CAMPUS ===\n")

    USUARIO_CORRECTO = "alumno"
    clave_correcta = "python123"
    MAX_INTENTOS = 3

    acceso = False
    for intento in range(1, MAX_INTENTOS + 1):
        print(f"Intento {intento}/{MAX_INTENTOS}")
        usuario = input("Usuario: ").strip()
        clave = input("Clave: ").strip()
        if usuario == USUARIO_CORRECTO and clave == clave_correcta:
            acceso = True
            print("Acceso concedido.\n")
            break
        print("Error: credenciales inválidas.\n")

    if not acceso:
        print("Cuenta bloqueada.")
        return

    salir = False
    while not salir:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un número válido.\n")
            continue

        opcion_num = int(opcion)
        if opcion_num < 1 or opcion_num > 4:
            print("Error: opción fuera de rango.\n")
            continue

        if opcion_num == 1:
            print("Estado: Inscripto\n")
        elif opcion_num == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.\n")
                continue
            confirmacion = input("Confirme la nueva clave: ")
            if nueva != confirmacion:
                print("Error: las claves no coinciden.\n")
                continue
            clave_correcta = nueva
            print("Clave actualizada con éxito.\n")
        elif opcion_num == 3:
            print("Mensaje: ¡Sigue adelante! El esfuerzo de hoy es el éxito de mañana.\n")
        elif opcion_num == 4:
            print("Hasta luego.")
            salir = True


# =============================================================================
# Ejercicio 3 - Agenda de Turnos con Nombres (sin listas)
# =============================================================================
def ejercicio_03():
    print("\n=== EJERCICIO 3: AGENDA DE TURNOS ===\n")

    operador = input("Nombre del operador: ").strip()
    while not operador.isalpha():
        print("Error: el nombre solo puede contener letras.")
        operador = input("Nombre del operador: ").strip()
    print(f"\nBienvenido/a, {operador}.\n")

    lunes1 = lunes2 = lunes3 = lunes4 = ""
    martes1 = martes2 = martes3 = ""

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
                    lunes1 = ""; cancelado = True
                elif lunes2 == nombre:
                    lunes2 = ""; cancelado = True
                elif lunes3 == nombre:
                    lunes3 = ""; cancelado = True
                elif lunes4 == nombre:
                    lunes4 = ""; cancelado = True
            else:
                if martes1 == nombre:
                    martes1 = ""; cancelado = True
                elif martes2 == nombre:
                    martes2 = ""; cancelado = True
                elif martes3 == nombre:
                    martes3 = ""; cancelado = True

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
                print(f"Turno 4: {lunes4 if lunes4 else '(libre)'}\n")
            else:
                print("\n--- AGENDA MARTES ---")
                print(f"Turno 1: {martes1 if martes1 else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 else '(libre)'}\n")

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
                print("Día con más turnos: LUNES\n")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: MARTES\n")
            else:
                print("Día con más turnos: EMPATE\n")


# =============================================================================
# Ejercicio 4 - Escape Room: La Bóveda
# =============================================================================
def ejercicio_04():
    print("\n=== EJERCICIO 4: ESCAPE ROOM - LA BÓVEDA ===\n")

    nombre = input("Nombre del agente: ").strip()
    while not nombre.isalpha():
        print("Error: solo letras.")
        nombre = input("Nombre del agente: ").strip()

    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    forzadas_seguidas = 0
    bloqueado = False

    print(f"\nAgente {nombre}, comienza la misión.\n")

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
        print("--- ESTADO ---")
        print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
        print(f"Alarma: {'ON' if alarma else 'OFF'} | Código parcial: '{codigo_parcial}'")
        print("1) Forzar cerradura (-20 energía, -2 tiempo)")
        print("2) Hackear panel (-10 energía, -3 tiempo)")
        print("3) Descansar (+15 energía, -1 tiempo)")

        opcion = input("Opción: ").strip()
        while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
            print("Error: opción inválida (1 a 3).")
            opcion = input("Opción: ").strip()
        opcion = int(opcion)

        if opcion == 1:
            energia -= 20
            tiempo -= 2
            forzadas_seguidas += 1

            if forzadas_seguidas >= 3:
                print(">> ¡La cerradura se trabó! Se activa la alarma.\n")
                alarma = True
                forzadas_seguidas = 0
            else:
                if energia < 40 and energia > 0:
                    print(">> Energía baja: riesgo de alarma. Elegí un número 1-3.")
                    eleccion = input("Número: ").strip()
                    while not eleccion.isdigit() or int(eleccion) not in (1, 2, 3):
                        print("Error: ingrese 1, 2 o 3.")
                        eleccion = input("Número: ").strip()
                    if int(eleccion) == 3:
                        alarma = True
                        print(">> ¡Alarma activada por error humano!\n")
                    else:
                        cerraduras_abiertas += 1
                        print(f">> Cerradura forzada. Abiertas: {cerraduras_abiertas}/3\n")
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
                        print(f">> Cerradura forzada. Abiertas: {cerraduras_abiertas}/3\n")
                    else:
                        print(">> Con la alarma activa, no logras abrir la cerradura.\n")

        elif opcion == 2:
            energia -= 10
            tiempo -= 3
            forzadas_seguidas = 0
            print(">> Hackeando panel...")
            for paso in range(1, 5):
                codigo_parcial += "A"
                print(f"   Paso {paso}/4 -> código parcial: '{codigo_parcial}'")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f">> Código completado. Cerradura abierta automáticamente. Abiertas: {cerraduras_abiertas}/3\n")
            else:
                print(">> Hackeo parcial.\n")

        elif opcion == 3:
            forzadas_seguidas = 0
            energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1
            if alarma:
                energia -= 10
                print(">> Descansaste, pero la alarma te resta 10 de energía extra.\n")
            else:
                print(">> Descansaste y recuperaste energía.\n")

        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            bloqueado = True

    print("=== FIN DE LA MISIÓN ===")
    if cerraduras_abiertas == 3:
        print(f"*** ¡VICTORIA, agente {nombre}! Bóveda abierta.")
    elif bloqueado:
        print(f"!!! DERROTA por bloqueo: la alarma activa con poco tiempo te atrapó.")
    else:
        print(f"XXX DERROTA: te quedaste sin energía o sin tiempo.")
    print(f"Estado final -> Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}")


# =============================================================================
# Ejercicio 5 - Escape Room: La Arena del Gladiador
# =============================================================================
def ejercicio_05():
    print("\n--- BIENVENIDO A LA ARENA ---")

    nombre = input("Nombre del Gladiador: ").strip()
    while not nombre.isalpha():
        print("Error: Solo se permiten letras.")
        nombre = input("Nombre del Gladiador: ").strip()

    vida_jugador = 100
    vida_enemigo = 100
    pociones = 3
    dano_jugador = 15
    dano_enemigo = 12
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


# =============================================================================
# Menú principal
# =============================================================================
def main():
    EJERCICIOS = {
        "1": ("Caja del Kiosco", ejercicio_01),
        "2": ("Acceso al Campus y Menú Seguro", ejercicio_02),
        "3": ("Agenda de Turnos (sin listas)", ejercicio_03),
        "4": ("Escape Room: La Bóveda", ejercicio_04),
        "5": ("Arena del Gladiador", ejercicio_05),
    }

    while True:
        print("\n" + "=" * 60)
        print("TP INTEGRADOR - REPETITIVAS, CONDICIONALES Y SECUENCIALES")
        print("=" * 60)
        for k, (titulo, _) in EJERCICIOS.items():
            print(f"  {k}. {titulo}")
        print("  0. Salir")
        print("=" * 60)

        opcion = input("Elija un ejercicio (0-5): ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        if opcion in EJERCICIOS:
            EJERCICIOS[opcion][1]()
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
