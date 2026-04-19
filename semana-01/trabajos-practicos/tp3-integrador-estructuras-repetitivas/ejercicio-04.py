"""
Ejercicio 4 - "Escape Room: La Bóveda"
--------------------------------------
Hay 3 cerraduras. Tenés energía y tiempo limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

Reglas clave:
- Anti-spam: 3 "Forzar cerradura" seguidas -> se cobra el costo, NO abre y se
  activa la alarma automáticamente.
- Si energía < 40 al forzar, hay "riesgo de alarma": se pide número 1-3,
  si elige 3 -> alarma = True.
- Hackear panel: for de 4 pasos sumando una letra al codigo_parcial.
  Si len(codigo_parcial) >= 8 al terminar, abre 1 cerradura automáticamente.
- Descansar: +15 energía (máx 100), -1 tiempo. Si alarma ON: -10 energía extra.
- Si alarma == True y tiempo <= 3 sin abrir bóveda -> DERROTA por bloqueo.

Validaciones (sin try/except): .isalpha() y .isdigit() en while.
"""

print("=== ESCAPE ROOM: LA BÓVEDA ===\n")

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
