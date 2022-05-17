import sympy as sp
from sympy.utilities.lambdify import lambdify
x = sp.sympify('x')
e = sp.sympify('e')

#Edwin Omar Mendez De Paz MP19034

def Lagrange_i(data_points, i):

    li, xi = 1, data_points[i][0]

    for j in range(len(data_points)):
        xj = data_points[j][0]

        if j != i:
            li *= (x - xj) / (xi - xj)
    return li

def Lagrange_squared(data_points, i):

    l2 = Lagrange_i(data_points, i) ** 2
    print("Li(x)^2 =" + str(l2))
    print()
    return l2



def Lagrange_Derivative(data_points, i):

    dl = Lagrange_i(data_points, i).diff(x)
    print("L'(x) = " + str(dl))
    print()
    return lambdify(x, dl)


def Hermite_Interpolation(data_points):

    print("\nPara los puntos:\n" + str(data_points) + "\n")
    hermite_function = 0
    for i in range(len(data_points)):
        xi, yi, mi = data_points[i]
        la_squared = Lagrange_squared(data_points, i)
        la_derivative = Lagrange_Derivative(data_points, i)
        hermite_function += (1 - 2*(x - xi) * la_derivative(xi)) * la_squared * yi + (x - xi)*la_squared * mi
        print("H" + str(i) + "(x)=" + str(hermite_function) + "\n")

    h = hermite_function
    dh = hermite_function.diff(x)
    print("\nH(x) = " + str(h) + "\n")
    h = lambdify(x, h)
    dh = lambdify(x, dh)

    for xi, yi, mi in data_points:
        print("x=" + str(xi) + " f(x)=" + str(yi) + " f'(x)=" + str(mi) + " H(x)=" + str(h(xi)) + " H'(x)=" + str(dh(xi)))

    return hermite_function


def Drive():
    """
   obtener datos de usuario y calcular H(x)
   :retorno: Ninguno
"""
    print("por favor, ponga sus puntos de datos de la siguiente manera:\n"
          "|      Primero       |      Segundo    |\n"
          "|--------------------|-----------------|\n"
          "|ValorInicial(X0)=0  | ValorInicial(X1)|\n"
          "|F(X)=COS(1)==1      | F(X1)=COS(-1)   |\n"
          "|F'(X)=-SEN(0)==0    | F'(X1)=-SEN(0)  |\n"
          "|____________________|_________________|\n"
          "Porfavor ingrese estos datos Para El Corto 3")
    data_points = list()
    while True:
        xi = float(input("Valor Buscado: "))
        yi = float(input("F(x): "))
        mi = float(input("F(x)': "))
        data_points.append((xi, yi, mi))

        stop = input("¿Continuar? N - no, cualquier otra tecla - Sí")
        if stop == "n" or stop == "N":
            break

    h = Hermite_Interpolation(data_points)
    print("H(x) = " + str(h))
Drive()