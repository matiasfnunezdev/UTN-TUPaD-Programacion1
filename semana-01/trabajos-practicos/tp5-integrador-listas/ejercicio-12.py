"""
Ejercicio 12 - Ordenar 8 enteros ingresados por el usuario
----------------------------------------------------------
- Mostrar la lista original.
- Mostrar ordenada de menor a mayor (sorted()).
- Mostrar ordenada de mayor a menor (sorted(..., reverse=True)).
"""

numeros = []
print("Ingresá 8 números enteros:")
for i in range(1, 9):
    valor = input(f"  Número {i}: ").strip()
    while not (valor.lstrip("-").isdigit()):
        print("  Error: ingrese un número entero válido.")
        valor = input(f"  Número {i}: ").strip()
    numeros.append(int(valor))

print("\nLista original:")
for n in numeros:
    print(f"  {n}", end="")
print()

ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

print("\nOrdenada de menor a mayor:")
for n in ascendente:
    print(f"  {n}", end="")
print()

print("\nOrdenada de mayor a menor:")
for n in descendente:
    print(f"  {n}", end="")
print()
