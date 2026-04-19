"""
Ejercicio 4
-----------
Solicitar la edad del usuario e indicar a qué categoría pertenece:
- Niño/a      : edad < 12
- Adolescente : 12 <= edad < 18
- Adulto/a joven : 18 <= edad < 30
- Adulto/a    : edad >= 30
"""

edad = int(input("Ingresá tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
