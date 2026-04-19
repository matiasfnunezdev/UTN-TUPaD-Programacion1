"""
Ejercicio 1 - "Caja del Kiosco"
-------------------------------
Simular una compra con validaciones y cálculo de total.

Validaciones obligatorias:
- Nombre: solo letras, no vacío (usar .isalpha() en while).
- Cantidad de productos: entero positivo > 0 (usar .isdigit() en while).
- Precio de cada producto: entero (usar .isdigit() en while).
- Descuento S/N: aceptar mayúsculas o minúsculas (usar while).
- Sin try/except.

Si tiene descuento, se aplica un 10% al precio del producto.
"""

print("=== CAJA DEL KIOSCO ===\n")

nombre = input("Nombre del cliente: ").strip()
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras y no puede estar vacío.")
    nombre = input("Nombre del cliente: ").strip()

cantidad_str = input("Cantidad de productos: ").strip()
while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad_str = input("Cantidad de productos: ").strip()
cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0.0

for i in range(1, cantidad + 1):
    precio_str = input(f"Producto {i} - Precio: ").strip()
    while not precio_str.isdigit():
        print("Error: el precio debe ser un número entero positivo.")
        precio_str = input(f"Producto {i} - Precio: ").strip()
    precio = int(precio_str)

    descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
    while descuento not in ("s", "n"):
        print("Error: ingrese 'S' o 'N'.")
        descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()

    total_sin_descuento += precio
    if descuento == "s":
        total_con_descuento += precio * 0.9
    else:
        total_con_descuento += precio

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print()
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
