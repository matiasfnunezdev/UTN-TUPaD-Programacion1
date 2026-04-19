"""
Ejercicio 2 - 5 productos
-------------------------
- Pedir al usuario que cargue 5 productos.
- Mostrar la lista ordenada alfabéticamente (con sorted()).
- Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""

productos = []
print("Cargá 5 productos:")
for i in range(1, 6):
    nombre = input(f"  Producto {i}: ").strip()
    productos.append(nombre)

ordenados = sorted(productos)
print("\nLista ordenada alfabéticamente:")
for p in ordenados:
    print(f"  - {p}")

a_eliminar = input("\n¿Qué producto desea eliminar?: ").strip()
if a_eliminar in productos:
    productos.remove(a_eliminar)
    print(f"\nProducto '{a_eliminar}' eliminado.")
else:
    print(f"\nEl producto '{a_eliminar}' no se encontró en la lista.")

print("\nLista final actualizada:")
for p in productos:
    print(f"  - {p}")
