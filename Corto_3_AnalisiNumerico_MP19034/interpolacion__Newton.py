import numpy as np
import sympy as Sympy
import cmath

x, e, y, z = Sympy.symbols('x e y z')

#Edwin Omar Mendez De Paz MP19034

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):#Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0 #inicialisamos la funcion en 0
        if seDeriva == 1: #ahora validamos la segunda derivada si es igual a 1
            if ordenDerivada == 1: # validamos si la orden de la derivada es igual a 1 y ordenarlos
                funcioon = Sympy.sympify(funcion)#asignamos las letras segun lo digitado por el usuario
                gxValor = Sympy.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])#guardamos la diferencia
                # de los valores intercambiados los datos de valor son intercambiados por los de x Y los datos de
                #e por math.e
                return gxValor #retornamos el valor encontrado
            else:#sino
                funcioon = Sympy.sympify(funcion)#guardamos en la variable funcioon despues de convertirla a expresion matematica
                gxValor = Sympy.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])#derivamos la funcion y cambiamos las variables por los sustitutos correspondientes
                return gxValor # retornamos los valores retornados
        else:#sino
            resultado = Sympy.sympify(funcion).subs([(x, valor), (e, cmath.e)])# convertimos a funcion matematica
            #y intercambiamos las variables por los sustitutos correspondientes para la ecuacion
            return resultado#retornamos la funcion
    except:
        return "Error"


def interpolacionNewton(puntosX, puntosY, valor):#creamos la funcion y pedimos lo requerido para la interpolacion
    Solucion_Listado = []

    xi = np.array(puntosX)#guardamos en un array el valor del punto x
    fi = np.array(puntosY)#guardamos en un array el valor del punto y

    n = len(xi) #tamanio de xi lo guardamos en n
    contador = 2

    # Encontramos los valores de b
    listadeB = []
    listaApollo = []
    listaApollo2 = []
    n2 = len(xi)

    for i in range(0, n, 1):
        if i == 0:
            print(fi[i])
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
    # Realizamos las multiplicaciones y generamos el polinomio simplificado como le gusta a la ing ^.^
    polinomio = 0
    for i in range(0, len(listadeB)):
        polinomio = polinomio + listadeB[i] * listadeBLineal[i]
    polinomioSimple = Sympy.expand(polinomio)
    # Evaluamos el polinomio en el valor a interpolar
    valorInterpolado = Sustituir_y_Evaluar_Funcion(polinomioSimple, valor, 0, 0)
    Solucion_Listado.append(polinomioSimple)
    Solucion_Listado.append(valorInterpolado)

    return Solucion_Listado

puntoA=[-0.75,-0.7,-0.5,-0.25,-0.1,-0.05]
puntoB=[-1.27,-1.07,-0.51,-0.13,-0.02,-0.01]
funcion=3

print(interpolacionNewton(puntoA,puntoB,funcion))

