"""
================================================================================
Trabajo Práctico N.º 2: Estructuras Condicionales
================================================================================
Materia : Programación 1
Carrera : Tecnicatura Universitaria en Programación a Distancia
Semana  : 01
Unidad  : 2 - Estructuras Condicionales
Alumno  : Matias Fernando Nuñez

Descripción:
    Resolución de los 10 ejercicios propuestos en la guía del TP2, aplicando
    estructuras condicionales en Python (if, elif, else) para la toma de
    decisiones a partir de las entradas del usuario.

Uso:
    Ejecutar el archivo y elegir del menú el número del ejercicio a probar
    (del 1 al 10). Ingresar 0 para salir.

        python tp2-estructuras-condicionales.py
================================================================================
"""


# ---------------------------------------------------------------------------
# Ejercicio 1
# ---------------------------------------------------------------------------
def ejercicio_01():
    """Solicita la edad e indica si es mayor de 18 años."""
    edad = int(input("Ingresá tu edad: "))

    if edad > 18:
        print("Es mayor de edad")


# ---------------------------------------------------------------------------
# Ejercicio 2
# ---------------------------------------------------------------------------
def ejercicio_02():
    """Solicita una nota e indica si está aprobado (>= 6) o desaprobado."""
    nota = float(input("Ingresá tu nota: "))

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


# ---------------------------------------------------------------------------
# Ejercicio 3
# ---------------------------------------------------------------------------
def ejercicio_03():
    """Permite ingresar solo números pares (uso del operador módulo %)."""
    numero = int(input("Ingresá un número par: "))

    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


# ---------------------------------------------------------------------------
# Ejercicio 4
# ---------------------------------------------------------------------------
def ejercicio_04():
    """Categoriza la edad: Niño/a, Adolescente, Adulto/a joven o Adulto/a."""
    edad = int(input("Ingresá tu edad: "))

    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")


# ---------------------------------------------------------------------------
# Ejercicio 5
# ---------------------------------------------------------------------------
def ejercicio_05():
    """Valida que una contraseña tenga entre 8 y 14 caracteres (uso de len())."""
    contrasena = input("Ingresá una contraseña (entre 8 y 14 caracteres): ")

    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# ---------------------------------------------------------------------------
# Ejercicio 6
# ---------------------------------------------------------------------------
def ejercicio_06():
    """Categoriza el consumo eléctrico mensual y advierte si supera 500 kWh."""
    consumo = float(input("Ingresá el consumo mensual en kWh: "))

    if consumo < 150:
        print("Consumo bajo")
    elif consumo <= 300:
        print("Consumo medio")
    else:
        print("Consumo alto")

    if consumo > 500:
        print("Considere medidas de ahorro energético")


# ---------------------------------------------------------------------------
# Ejercicio 7
# ---------------------------------------------------------------------------
def ejercicio_07():
    """Agrega '!' al final si el string termina en vocal."""
    texto = input("Ingresá una palabra o frase: ")

    if texto[-1].lower() in "aeiou":
        print(texto + "!")
    else:
        print(texto)


# ---------------------------------------------------------------------------
# Ejercicio 8
# ---------------------------------------------------------------------------
def ejercicio_08():
    """Transforma el nombre con upper(), lower() o title() según la opción."""
    nombre = input("Ingresá tu nombre: ")
    opcion = int(input("Elegí una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado): "))

    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())
    else:
        print("Opción inválida. Debe ser 1, 2 o 3.")


# ---------------------------------------------------------------------------
# Ejercicio 9
# ---------------------------------------------------------------------------
def ejercicio_09():
    """Clasifica un terremoto según la escala de Richter."""
    magnitud = float(input("Ingresá la magnitud del terremoto (escala de Richter): "))

    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")


# ---------------------------------------------------------------------------
# Ejercicio 10
# ---------------------------------------------------------------------------
def ejercicio_10():
    """Indica la estación del año a partir del hemisferio, mes y día.

    Tabla astronómica:
        21 mar - 20 jun  → Primavera (N) / Otoño (S)
        21 jun - 22 sep  → Verano    (N) / Invierno (S)
        23 sep - 20 dic  → Otoño     (N) / Primavera (S)
        21 dic - 20 mar  → Invierno  (N) / Verano (S)
    """
    hemisferio = input("Ingresá tu hemisferio (N/S): ").strip().upper()
    mes = int(input("Ingresá el mes (1-12): "))
    dia = int(input("Ingresá el día (1-31): "))

    if (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        periodo = "primavera-norte"
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 22):
        periodo = "verano-norte"
    elif (mes == 9 and dia >= 23) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        periodo = "otoño-norte"
    else:
        periodo = "invierno-norte"

    if hemisferio == "N":
        if periodo == "primavera-norte":
            estacion = "Primavera"
        elif periodo == "verano-norte":
            estacion = "Verano"
        elif periodo == "otoño-norte":
            estacion = "Otoño"
        else:
            estacion = "Invierno"
    elif hemisferio == "S":
        if periodo == "primavera-norte":
            estacion = "Otoño"
        elif periodo == "verano-norte":
            estacion = "Invierno"
        elif periodo == "otoño-norte":
            estacion = "Primavera"
        else:
            estacion = "Verano"
    else:
        estacion = None

    if estacion is None:
        print("Hemisferio inválido. Ingresá N (norte) o S (sur).")
    else:
        print(f"Te encontrás en {estacion}.")


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------
EJERCICIOS = {
    1: ("Mayor de edad", ejercicio_01),
    2: ("Aprobado / Desaprobado", ejercicio_02),
    3: ("Número par o impar", ejercicio_03),
    4: ("Categorías de edad", ejercicio_04),
    5: ("Validación de contraseña (8-14 caracteres)", ejercicio_05),
    6: ("Consumo eléctrico", ejercicio_06),
    7: ("Frase que termina en vocal", ejercicio_07),
    8: ("Transformación de nombre (upper/lower/title)", ejercicio_08),
    9: ("Magnitud de terremoto (escala de Richter)", ejercicio_09),
    10: ("Estación del año (hemisferio, mes, día)", ejercicio_10),
}


def mostrar_menu():
    print("\n" + "=" * 60)
    print("  TP2 - Estructuras Condicionales - Programación 1")
    print("=" * 60)
    for numero, (titulo, _) in EJERCICIOS.items():
        print(f"  {numero:>2}. {titulo}")
    print("   0. Salir")
    print("=" * 60)


def main():
    while True:
        mostrar_menu()
        opcion_str = input("Elegí un ejercicio (0 para salir): ").strip()

        if not opcion_str.isdigit():
            print("⚠ Opción inválida. Ingresá un número del 0 al 10.")
            continue

        opcion = int(opcion_str)

        if opcion == 0:
            print("¡Hasta luego!")
            break

        if opcion not in EJERCICIOS:
            print("⚠ Opción inválida. Ingresá un número del 0 al 10.")
            continue

        titulo, funcion = EJERCICIOS[opcion]
        print(f"\n--- Ejercicio {opcion}: {titulo} ---")
        funcion()


if __name__ == "__main__":
    main()
