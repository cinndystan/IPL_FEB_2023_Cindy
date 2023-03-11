# Nivel de una cisterna

nivel_agua= float(input("Ingresa el nivel de la cisterna en metros: "))

if nivel_agua > 6:
    print("Desbordamiento de agua")

elif (nivel_agua >=4 and nivel_agua < 6): 
    print("Desacelerar bomba")

elif (nivel_agua >= 2 and nivel_agua < 4):
    print("Bomba trabajando")

elif (nivel_agua > 0 and nivel_agua < 2):
    print("Acelerar bomba")

elif nivel_agua == 0:
    print("Encender bomba")

elif nivel_agua < 0:
    print("Fuga en cisterna")

elif nivel_agua == 6:
    print("Apagar bomba")   



