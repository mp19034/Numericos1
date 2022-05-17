import numpy as np
import sympy as sp
import cmath

x = sp.Symbol('x')
e = sp.Symbol('e')


def evaluarFuncion(funcion, valor, seDeriva, ordenDerivada):
    funcioon = 0
    if seDeriva == 1:
        if ordenDerivada == 1:
            funcioon = sp.sympify(funcion)
            gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
            return gxValor
        else:
            funcioon = sp.sympify(funcion)
            gxValor = sp.Derivative(funcion, x, 2).subs(
                [(x, valor), (e, 2.7182)])
            return gxValor
    else:
        resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
        return resultado


def interpolacionNewton(puntosX, puntosY, valor):
    listaResultados = []

    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    contador = 2

    # Encontramos los valores de b
    listadeB = []
    listaApollo = []
    listaApollo2 = []
    n2 = len(xi)

    # Desde aca hasta la linea 1322 calculamos los valores de b
    for i in range(0, n, 1):
        if i == 0:
            listadeB.append(fi[i])
        elif i == 1:
            # Encontramos b1
            for j in range(1, n, 1):
                numerador = 1
                denominador = 1
                numerador = numerador * (fi[j] - fi[j - 1])
                denominador = denominador * (xi[j] - xi[j - 1])
                listaApollo.append(numerador / denominador)
                listaApollo2.append(numerador / denominador)

            listadeB.append(listaApollo[0])
            listaApollo = []
        else:
            for j in range(1, len(listaApollo2)):
                numerador = 1
                denominador = 1
                numerador = numerador * (listaApollo2[j] - listaApollo2[j - 1])

                # Simplemente el contador ira aumentando en uno para traer los valores de la lista xi
                denominador = denominador * (xi[contador] - xi[contador - contador])
                listaApollo.append(numerador / denominador)

            # Aumentamos en uno el contador para controlar la posicion de la lista xi
            contador += 1

            listaApollo2 = []

            # Le asignamos los nuevos valores a listaApollo2
            for z in listaApollo:
                listaApollo2.append(z)

            # Agregamos el respectivo valor de b a la listadeB
            listadeB.append(listaApollo2[0])

            # Limpiamos la listaApollo para volver a iterar
            listaApollo = []

    # Desde aqui hasta la linea 1339 hacemos el calculo lineal de los valores de (Xn-Xn-1)---x(X0)
    listadeBLineal = []
    bLineal = 1
    contador2 = 2

    for i in range(0, n):
        if i == 0:
            listadeBLineal.append(1)
        elif i == 1:
            listadeBLineal.append((x - xi[i - 1]))
        else:
            bLineal = 1
            for j in range(0, contador2):
                bLineal = bLineal * (x - xi[j])
            contador2 += 1
            listadeBLineal.append(bLineal)

    polinomio = 0
    for i in range(0, len(listadeB)):
        polinomio = polinomio + listadeB[i] * listadeBLineal[i]

    polinomioSimple = sp.expand(polinomio)

    # Evaluamos el polinomio en el valor a interpolar
    valorInterpolado = evaluarFuncion(polinomioSimple, valor, 0, 0)

    listaResultados.append(polinomioSimple)
    listaResultados.append(valorInterpolado)

    return listaResultados


listaX = [-0.75,-0.7,-0.5,-0.25,-0.1,-0.05]  # valores de X
listaY = [1.27,-1.07,-0.51,-0.13,-0.02,-0.01]  # valores de Y
punto = 3  # Agregar el valor

salida = interpolacionNewton(listaX, listaY, punto)
print(salida)