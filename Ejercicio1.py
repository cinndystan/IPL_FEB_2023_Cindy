# Variables
calif_1 = float(input("Escribe la calificación del primer parcial: "))
calif_2 = float(input("Escribe la calificación del segundo parcial: "))
calif_3 = float(input("Escribe la calificación del tercer parcial: "))

import statistics

# Operaciones
prom = statistics.mean([calif_1,calif_3,calif_3])

# Salida de datos
print(f"El promedio es = {round(prom, 3)}")

if prom < 5:
    print("Alumno reprobado")

else:
    print("Alumno aprobado")







