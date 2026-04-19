"""
Ejercicio 9
-----------
Pedir al usuario la magnitud de un terremoto y clasificarla según la
escala de Richter:
- magnitud < 3        → "Muy leve"
- 3 <= magnitud < 4   → "Leve"
- 4 <= magnitud < 5   → "Moderado"
- 5 <= magnitud < 6   → "Fuerte"
- 6 <= magnitud < 7   → "Muy Fuerte"
- magnitud >= 7       → "Extremo"
"""

magnitud = float(input("Ingresá la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")
