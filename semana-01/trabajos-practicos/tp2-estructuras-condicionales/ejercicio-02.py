"""
Ejercicio 2
-----------
Solicitar la nota del usuario.
- Si la nota es mayor o igual a 6 → "Aprobado".
- En caso contrario           → "Desaprobado".
"""

nota = float(input("Ingresá tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
