import decimal
from numpy.lib.shape_base import column_stack
import sympy as sp
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth, ln
from numpy.polynomial import Polynomial as P
from sympy.core.function import expand
from sympy.simplify.radsimp import fraction, numer
from fractions import Fraction

x, e, y, z = sp.symbols('x e y z')

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada): #Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs(
                    [(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "Error"

def integracion_simpson_tresOctavos_compuesta(funcion, a, b, n_Intervalos):
    # Variables a utilizar
    h = (b - a)/n_Intervalos  # Distanca de separacion entre punto y punto
    listaX = []  # Aqui guardaremos todos los x

    lista_subIntervalos = []  # Tendra la sima de 1/3 a los valores de x

    sumatoria_Fx = 0  # aqui sumaremos todos los f(x)

    # aqui sumaremos todos los f(x) de los subindices
    sumatoria_Fx_Subindices = 0
    respuesta = 0
    Listado_Resultante_Final = []

    if funcion != "":

        listaX.append(a)  # Agregamos el primer x

        # Agregamos los demas valores de x
        for i in range(0, n_Intervalos, 1):
            listaX.append(listaX[i]+h)

        # Agregamos los sub intervalos
        contador_Dos = 0  # Esta variable ira saltando de dos en dos
        for i in range(0, len(listaX)-1, 1):
            lista_subIntervalos.append(listaX[i]+(1/3))

            lista_subIntervalos.append(lista_subIntervalos[contador_Dos]+1/3)
            contador_Dos += 2

        # for para sumar los x evaluados en la funcion
        for i in range(1, len(listaX)-1, 1):
            sumatoria_Fx += Sustituir_y_Evaluar_Funcion(funcion, listaX[i], 0, 0)

        # for para sumar los subintervalos en la funcion
        for i in range(0, len(lista_subIntervalos), 1):
            sumatoria_Fx_Subindices += Sustituir_y_Evaluar_Funcion(
                funcion, lista_subIntervalos[i], 0, 0)

        respuesta = ((b-a)/(8*n_Intervalos))*(Sustituir_y_Evaluar_Funcion(funcion, listaX[0], 0, 0) +
                                              3*sumatoria_Fx_Subindices +
                                              2*sumatoria_Fx +
                                              Sustituir_y_Evaluar_Funcion(funcion, listaX[len(listaX)-1], 0, 0))

        Listado_Resultante_Final.append("Respuesta: "+str(respuesta))
        return Listado_Resultante_Final

n=0
x = np.zeros(n+1)
print(integracion_simpson_tresOctavos_compuesta( ((math.sin(math.log(x)))/ x), math.e, 1, 6))