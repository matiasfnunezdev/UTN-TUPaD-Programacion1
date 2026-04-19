"""
Ejercicio 6
-----------
Solicitar el consumo mensual de energía eléctrica (kWh) e indicar la
categoría:
- Menor que 150 kWh           → "Consumo bajo"
- Entre 150 y 300 (inclusive) → "Consumo medio"
- Mayor que 300 kWh           → "Consumo alto"

Si supera los 500 kWh, mostrar también:
"Considere medidas de ahorro energético".
"""

consumo = float(input("Ingresá el consumo mensual en kWh: "))

if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")
