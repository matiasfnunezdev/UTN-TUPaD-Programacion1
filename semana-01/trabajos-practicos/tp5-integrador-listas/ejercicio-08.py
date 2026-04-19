"""
Ejercicio 8 - Notas de 5 estudiantes en 3 materias (matriz 5x3)
---------------------------------------------------------------
- Mostrar el promedio de cada estudiante.
- Mostrar el promedio de cada materia.
"""

estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
materias = ["Matemática", "Programación", "Inglés"]

notas = [
    [8, 9, 7],
    [6, 7, 8],
    [10, 9, 9],
    [5, 6, 7],
    [9, 8, 10],
]

print("Notas:")
print(f"  {'Estudiante':<12}", end="")
for m in materias:
    print(f"{m:<14}", end="")
print()
for i in range(len(estudiantes)):
    print(f"  {estudiantes[i]:<12}", end="")
    for nota in notas[i]:
        print(f"{nota:<14}", end="")
    print()

print("\nPromedio por estudiante:")
for i in range(len(estudiantes)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"  {estudiantes[i]}: {promedio:.2f}")

print("\nPromedio por materia:")
for j in range(len(materias)):
    suma = 0
    for i in range(len(estudiantes)):
        suma += notas[i][j]
    promedio = suma / len(estudiantes)
    print(f"  {materias[j]}: {promedio:.2f}")
