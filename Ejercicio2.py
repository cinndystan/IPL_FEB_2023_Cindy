# Área del círculo
radio = float(input("Ingresa el radio del círculo en cm: "))
PI = 3.1416

area = PI * pow(radio, 2)
perímetro = 2 * PI * radio

print(f"El área del círculo es: {round(area, 3)}")
print("El perímetro del círculo es:", round(perímetro, 1))

