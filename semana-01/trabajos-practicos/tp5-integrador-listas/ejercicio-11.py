"""
Ejercicio 11 - Buscar nombre en una lista de 10 estudiantes
-----------------------------------------------------------
- Solicitar al usuario un nombre a buscar.
- Indicar si está y mostrar la posición.
- Si no está, informar que no se encuentra.
"""

estudiantes = [
    "Ana", "Bruno", "Carla", "Diego", "Elena",
    "Fernando", "Gabriela", "Hugo", "Inés", "Julián"
]

print("Lista de estudiantes:")
for i, nombre in enumerate(estudiantes):
    print(f"  [{i}] {nombre}")

buscado = input("\nIngrese el nombre a buscar: ").strip()

if buscado in estudiantes:
    posicion = estudiantes.index(buscado)
    print(f"\n[OK] '{buscado}' se encuentra en la posición {posicion}.")
else:
    print(f"\n[!] '{buscado}' no está en la lista.")
