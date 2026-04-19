"""
Ejercicio 1 - Notas de 10 estudiantes
-------------------------------------
- Mostrar la lista completa.
- Calcular y mostrar el promedio.
- Indicar la nota más alta y la más baja.
"""

notas = [7.5, 8.0, 6.0, 9.5, 4.0, 10.0, 5.5, 7.0, 8.5, 6.5]

print("Notas de los estudiantes:")
for i, nota in enumerate(notas, start=1):
    print(f"  Estudiante {i}: {nota}")

promedio = sum(notas) / len(notas)
print(f"\nPromedio: {promedio:.2f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")
