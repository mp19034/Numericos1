import math
import numpy as np
valor1 = float(input("Ingrese el valor del primer numero de la cuadratica x^3"))
a=float(input("Ingrese el valor del segundo numero de la cuadratica x^2"))
b=float(input("Ingrese el valor del tercer numero de la cuadratica x"))
c=float(input("Ingrese el valor del numero de la cuadratica N"))

if valor1 == 1:
    val = a+b
    p = (3*b-pow(a,2))/3 #encontramos p
    q = ((2*pow(a,3))-(9*a*b)+(27*c))/27 #Encontramos q
    delta = (pow((q/2),2)+pow((p/3),3))#discriminante
    if delta>0:
        x=(np.cbrt(-(q/2) + (math.sqrt(delta))))+(np.cbrt(-(q/2) - (math.sqrt(delta)))) - (a/3)#raiz real
        print("Raiz es: ",x)
        #raiz imaginaria
        u=np.cbrt(-(q/2)+math.sqrt(delta))#encontramos u
        v=np.cbrt(-(q/2)-math.sqrt(delta))#encontramos v
        x1=(-(u+v)/2)-(a/3)+ ((math.sqrt(3)/2)*(u-v))#evaluamos con positivo
        print("Raiz imaginaria 1: ",x1)
        x2 = (-(u + v) / 2) - (a / 3) - ((math.sqrt(3) / 2) * (u - v))#evaluamos con negativo
        print("La raiz imaginaria 2 es: ",x2)
    elif delta==0:
        if p==0 and q == 0:
            x = -(a/3)
            print("Su raiz es: ",x)
        elif q!=0 and p!=0:
            x = -((3*q)/(2*p))- (a/3)
            x1 = -(pow((4*p),2)/(2*p))-(a/3)
            print ("Raiz simple: ",x)
            print(("Raiz doble: ",x1))
    elif delta<0:
        teta = math.acos((q/2)/math.sqrt(-(pow((p/3),3))))
        for k in range(3):
            x = (2*(math.sqrt((-p/3))))*math.cos((teta+2*k*math.pi)/3)-(a/3)
            print("La Raiz #",k," es: ",x)
else:

    a =a/valor1
    b =b/valor1
    c =c/valor1
    valor1 = valor1 / valor1
    p = (3 * b - pow(a, 2)) / 3  # encontramos p
    q = ((2 * pow(a, 3)) - (9 * a * b) + (27 * c)) / 27  # Encontramos q
    delta = (pow((q / 2), 2) + pow((p / 3), 3))  # discriminante
    if delta > 0:
        x = (np.cbrt(-(q / 2) + (math.sqrt(delta)))) + (np.cbrt(-(q / 2) - (math.sqrt(delta)))) - (a / 3)  # raiz real
        print("Raiz es: ", x)
        # raiz imaginaria
        u = np.cbrt(-(q / 2) + math.sqrt(delta))  # encontramos u
        v = np.cbrt(-(q / 2) - math.sqrt(delta))  # encontramos v
        x1 = (-(u + v) / 2) - (a / 3) + ((math.sqrt(3) / 2) * (u - v))  # evaluamos con positivo
        print("Raiz imaginaria 1: ", x1)
        x2 = (-(u + v) / 2) - (a / 3) - ((math.sqrt(3) / 2) * (u - v))  # evaluamos con negativo
        print("La raiz imaginaria 2 es: ", x2)
    elif delta == 0:
        if p == 0 and q == 0:
            x = -(a / 3)
            print("Su raiz es: ", x)
        elif q != 0 and p != 0:
            x = -((3 * q) / (2 * p)) - (a / 3)
            x1 = -(pow((4 * p), 2) / (2 * p)) - (a / 3)
            print("Raiz simple: ", x)
            print(("Raiz doble: ", x1))
    elif delta < 0:
        print(p)
        print(q)
        print(delta)
        teta = -(q / 2) /  math.sqrt(-pow((p / 3), 3))
        print ("esta es la teta ",teta)
        teta = np.arccos(teta)
        print (teta)
        for k in range(3):
            x = (2 * math.sqrt(-p / 3)) * math.cos((teta + (2 * k * math.pi)) / 3) - (a / 3)
            print("La Raiz #", k, " es: ", x)
            print ("paso")
