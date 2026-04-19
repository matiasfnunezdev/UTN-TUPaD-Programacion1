"""
Ejercicio 4
-----------
Crear un programa que pida al usuario el radio de un círculo e imprima por
pantalla su área y su perímetro.

Fórmulas:
    área      = π · r²
    perímetro = 2 · π · r
"""

import math

radio = float(input("Ingresá el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área:      {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
