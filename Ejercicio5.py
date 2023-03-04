# Formula general
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

interior_raiz = pow(b, 2)-(4 * a * c)
raiz = pow(interior_raiz, 0.5)

x1 = (- b - raiz)/(2 * a)
x2 = (-b + raiz)/(2 * a)

print("X1 =",x1)
print("X2 =", x2)
