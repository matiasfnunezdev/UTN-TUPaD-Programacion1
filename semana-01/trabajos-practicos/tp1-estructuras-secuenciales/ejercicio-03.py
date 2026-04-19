"""
Ejercicio 3
-----------
Crear un programa que pida al usuario su nombre, apellido, edad y lugar de
residencia e imprima por pantalla una oración con los datos ingresados.

Ejemplo:
    Entrada: Marcos, Pérez, 30, Argentina
    Salida:  Soy Marcos Pérez, tengo 30 años y vivo en Argentina
"""

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
