"""
Ejercicio 10
------------
Crear un programa que pida al usuario 3 números e imprima por pantalla el
promedio de dichos números.
"""

n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))
n3 = float(input("Ingresá el tercer número: "))

promedio = (n1 + n2 + n3) / 3

print(f"El promedio de {n1}, {n2} y {n3} es: {promedio:.2f}")
