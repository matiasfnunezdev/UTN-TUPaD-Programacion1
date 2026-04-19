"""
Ejercicio 3 - 15 números aleatorios entre 1 y 100
-------------------------------------------------
- Crear una lista con los pares y otra con los impares.
- Mostrar cuántos números tiene cada lista.
"""

import random

numeros = [random.randint(1, 100) for _ in range(15)]

print("Lista generada:")
for n in numeros:
    print(f"  {n}", end="")
print()

pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nPares:")
for p in pares:
    print(f"  {p}", end="")
print(f"\nTotal pares: {len(pares)}")

print("\nImpares:")
for i in impares:
    print(f"  {i}", end="")
print(f"\nTotal impares: {len(impares)}")
