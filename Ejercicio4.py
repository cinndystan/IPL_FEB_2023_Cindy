# Convertir temperatura °F, K, °C
seleccion= float(input("Elige la unidad de temperatura en la que ingresarás tu dato: 1.°F  2.°C  3.K: "))

if seleccion > 0 and seleccion < 2:

    grados_f= float(input("ingresa la temperatura en °F: "))

    gc = ((grados_f-32)*5)/9
    gk = (((grados_f-32)*5)/9)+273.15

    print("De °F a °C: ", round(gc, 2))
    print("De °F a K: ", round(gk, 2))
          
elif seleccion > 1 and seleccion <3:
    grados_c = float(input("ingresa la temperatura en °C: "))
    
    gk2 = grados_c + 273.15
    gf2 = ((grados_c*9)/5)+32
    
    print("De °C a °F: ", round(gf2, 2))
    print("De °C a K: ", round(gk2, 2))

else:
    grados_k = float(input("ingresa la temperatura en K: "))

    gc3 = grados_k - 273.15
    gf3 = (gc3 * 9/5) + 32

    print("De K a °C: ", round(gc3, 2))
    print("De K a °F: ", round(gf3, 2))




