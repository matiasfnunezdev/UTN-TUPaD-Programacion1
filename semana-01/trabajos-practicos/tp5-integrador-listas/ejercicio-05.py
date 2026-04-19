"""
Ejercicio 5 - Estudiantes presentes
-----------------------------------
- Lista con 8 nombres.
- Preguntar al usuario si quiere agregar o eliminar uno.
- Mostrar la lista final actualizada.
"""

estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Fernando", "Gabriela", "Hugo"]

print("Lista inicial:")
for i, nombre in enumerate(estudiantes, start=1):
    print(f"  {i}. {nombre}")

print("\n¿Qué desea hacer?")
print("  1) Agregar un estudiante")
print("  2) Eliminar un estudiante")
opcion = input("Opción: ").strip()

while opcion not in ("1", "2"):
    print("Error: ingrese 1 o 2.")
    opcion = input("Opción: ").strip()

if opcion == "1":
    nuevo = input("Nombre del nuevo estudiante: ").strip()
    estudiantes.append(nuevo)
    print(f"\n'{nuevo}' agregado.")
else:
    a_eliminar = input("Nombre del estudiante a eliminar: ").strip()
    if a_eliminar in estudiantes:
        estudiantes.remove(a_eliminar)
        print(f"\n'{a_eliminar}' eliminado.")
    else:
        print(f"\n'{a_eliminar}' no se encontró en la lista.")

print("\nLista final actualizada:")
for i, nombre in enumerate(estudiantes, start=1):
    print(f"  {i}. {nombre}")
