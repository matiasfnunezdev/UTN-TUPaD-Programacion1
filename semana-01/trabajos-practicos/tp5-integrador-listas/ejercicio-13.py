"""
Ejercicio 13 - Ranking de puntajes
----------------------------------
Dada la lista puntajes = [450, 1200, 875, 990, 300, 1500, 640]:
- Mostrar el puntaje más alto y el más bajo.
- Mostrar la lista ordenada de mayor a menor (ranking).
- Indicar en qué posición del ranking se encuentra el puntaje 990.
"""

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print("Puntajes registrados:")
for p in puntajes:
    print(f"  {p}", end="")
print()

print(f"\nPuntaje más alto: {max(puntajes)}")
print(f"Puntaje más bajo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)
print("\nRanking (de mayor a menor):")
for i, p in enumerate(ranking, start=1):
    print(f"  {i}°: {p}")

posicion = ranking.index(990) + 1
print(f"\nEl puntaje 990 ocupa la posición {posicion}° del ranking.")
