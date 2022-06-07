
import decimal

import sympy as sym
from numpy.lib.shape_base import column_stack
import sympy as sp
import numpy as np
import math
import cmath


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

def evaluar_formula_Simpson_adapatativo(a, b, funcion):
    puntoS = []
    puntoS = (((b-a)/6)*(Sustituir_y_Evaluar_Funcion(funcion, a, 0, 0)+Sustituir_y_Evaluar_Funcion(funcion,b, 0, 0) + (4 * Sustituir_y_Evaluar_Funcion(funcion, ((a+b)/2), 0, 0))))
    return puntoS
f = x / x* sym.log(x)
print ("Respuesta segun metodo adaptativo: ",evaluar_formula_Simpson_adapatativo(np.e,pow(np.e,2),f))