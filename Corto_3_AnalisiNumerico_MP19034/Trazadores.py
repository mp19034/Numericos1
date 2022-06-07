import sympy as sp
import numpy as np
import math
import cmath

#Edwin Omar Mendez De Paz MP19034
#
a, b, c, d, e, x = sp.symbols('a b c d e x')


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


def resolverMatrices(listaCoeficientes, listaIndependientes):
    coeficientes = np.matrix(listaCoeficientes)
    independientes = np.matrix(listaIndependientes)

    x = (coeficientes ** -1) * independientes

    return x


def trazadoresCubicos(listaX, listaY):
    listaResultados = []
    intervalos = []
    intervalorsY = []
    listaConCeros = []
    listaCon4Ceros = []
    n = len(listaX)

    for i in range(0, n - 1, 1):
        intervalos.append([listaX[i], listaX[i + 1]])
        intervalorsY.append([listaY[i], listaY[i + 1]])

    listaConCeros = []
    listaCon4Ceros = []

    ecuacionesSimbolicas = []

    soluciones = []
    ecuaciones_Para_Matriz = []

    YParaMatriz = []

    for i in range(0, n - 1, 1):
        YParaMatriz.append([listaY[i]])
        YParaMatriz.append([listaY[i + 1]])

    for i in range(0, n - 1, 1):
        YParaMatriz.append([0])
        YParaMatriz.append([0])

    for i in range(0, len(intervalos) - 1, 1):
        for j in range(0, 4, 1):
            listaConCeros.append(0)

    for i in range(0, 4, 1):
        listaCon4Ceros.append(0)

    contador = 0
    columna = 0
    multiplicadorDeCeros = 0

    for i in range(0, len(intervalos) * 2, 1):
        if i % 2 == 0 and i != 0:
            contador += 1
            multiplicadorDeCeros += 1
            for i in range(0, 4, 1):
                listaConCeros.pop()

        if i < 2:
            ecuaciones_Para_Matriz.append(
                [(intervalos[contador][columna] ** 3), (intervalos[contador][columna] ** 2),
                 (intervalos[contador][columna]), 1] + listaConCeros)
        elif i >= 2:
            ecuaciones_Para_Matriz.append(
                (listaCon4Ceros * multiplicadorDeCeros) + [(intervalos[contador][columna] ** 3),
                                                           (intervalos[contador][columna] ** 2),
                                                           (intervalos[contador][columna]), 1] + listaConCeros)

        if columna == 0:
            columna = 1
        elif columna == 1:
            columna = 0

    columna = 1
    listaConCeros = []
    multiplicadorDeCeros = 0
    # Agregamos 0 del total de variables a encontrar
    for i in range(0, len(intervalos) - 2, 1):
        for j in range(0, 4, 1):
            listaConCeros.append(0)

    for i in range(0, len(intervalos) - 1, 1):  # Primer derivada
        if i == 0:
            ecuaciones_Para_Matriz.append(
                [3 * (intervalos[i][columna] ** 2), 2 * (intervalos[i][columna]), 1, 0,
                 -3 * (intervalos[i + 1][columna - 1] ** 2), -2 * (intervalos[i + 1][columna - 1]), -1,
                 0] + listaConCeros)
        else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
            ecuaciones_Para_Matriz.append(
                (listaCon4Ceros * multiplicadorDeCeros) + [3 * (intervalos[i][columna] ** 2),
                                                           2 * (intervalos[i][columna]), 1, 0,
                                                           -3 * (intervalos[i + 1][columna - 1] ** 2),
                                                           -2 * (intervalos[i + 1][columna - 1]), -1,
                                                           0] + listaConCeros)
        multiplicadorDeCeros += 1

        if i < len(intervalos) - 2:
            # Eliminamos 4 ceros de la lista que contiene todos los ceros
            for j in range(0, 4, 1):
                listaConCeros.pop()

    listaConCeros = []
    multiplicadorDeCeros = 0
    # Agregamos 0 del total de variables a encontrar
    for i in range(0, len(intervalos) - 2, 1):
        for j in range(0, 4, 1):
            listaConCeros.append(0)

    for i in range(0, len(intervalos) - 1, 1):  # Segunda derivada

        if i == 0:
            ecuaciones_Para_Matriz.append(
                [6 * (intervalos[i][columna]), 2, 0, 0, -6 * (intervalos[i + 1][columna - 1]), -2, 0,
                 0] + listaConCeros)

        else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
            ecuaciones_Para_Matriz.append(
                (listaCon4Ceros * multiplicadorDeCeros) + [6 * (intervalos[i][columna]), 2, 0, 0,
                                                           -6 * (intervalos[i + 1][columna - 1]), -2, 0,
                                                           0] + listaConCeros)

        multiplicadorDeCeros += 1

        if i < len(intervalos) - 2:
            # Eliminamos 4 ceros de la lista que contiene todos los ceros
            for j in range(0, 4, 1):
                listaConCeros.pop()

    # Libres que igualamos a cero

    for i in range(0, len(intervalos) - 1, 1):
        for j in range(0, 4, 1):
            listaConCeros.append(0)

    ecuaciones_Para_Matriz.append(
        [6 * (intervalos[0][0]), 2, 0, 0] + listaConCeros)

    ecuaciones_Para_Matriz.append(
        listaConCeros + [6 * (intervalos[len(intervalos) - 1][1]), 2, 0, 0])

    listaDeSoluciones = []
    soluciones = resolverMatrices(
        ecuaciones_Para_Matriz, YParaMatriz)  # Resolvemos la matriz
    # Lista con las respuestas de las variables a b c d
    listaDeSoluciones = np.array(soluciones).flatten().tolist()

    # Aqui formamos las funciones spline ax+b
    contador3 = 0

    for i in range(0, len(intervalos), 1):
        ecuacionesSimbolicas.append(
            listaDeSoluciones[contador3] * x ** 3 + listaDeSoluciones[contador3 + 1] * x ** 2 + listaDeSoluciones[
                contador3 + 2] * x + listaDeSoluciones[contador3 + 3])
        contador3 += 4

        # Aca unimos el intervalo con su funcion respectiva para mostrarlo.
    contador3 = 1
    solucionesEcuaciones = []
    for i in range(0, len(ecuacionesSimbolicas), 1):
        salida = "Intervalo " + \
                 str(intervalos[i]) + " ----> " + "Polinomio: " + str(ecuacionesSimbolicas[i]) + \
                 " ----> " + "Evaluacion: " + \
                 str(evaluarFuncion(ecuacionesSimbolicas[i], 3.14 / 12, 0, 0))
        solucionesEcuaciones.append(salida)
        # print(ecuacionesSimbolicas[i])

    for i in solucionesEcuaciones:
        print(i)


# LISTA DE DONDE IRAN LOS VALORES
listaCoeficientes = [1,2,3,4]  # VALORES DE X
listaIndependientes = [-1,6,31,19]  # VALORES DE Y

trazadoresCubicos(listaCoeficientes, listaIndependientes)
