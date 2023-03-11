#Obtener un número y determinar lo sig:

numero = float(input("Ingresa un número: "))


if(numero <0 and numero >-100):
    print("cumple")

    for i in range(-1,-101,-2): 
        print(i,"impar")

elif (numero >0 and numero <100):
    print("cumple dos")

    for i in range(0,102,2): 
        print(i,"par")

elif (numero<=-100 or numero ==0 or numero >=100):
    print("Inválido")

