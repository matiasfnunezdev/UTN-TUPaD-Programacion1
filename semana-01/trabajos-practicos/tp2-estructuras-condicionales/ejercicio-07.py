"""
Ejercicio 7
-----------
Solicitar una frase o palabra al usuario.
- Si termina en vocal → añadir un signo de exclamación al final.
- Si no              → dejar el string tal cual.

Para detectar la última letra usamos el indexado [-1] sobre el string.
Comparamos en minúsculas para cubrir vocales en mayúscula y minúscula.
"""

texto = input("Ingresá una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)
