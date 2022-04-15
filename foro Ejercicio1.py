import math

a = float(input("Ingrese coeficiente a:"))
b = float(input("Ingrese coeficiente b:"))
c = float(input("Ingrese coeficiente c:"))

if a==0:
    print("El coeficiente a no puede ser igual a cero")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        if discriminante == 0:
            x = -b / (2 * a)
            print("La raíz única es {:.3f}".format(x))
        else:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print("La raíz real x1 es {:.3f}".format(x1))
            print("La raíz real x2 es {:.3f}".format(x2))
    else:
        print("Error la raiz es imaginaria")