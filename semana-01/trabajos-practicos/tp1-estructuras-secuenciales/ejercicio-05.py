"""
Ejercicio 5
-----------
Crear un programa que pida al usuario una cantidad de segundos e imprima por
pantalla a cuántas horas equivale.

1 hora = 3600 segundos
"""

segundos = float(input("Ingresá la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.4f} horas")
