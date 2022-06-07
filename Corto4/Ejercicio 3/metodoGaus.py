import decimal

import sympy as sym
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
def integracion_cuadratura_Gaussiana(funcion, a, b, n):
    # cada sub-lista va a representar un punto
    listaResultado = []
    Listado_Resultante_Final = []
    lista_Wk = [[2], [1, 1], [0.555556, 0.888889, 0.555556], [0.347855, 0.652145, -0.652145, -
                                                              0.347855], [0.236927, 0.478629, 0.568889, 0.478629, 0.236927], [], [], [], [], [], [], []]

    lista_Tk = [[0], [0.57735, -0.57735], [-0.774597, 0, 0.774597], [-0.861136, -0.339981,
                                                                     0.339981, 0.861136], [-0.90618, -0.538469, 0, 0.538469, 0.90618], [], [], [], [], [], [], []]

    lista_variable_Wk = lista_Wk[n-1]
    lista_variable_Tk = lista_Tk[n-1]
    resultado = 0
    punto = 0

    for i in range(0, n, 1):
        punto = ((b-a)*lista_variable_Tk[i] + (b+a))/2
        resultado += lista_variable_Wk[i]*Sustituir_y_Evaluar_Funcion(funcion, punto, 0, 0)

    resultado = resultado*(b-a)/2

    Listado_Resultante_Final.append("Respuesta: "+str(resultado))
    listaResultado.append(resultado)
    return Listado_Resultante_Final

f = (x/x*(1+sym.log(x)))
print (integracion_cuadratura_Gaussiana( f , 1,np.e, 4))