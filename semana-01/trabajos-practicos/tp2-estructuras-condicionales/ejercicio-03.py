"""
Ejercicio 3
-----------
Permitir ingresar solo números pares.
- Si es par   → "Ha ingresado un número par".
- Si es impar → "Por favor, ingrese un número par".

Para detectar paridad usamos el operador módulo (%).
Un número es par cuando el resto de dividirlo por 2 es 0.
"""

numero = int(input("Ingresá un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
