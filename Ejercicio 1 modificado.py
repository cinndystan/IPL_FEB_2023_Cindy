# Ejercicio 1 modificado
calif_1 = float(input("Escribe la calificación del primer parcial: "))
calif_2 = float(input("Escribe la calificación del segundo parcial: "))
calif_3 = float(input("Escribe la calificación del tercer parcial: "))

import statistics

prom = statistics.mean([calif_1,calif_3,calif_3])

print(f"El promedio es = {round(prom, 3)}")

if prom >= 6.5 and prom <= 10:
    print("Aprobado")

elif prom > 0 and prom < 6 :
    print("Reprobado")

elif prom == 6:
    print("Panzaste")

elif prom < 0 or prom > 10 :
    print("Inválido")

