"""
Ejercicio 8
-----------
Crear un programa que pida al usuario su altura y su peso e imprima por
pantalla su índice de masa corporal (IMC).

Fórmula:
    IMC = peso (kg) / altura (m)²
"""

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
