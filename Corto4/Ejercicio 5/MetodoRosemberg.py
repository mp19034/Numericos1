
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

def regla_del_trapecio_simple(funcion, a, b, tablaValores, formaRespuesta):
    Listado_Resultante = []
    Listado_Resultante_Final = []  # Lista que se mostrar en el formulario

    if funcion != '':

        numerador = Sustituir_y_Evaluar_Funcion(funcion, a, 0, 0) + \
            Sustituir_y_Evaluar_Funcion(funcion, b, 0, 0)
        evaluacion = (b-a)*(numerador/2)

        Listado_Resultante.append(evaluacion)
        Listado_Resultante_Final.append("La respuesta es:"+str(evaluacion))

        if formaRespuesta == 0:
            return Listado_Resultante_Final
        else:
            return Listado_Resultante

    else:  # Para cuando trabajamos con puntos y no con funciones

        tamanio = len(tablaValores[0])
        listaX = tablaValores[0]
        listaY = tablaValores[1]

        if tamanio == 2:
            resultado = (listaX[1]-listaX[0])*((listaY[0]+listaY[1])/2)
            Listado_Resultante.append(resultado)

            Listado_Resultante_Final.append("La respuesta es:"+str(resultado))

            if formaRespuesta == 0:
                return Listado_Resultante_Final
            else:
                return Listado_Resultante

        else:
            print("Para resolver mediante el trapecio simple solo se utilizan 2 puntos")

def regla_del_trapecio_compuesta(funcion, a, b, n, tablaValores, formaRespuesta):

    # respuesta
    Listado_Resultante = []
    Listado_Resultante_Final = []  # Lista que se mostrar en el formulario

    if funcion != '':

        h = (b-a)/n
        aa = a

        lista_con_valor_h = []
        lista_evaluaciones = []
        sumatoria_puntos_medios = 0

        for i in range(0, n+1, 1):
            lista_con_valor_h.append(aa)
            lista_evaluaciones.append(Sustituir_y_Evaluar_Funcion(
                funcion, lista_con_valor_h[i], 0, 0))
            if i >= 1 and i <= n-1:
                sumatoria_puntos_medios += lista_evaluaciones[i]

            # Aumentamos el valor de a en h
            aa += h

        resultado = (
            b-a)*((lista_evaluaciones[0] + 2*sumatoria_puntos_medios + lista_evaluaciones[n]))/(2*n)

        Listado_Resultante.append(resultado)
        Listado_Resultante_Final.append("Respuesta: "+str(resultado))

        if formaRespuesta == 0:
            return Listado_Resultante_Final
        else:
            return Listado_Resultante

    else:

        sumatoria_puntos_medios = 0
        listaX = tablaValores[0]
        listaY = tablaValores[1]
        tamanio = len(listaX)-1

        for i in range(0, tamanio+1, 1):
            if i >= 1 and i <= tamanio-1:

                sumatoria_puntos_medios += listaY[i]

        resultado = (
            b-a)*(listaY[0] + 2*sumatoria_puntos_medios + listaY[tamanio])/(2*tamanio)

        Listado_Resultante.append(resultado)
        Listado_Resultante_Final.append("Respuesta: "+str(resultado))

        if formaRespuesta == 0:
            return Listado_Resultante_Final
        else:
            return Listado_Resultante

def integracion_rosemberg(funcion, a=1, b=4, nivel=5):

    # lista con respuestas
    Listado_Resultante = []
    Listado_Resultante_Final = []

    # lista donde se encontrara el primer nivel
    primer_nivel = []
    n = 2

    for i in range(0, nivel, 1):
        if i == 0:
            valor = regla_del_trapecio_simple(funcion, a, b, [], 1)
            primer_nivel.append((valor[0]).evalf())
        else:
            valor = regla_del_trapecio_compuesta(funcion, a, b, n, [], 1)
            primer_nivel.append(valor[0].evalf())
            n += 2

    # lista que ira cambiando de tamaño con respecto al nivel en el que se encuente
    lista_cambiante = primer_nivel

    # matriz donde estaran los demas niveles
    matriz_con_niveles = []
    matriz_con_niveles.append(primer_nivel)
    lista_nivel = []
    contador_nivel = 3

    for i in range(1, nivel, 1):
        for j in range(1, len(lista_cambiante)):
            if i == 1:
                primer_termino = (4/3)*lista_cambiante[j]
                segundo_termino = (-1/3)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            elif i == 2:
                primer_termino = (16/15)*lista_cambiante[j]
                segundo_termino = (-1/15)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            else:
                primer_termino = ((4**contador_nivel) /
                                  ((4**contador_nivel)-1))*lista_cambiante[j]
                segundo_termino = ((1)/((4**contador_nivel)-1)
                                   )*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)

        matriz_con_niveles.append(lista_nivel)
        lista_cambiante = lista_nivel
        lista_nivel = []
        if i >= 3:
            contador_nivel += 1

    Listado_Resultante = matriz_con_niveles

    #Listado_Resultante_Final.append("Tabla rosemberg:\n\n")

    #Listado_Resultante_Final.append(matriz_con_niveles)
    #print("\n")
    Listado_Resultante_Final.append("Respuesta final: " +
                            str(matriz_con_niveles[len(matriz_con_niveles)-1]))

    return Listado_Resultante_Final
f = sym.sqrt(x*sym.log(x))
print(integracion_rosemberg(f,1,4,5))