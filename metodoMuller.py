from math import pow, inf
import cmath as cmath
import math

# devuelve un array con los coeficientes de la derivada del polinomio
def derivar(listaCoeficientes):
    # len(listaCoeficientes)-1 de una segunda derivada del polinomio grado 1, es igual a 0
    # pero debemos hacer que sea 1, así que ponemos un if
    derivada = []
    i = 1
    if ((len(listaCoeficientes)) == 1):
        derivada.append(0)
    else:
        # grado del polinomio = len(listaCoeficientes)-1
        while (len(listaCoeficientes) > i):
            derivada.append(listaCoeficientes[i] * i)
            i = i + 1

    return derivada
# Metodo de Bairstow)
def bairstow(coeficientes, r, s, grado, raiz, tolerancia):
    if (grado < 1):  # no hay raices
        return None
    if ((grado == 1) and (coeficientes[1] != 0)):  # saca la única raíz que hay
        raiz.append((float(coeficientes[0]) / float(coeficientes[1])) * (-1))
        return None
    if (grado == 2):
        D = (coeficientes[1] ** 2.0) - (4.0) * (coeficientes[2]) * (coeficientes[0])
        if (D < 0):
            X1 = (-coeficientes[1] - cmath.sqrt(D)) / (2.0 * coeficientes[2])
            X2 = (-coeficientes[1] + cmath.sqrt(D)) / (2.0 * coeficientes[2])
        else:
            X1 = (-coeficientes[1] - math.sqrt(D)) / (2.0 * coeficientes[2])
            X2 = (-coeficientes[1] + math.sqrt(D)) / (2.0 * coeficientes[2])
        raiz.append(X1)
        raiz.append(X2)
        return None
    n = len(coeficientes)
    b = [0] * len(coeficientes)
    c = [0] * len(coeficientes)
    b[n - 1] = coeficientes[n - 1]
    b[n - 2] = coeficientes[n - 2] + r * b[n - 1]
    i = n - 3
    while (i >= 0):
        b[i] = coeficientes[i] + r * b[i + 1] + s * b[i + 2]
        i = i - 1
    c[n - 1] = b[n - 1]
    c[n - 2] = b[n - 2] + r * c[n - 1]
    i = n - 3
    while (i >= 0):
        c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        i = i - 1
    Din = ((c[2] * c[2]) - (c[3] * c[1])) ** (-1.0)
    r = r + (Din) * ((c[2]) * (-b[1]) + (-c[3]) * (-b[0]))
    s = s + (Din) * ((-c[1]) * (-b[1]) + (c[2]) * (-b[0]))
    if (abs(b[0]) > tolerancia or abs(b[1]) > tolerancia):
        return bairstow(coeficientes, r, s, grado, raiz, tolerancia)
    if (grado >= 3):
        Dis = ((r) ** (2.0)) + ((4.0) * (1.0) * (s))
        X1 = (r - (cmath.sqrt(Dis))) / (2.0)
        X2 = (r + (cmath.sqrt(Dis))) / (2.0)
        raiz.append(X1)
        raiz.append(X2)
        return bairstow(b[2:], r, s, grado - 2, raiz, tolerancia)


# Una ves tenemos todos los metodos que usaremos a lo largo del programa
# Empezamos a hacer las operaciones pidiendo el polinomio
print(
    "-----------------------------------------------------------------------------------------------------------------------")
print(
    "\n Hola que tal, soy el programa que te ayudar a a calcular los puntos notables de tu polinomio, así que comencemos:")
print(
    "-----------------------------------------------------------------------------------------------------------------------")

# se asegura de que el grado sea mayor a cero
grado = input("Porfavor, ingresa el grado del polinomio (debe ser mayor a cero): ")
print("\n------------------------------------------------------------------------------------------")
grado = int(grado)
while grado <= 0:
    grado = input("El grado debe ser mayor a cero, porfavor intentelo de nuevo.")
    grado = int(grado)

# Pide los coeficientes al usuario y se los asigna su respectiva x
listaCoeficientes = []
print("Ahora me daras los valores de tu polinomio.:D")
for i in range(grado + 1):
    coef = float(input("Ingresa x^" + str(grado - i) + ": "))
    listaCoeficientes.append(coef)
listaCoeficientes.reverse()

# vas a usar el porcentaje de error relativo y las cifras significativas, para estimar el numero de iteraciones que harás en el algoritno de Newton-Raphson
# Pide las cifras significativas con las que hemos estado trabajando
print("\n------------------------------------------------------------------------------------------")
print("Con cuantas cifras significativas quieres trabajar.:D")
cifrasSignificativas = input("Ingrese las cifras significativas: ")
cifrasSignificativas = int(cifrasSignificativas)
cifras = 1 / pow(10, cifrasSignificativas)

# La variable TOLERANCIA se calcula con la cantidad de cifras significativas.
tolerancia = 0.5 * (10 ** (2 - cifrasSignificativas))

# La variable ERNP guardará el error relativo. Se inicia en 1, para garantizar que es mayor que la tolerancia desde el inicio.
errorRNP = 1

# Primera y segunda derivada
derivada1 = derivar(listaCoeficientes)
derivada2 = derivar(derivada1)
r = listaCoeficientes[0] / listaCoeficientes[-1]
s = r
raiz1 = derivada1[0] / derivada1[-1]
# r2 no importa si el polinomio es de grado 1
if (grado == 1):
    raiz2 = 1
else:
    raiz2 = derivada2[0] / derivada2[-1]

s1 = raiz1
s2 = raiz2

# Raíces de los polinomios
raices = []
raices1 = []
raices2 = []

bairstow(listaCoeficientes, r, s, grado, raices, tolerancia)
bairstow(derivada1, raiz1, s1, grado - 1, raices1, tolerancia)  # raices de la primera derivada
bairstow(derivada2, raiz2, s2, grado - 2, raices2, tolerancia)  # raices de la segunda derivada

# las raices con +0j son normales y nos quedamos solo con la parte real
for i in range(len(raices)):
    if (complex(raices[i]).imag == 0):
        raices[i] = raices[i].real
for i in range(len(raices1)):
    if (complex(raices1[i]).imag == 0):
        raices1[i] = raices1[i].real
for i in range(len(raices2)):
    if (complex(raices2[i]).imag == 0):
        raices2[i] = raices2[i].real

raices1 = [x for x in raices1 if type(x) is not complex]  # si se vacía, no tiene max, min, ni crecec ni decrece
raices2 = [x for x in raices2 if type(x) is not complex]  # si se vacía, no tiene puntos de inflexion ni concavidad

#
# Imprimimos todos los valores obtenidos

# raices
print("\n------------------------------------------------------------------------------------------")
print("\nLas Raices del polinomio son:")
for i in raices:
    print(i)



