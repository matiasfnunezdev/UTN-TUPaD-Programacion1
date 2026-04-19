"""
Ejercicio 8
-----------
Solicitar el nombre del usuario y una opción (1, 2 o 3):
- 1 → mostrar el nombre en MAYÚSCULAS  (upper())
- 2 → mostrar el nombre en minúsculas   (lower())
- 3 → mostrar el nombre con la primera letra de cada palabra en mayúscula
       (title())
"""

nombre = input("Ingresá tu nombre: ")
opcion = int(input("Elegí una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida. Debe ser 1, 2 o 3.")
