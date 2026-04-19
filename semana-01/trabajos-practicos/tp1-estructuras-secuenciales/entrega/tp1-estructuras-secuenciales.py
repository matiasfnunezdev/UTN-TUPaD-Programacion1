"""
================================================================================
Trabajo Práctico N.º 1: Estructuras Secuenciales
================================================================================
Materia : Programación 1
Carrera : Tecnicatura Universitaria en Programación a Distancia
Semana  : 01
Alumno  : Matias Fernando Nuñez

Descripción:
    Resolución de los 10 ejercicios propuestos en la guía del TP1, aplicando
    estructuras secuenciales en Python (entrada de datos, cálculos y salida
    por pantalla).

Uso:
    Ejecutar el archivo y elegir del menú el número del ejercicio a probar
    (del 1 al 10). Ingresar 0 para salir.

        python tp1-estructuras-secuenciales.py
================================================================================
"""

import math


# ---------------------------------------------------------------------------
# Ejercicio 1
# ---------------------------------------------------------------------------
def ejercicio_01():
    """Imprime por pantalla el mensaje 'Hola Mundo!'."""
    print("Hola Mundo!")


# ---------------------------------------------------------------------------
# Ejercicio 2
# ---------------------------------------------------------------------------
def ejercicio_02():
    """Pide el nombre del usuario e imprime un saludo personalizado."""
    nombre = input("Ingresá tu nombre: ")
    print(f"Hola {nombre}!")


# ---------------------------------------------------------------------------
# Ejercicio 3
# ---------------------------------------------------------------------------
def ejercicio_03():
    """Pide nombre, apellido, edad y residencia, e imprime una presentación."""
    nombre = input("Ingresá tu nombre: ")
    apellido = input("Ingresá tu apellido: ")
    edad = input("Ingresá tu edad: ")
    residencia = input("Ingresá tu lugar de residencia: ")

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# ---------------------------------------------------------------------------
# Ejercicio 4
# ---------------------------------------------------------------------------
def ejercicio_04():
    """Calcula área y perímetro de un círculo a partir de su radio.

    Fórmulas:
        área      = π · r²
        perímetro = 2 · π · r
    """
    radio = float(input("Ingresá el radio del círculo: "))

    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio

    print(f"Área:      {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")


# ---------------------------------------------------------------------------
# Ejercicio 5
# ---------------------------------------------------------------------------
def ejercicio_05():
    """Convierte una cantidad de segundos a horas (1 hora = 3600 segundos)."""
    segundos = float(input("Ingresá la cantidad de segundos: "))

    horas = segundos / 3600

    print(f"{segundos} segundos equivalen a {horas:.4f} horas")


# ---------------------------------------------------------------------------
# Ejercicio 6
# ---------------------------------------------------------------------------
def ejercicio_06():
    """Imprime la tabla de multiplicar (del 1 al 10) del número ingresado."""
    numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))

    print(f"\nTabla de multiplicar del {numero}:")
    print(f"{numero} x  1 = {numero * 1}")
    print(f"{numero} x  2 = {numero * 2}")
    print(f"{numero} x  3 = {numero * 3}")
    print(f"{numero} x  4 = {numero * 4}")
    print(f"{numero} x  5 = {numero * 5}")
    print(f"{numero} x  6 = {numero * 6}")
    print(f"{numero} x  7 = {numero * 7}")
    print(f"{numero} x  8 = {numero * 8}")
    print(f"{numero} x  9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")


# ---------------------------------------------------------------------------
# Ejercicio 7
# ---------------------------------------------------------------------------
def ejercicio_07():
    """Realiza suma, resta, multiplicación y división entre dos enteros."""
    a = int(input("Ingresá el primer número entero (distinto de 0): "))
    b = int(input("Ingresá el segundo número entero (distinto de 0): "))

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    print(f"\nSuma:           {a} + {b} = {suma}")
    print(f"Resta:          {a} - {b} = {resta}")
    print(f"Multiplicación: {a} * {b} = {multiplicacion}")
    print(f"División:       {a} / {b} = {division}")


# ---------------------------------------------------------------------------
# Ejercicio 8
# ---------------------------------------------------------------------------
def ejercicio_08():
    """Calcula el Índice de Masa Corporal (IMC) a partir de peso y altura.

    Fórmula:
        IMC = peso (kg) / altura (m)²
    """
    peso = float(input("Ingresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))

    imc = peso / (altura ** 2)

    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")


# ---------------------------------------------------------------------------
# Ejercicio 9
# ---------------------------------------------------------------------------
def ejercicio_09():
    """Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Fórmula:
        °F = (9/5) · °C + 32
    """
    celsius = float(input("Ingresá la temperatura en grados Celsius: "))

    fahrenheit = (9 / 5) * celsius + 32

    print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")


# ---------------------------------------------------------------------------
# Ejercicio 10
# ---------------------------------------------------------------------------
def ejercicio_10():
    """Calcula el promedio de 3 números ingresados por el usuario."""
    n1 = float(input("Ingresá el primer número: "))
    n2 = float(input("Ingresá el segundo número: "))
    n3 = float(input("Ingresá el tercer número: "))

    promedio = (n1 + n2 + n3) / 3

    print(f"El promedio de {n1}, {n2} y {n3} es: {promedio:.2f}")


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------
EJERCICIOS = {
    1: ("Hola Mundo", ejercicio_01),
    2: ("Saludo personalizado", ejercicio_02),
    3: ("Presentación con datos del usuario", ejercicio_03),
    4: ("Área y perímetro de un círculo", ejercicio_04),
    5: ("Conversión de segundos a horas", ejercicio_05),
    6: ("Tabla de multiplicar", ejercicio_06),
    7: ("Operaciones aritméticas básicas", ejercicio_07),
    8: ("Cálculo del IMC", ejercicio_08),
    9: ("Conversión Celsius a Fahrenheit", ejercicio_09),
    10: ("Promedio de 3 números", ejercicio_10),
}


def mostrar_menu():
    print("\n" + "=" * 60)
    print("  TP1 - Estructuras Secuenciales - Programación 1")
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
