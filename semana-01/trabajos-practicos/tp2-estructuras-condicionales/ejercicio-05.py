"""
Ejercicio 5
-----------
Permitir introducir contraseñas de entre 8 y 14 caracteres (inclusive).
- Si la longitud está en el rango  → "Ha ingresado una contraseña correcta".
- En caso contrario               → "Por favor, ingrese una contraseña de
                                      entre 8 y 14 caracteres".

Usamos la función len() para obtener la cantidad de caracteres del string.
"""

contrasena = input("Ingresá una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
