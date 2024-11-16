import math


a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

discriminante = pow ((b**2) - (4*a*c),1/2)

raiz1 = ((-b + discriminante)/(2*a))
raiz2 = ((-b - discriminante)/(2*a))

print("el resultado de la raiz 1 es :",raiz1)
print("el resutaldo de la raiz2 es",raiz2)