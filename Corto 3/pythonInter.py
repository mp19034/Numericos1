import math
import  numpy as np
import sympy as sym
#from tabulate import tabulate
import matplotlib.pyplot as plt

xi = np.array([0, 1, 2, 3, 4, 5, 6])
fi = np.array([1, math.e, math.e**2, math.e**3, math.e**4, math.e**5,math.e**6])

# PROCEDIMIENTO
# Tabla de Diferencias Divididas Avanzadas
titulo = ['i   ', 'xi  ', 'fi  ']
n = len(xi)
ki = np.arange(0, n, 1)
tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
tabla = np.transpose(tabla)

# diferencias divididas vacia
dfinita = np.zeros(shape=(n, n), dtype=float)
tabla = np.concatenate((tabla, dfinita), axis=1)

# Calcula tabla, inicia en columna 3
[n, m] = np.shape(tabla)
diag = n - 1
j = 3
while (j < m):
        # Añade título para cada columna
        titulo.append('f[' + str(j - 2) + ']')
        # cada fila de columna
        i = 0
        paso = j - 2  # inicia en 1
        while (i < diag):
                denom = (xi[i + paso] - xi[i])
                num = tabla[i + 1, j - 1] - tabla[i, j - 1]
                tabla[i, j] = num / denom
                i = i + 1
                diag = diag - 1
                j = j + 1

                # pol con diferencias Divididas
                # caso: puntos equidistantes en eje x
        dDividida = tabla[0, 3:]
        n = len(dfinita)

        # expresión del pol con Sympy
        x = sym.Symbol('x')
        pol = fi[0]
        for j in range(1, n, 1):
            factor = dDividida[j - 1]
            term = 1
            for k in range(0, j, 1):
                term = term * (x - xi[k])
            pol = pol + term * factor

        # simplifica multiplicando entre (x-xi)
        polSimp = pol.expand()

        # pol para evaluacion numérica
        px = sym.lambdify(x, polSimp)
        print("El valor del punto es", px(2.3))

        # Puntos para la gráfica
        muestras = 101
        a = np.min(xi)
        b = np.max(xi)
        pxi = np.linspace(a, b, muestras)
        pfi = px(pxi)

        # SALIDA
        np.set_printoptions(precision=4)
        print('Tabla Diferencia Dividida')
        print([titulo])
        print(tabla)
        #print(tabulate(tabla, headers=titulo, tablefmt="pretty"))
        print('dDividida: ')
        print(dDividida)
        print('pol: ')
        print(pol)
        print('pol simplificado: ')
        print(polSimp)
        break;