"""
Ejercicio 2 - "Acceso al Campus y Menú Seguro"
----------------------------------------------
Login con máximo 3 intentos + menú repetitivo de acciones.

Credenciales fijas:
    usuario: "alumno"
    clave:   "python123"

Validaciones (sin try/except):
- Opción del menú: número (.isdigit()) y entre 1 y 4.
- Cambio de clave: mínimo 6 caracteres y debe coincidir con la confirmación.
"""

USUARIO_CORRECTO = "alumno"
clave_correcta = "python123"
MAX_INTENTOS = 3

print("=== ACCESO AL CAMPUS ===\n")

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
else:
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
