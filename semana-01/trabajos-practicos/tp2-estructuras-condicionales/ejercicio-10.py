"""
Ejercicio 10
------------
Preguntar al usuario el hemisferio (N/S), el mes y el día, e indicar
en qué estación del año se encuentra.

Tabla de estaciones (referencia astronómica):
  Período                       | Norte       | Sur
  ----------------------------- | ----------- | -----------
  21 marzo - 20 junio           | Primavera   | Otoño
  21 junio - 22 septiembre      | Verano      | Invierno
  23 septiembre - 20 diciembre  | Otoño       | Primavera
  21 diciembre - 20 marzo       | Invierno    | Verano

Estrategia: primero determinamos el "período" del año a partir del mes y
el día, luego asignamos la estación según el hemisferio.
"""

hemisferio = input("Ingresá tu hemisferio (N/S): ").strip().upper()
mes = int(input("Ingresá el mes (1-12): "))
dia = int(input("Ingresá el día (1-31): "))

if (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
    periodo = "primavera-norte"
elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 22):
    periodo = "verano-norte"
elif (mes == 9 and dia >= 23) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
    periodo = "otoño-norte"
else:
    periodo = "invierno-norte"

if hemisferio == "N":
    if periodo == "primavera-norte":
        estacion = "Primavera"
    elif periodo == "verano-norte":
        estacion = "Verano"
    elif periodo == "otoño-norte":
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif hemisferio == "S":
    if periodo == "primavera-norte":
        estacion = "Otoño"
    elif periodo == "verano-norte":
        estacion = "Invierno"
    elif periodo == "otoño-norte":
        estacion = "Primavera"
    else:
        estacion = "Verano"
else:
    estacion = None

if estacion is None:
    print("Hemisferio inválido. Ingresá N (norte) o S (sur).")
else:
    print(f"Te encontrás en {estacion}.")
