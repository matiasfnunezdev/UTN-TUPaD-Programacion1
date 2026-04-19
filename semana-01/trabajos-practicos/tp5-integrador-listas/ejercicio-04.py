"""
Ejercicio 4 - Eliminar duplicados
---------------------------------
Dada una lista con valores repetidos, crear una nueva sin duplicados
preservando el orden de aparición.
"""

original = [1, 3, 5, 3, 7, 1, 9, 5, 11, 7, 13, 9, 15]

print("Lista original:")
for x in original:
    print(f"  {x}", end="")
print()

sin_duplicados = []
for x in original:
    if x not in sin_duplicados:
        sin_duplicados.append(x)

print("\nLista sin duplicados:")
for x in sin_duplicados:
    print(f"  {x}", end="")
print()
