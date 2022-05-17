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
    print(puntosX)
    print(puntosY)

    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    contador = 2

    listadeB = []
    listaApollo = []
    listaApollo2 = []
    n2 = len(xi)

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

                denominador = denominador * (xi[contador] - xi[contador - contador])
                listaApollo.append(numerador / denominador)

            contador += 1

            listaApollo2 = []

            for z in listaApollo:
                listaApollo2.append(z)

            listadeB.append(listaApollo2[0])

            listaApollo = []

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

    valorInterpolado = evaluarFuncion(polinomioSimple, valor, 0, 0)

    listaResultados.append(polinomioSimple)
    listaResultados.append(valorInterpolado)

    return listaResultados


puntosX = [1 / 8 * 3.14, 1 / 6 * 3.14, 1 / 4 * 3.14, 1 / 3 * 3.14, 3.14]
puntosY = [0.3552640073, 0.3744507196, 0.4429592654, 0.5963643462, -0.1013211836]
valor = 3.1415 / 12

metodo = interpolacionNewton(puntosX, puntosY, valor)
print(metodo)