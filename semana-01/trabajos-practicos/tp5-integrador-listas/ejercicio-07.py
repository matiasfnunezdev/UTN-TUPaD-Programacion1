"""
Ejercicio 7 - Temperaturas semanales (matriz 7x2)
-------------------------------------------------
Cada fila representa un día con [mínima, máxima].
- Calcular el promedio de las mínimas y el de las máximas.
- Mostrar en qué día se registró la mayor amplitud térmica.
"""

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

temperaturas = [
    [12, 22],
    [10, 19],
    [13, 25],
    [14, 28],
    [11, 23],
    [9,  20],
    [8,  17],
]

print("Temperaturas de la semana:")
for i in range(len(dias)):
    print(f"  {dias[i]:<10} | mín: {temperaturas[i][0]}°C | máx: {temperaturas[i][1]}°C")

suma_min = 0
suma_max = 0
for fila in temperaturas:
    suma_min += fila[0]
    suma_max += fila[1]

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

print(f"\nPromedio mínimas: {prom_min:.2f}°C")
print(f"Promedio máximas: {prom_max:.2f}°C")

mayor_amplitud = -1
dia_amplitud = ""
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = dias[i]

print(f"\nMayor amplitud térmica: {dia_amplitud} ({mayor_amplitud}°C)")
