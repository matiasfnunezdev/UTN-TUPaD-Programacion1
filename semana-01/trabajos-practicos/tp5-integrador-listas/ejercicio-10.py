"""
Ejercicio 10 - Ventas de 4 productos en 7 días (matriz 4x7)
-----------------------------------------------------------
- Mostrar el total vendido por cada producto.
- Mostrar el día con mayores ventas totales.
- Indicar cuál fue el producto más vendido en la semana.
"""

productos = ["Café", "Té", "Galletas", "Jugo"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventas = [
    [12, 15, 10, 8,  20, 25, 18],
    [5,  7,  6,  4,  9,  10, 8],
    [20, 22, 18, 15, 30, 35, 28],
    [10, 12, 11, 9,  14, 18, 16],
]

print("Matriz de ventas:")
print(f"  {'Producto':<10}", end="")
for d in dias:
    print(f"{d[:3]:>5}", end="")
print(f"{'TOTAL':>8}")
for i in range(len(productos)):
    print(f"  {productos[i]:<10}", end="")
    for v in ventas[i]:
        print(f"{v:>5}", end="")
    print(f"{sum(ventas[i]):>8}")

print("\nTotal vendido por producto:")
totales_producto = []
for i in range(len(productos)):
    total = sum(ventas[i])
    totales_producto.append(total)
    print(f"  {productos[i]}: {total}")

print("\nVentas totales por día:")
totales_dia = []
for j in range(len(dias)):
    suma = 0
    for i in range(len(productos)):
        suma += ventas[i][j]
    totales_dia.append(suma)
    print(f"  {dias[j]}: {suma}")

mayor_dia_idx = 0
for j in range(1, len(totales_dia)):
    if totales_dia[j] > totales_dia[mayor_dia_idx]:
        mayor_dia_idx = j

print(f"\nDía con mayores ventas: {dias[mayor_dia_idx]} ({totales_dia[mayor_dia_idx]} unidades)")

mayor_prod_idx = 0
for i in range(1, len(totales_producto)):
    if totales_producto[i] > totales_producto[mayor_prod_idx]:
        mayor_prod_idx = i

print(f"Producto más vendido: {productos[mayor_prod_idx]} ({totales_producto[mayor_prod_idx]} unidades)")
