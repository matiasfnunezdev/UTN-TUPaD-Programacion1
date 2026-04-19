"""
Ejercicio 9
-----------
Crear un programa que pida al usuario una temperatura en grados Celsius e
imprima por pantalla su equivalente en grados Fahrenheit.

Fórmula:
    °F = (9/5) · °C + 32
"""

celsius = float(input("Ingresá la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")
