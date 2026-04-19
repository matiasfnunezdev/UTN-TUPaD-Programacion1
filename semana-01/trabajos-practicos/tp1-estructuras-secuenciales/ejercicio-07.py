"""
Ejercicio 7
-----------
Crear un programa que pida al usuario dos números enteros distintos del 0 y
muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y
restarlos.
"""

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
