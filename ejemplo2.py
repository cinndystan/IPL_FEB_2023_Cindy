# Operaciones Matemáticas

# Importar librería o biblioteca para funciones matemáticas
import math


# Entrada de datos
# Declarar o crear las variables
número_1 = float(input("Escribe un número: "))
número_2 = float(input("Escribe otro número: "))

# Declarar una Constante
PI = 3.1416

# Procesos (cálculos matemáticos y/o logicos)
suma = número_1 + número_2
resta = número_1 - número_2
mult = número_1 * número_2
div = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1,número_2)
cuadrado = pow(número_1, 2)
cubo = pow(número_2, 3)

raíz_cuad_1 = math.sqrt(9)
raíz_cuad_2 = pow(9, 1/2)
raíz_cubica = pow(27, 1/3)

modulo_residuo = número_1 % número_2



# Salida de datos
print("La suma es =", suma)
print("La suma es = " + str(suma)) #Concatenacion (Unir 2 o mas textos)
# Casteo: Conversion de un tipo de dato en otro tipo de dato
print(f"La suma es = {suma}")

print("La resta es =",resta)
print("La multiplicación es = " + str(mult))
print(f"La división es = {div}")

print(f"Potencia 1 = {round(potencia_1, 2)}")
print(f"Potencia 2 ={round(potencia_2, 3)}")
print("Cuadrado =", cuadrado)
print("Cubo =", cubo)


print(f"Raíz cuadrada 1 = {raíz_cuad_1}")
print("Raíz cuadrada 2 =", raíz_cuad_2)
print(f"Raíz cúbica = {raíz_cubica}")
print("Módulo o residuo = ",modulo_residuo)



