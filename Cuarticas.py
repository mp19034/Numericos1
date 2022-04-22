import math
import numpy as np

x4= float(input("Ingrese el valor de X^4: "))
a= float(input("Ingrese el valor de X^3: "))
b= float(input("Ingrese el valor de X^2: "))
c= float(input("Ingrese el valor de X: "))
d= float(input("Ingrese el valor de N: "))

if x4==1:
    p=((8*b)-(3*pow(a,2)))/8
    q=((8*c)-(4*a*b)+pow(a,3))/8
    r=((256*d)-(64*a*c)+(16*(pow(a,2))*b)-3*(pow(a,4)))/256
    #paso 3
    u1=1
    u2=-(p/2)
    u3=-r
    n=((4*p*r)-(pow(q,2)))/8

    #paso 4

    p = (3 * u3 - pow(u2, 2)) / 3  # encontramos p
    q = ((2 * pow(u2, 3)) - (9 * u2 * u3) + (27 * n)) / 27  # Encontramos q
    delta = (pow((q / 2), 2) + pow((p / 3), 3))  # discriminante

    if delta > 0:
        x = (np.cbrt(-(q / 2) + (math.sqrt(delta)))) + (np.cbrt(-(q / 2) - (math.sqrt(delta)))) - (u2 / 3)  # raiz real
        print("Raiz real es: ", x)
        # raiz imaginaria
        u = np.cbrt(-(q / 2) + math.sqrt(delta))  # encontramos u
        v = np.cbrt(-(q / 2) - math.sqrt(delta))  # encontramos v
        x1 = (-(u + v) / 2) - (u2 / 3) + ((math.sqrt(3) / 2) * (u - v))  # evaluamos con positivo
        print("Raiz imaginaria 1: ", x1)
        x2 = (-(u + v) / 2) - (u2 / 3) - ((math.sqrt(3) / 2) * (u - v))  # evaluamos con negativo
        print("La raiz imaginaria 2 es: ", x2)
    elif delta == 0:
        if p == 0 and q == 0:
            x = -(u2 / 3)
            print("Su raiz real es: ", x)
        elif q != 0 and p != 0:
            x = -((3 * q) / (2 * p)) - (u2 / 3)
            x1 = -(pow((4 * p), 2) / (2 * p)) - (u2 / 3)
            print("Raiz simple: ", x)
            print(("Raiz doble: ", x1))
    elif delta < 0:
        teta = math.acos((q / 2) / math.sqrt(-(pow(p / 3), 3)))
        for k in range(3):
            x = (2 * (math.sqrt((-p / 3)))) * math.cos((teta + 2 * k * math.pi) / 3) - (u2 / 3)
            print("La Raiz #", k, " es: ", x)
    v = 
    #aca termina
else:
    x4=x4/x4
    a=a/x4
    b=b/x4
    c=c/x4
    d=d/x4
