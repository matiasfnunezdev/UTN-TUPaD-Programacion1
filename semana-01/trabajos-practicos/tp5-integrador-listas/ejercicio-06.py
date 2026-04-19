"""
Ejercicio 6 - Rotación a la derecha
-----------------------------------
Dada una lista con 7 números, rotar todos los elementos UNA posición hacia la
derecha (el último pasa a ser el primero).
"""

numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in numeros:
    print(f"  {n}", end="")
print()

ultimo = numeros[-1]
rotada = [ultimo]
for i in range(len(numeros) - 1):
    rotada.append(numeros[i])

print("\nLista rotada a la derecha:")
for n in rotada:
    print(f"  {n}", end="")
print()
