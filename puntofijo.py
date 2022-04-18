import numpy as np
def cube_root(x):
    return np.sign(x)*(abs(x)**(1/3.))

def function(x):
  return cube_root(x-1)


def puntofijo(x0, TOL, N_max, g=function):
    """
      Dada una función g definida en los reales dónde g'(x0)<1,
      devuelve un punto fijo de la función g usando el método
      del punto fijo.


      Parámetros:
      * x0: Primera iteración
      * TOL: Diferencia máxima entre dos iteraciones seguidas
      * N_max: Número máximo de iteraciones
      * g: función definida en los reales


      Valor de retorno
      * pf es el punto fijo de la función g(x)
    """
    pf = x0;
    ant = x0 + 1
    for i in range(N_max):
        if abs(pf - ant) <= TOL:
            return pf
        ant = pf
        pf = g(pf)
    return pf, "Numero maximo de iteraciones superado"

dato1 = float(input("Ingrese el valor inicial: "))
dato2 = float(input("Diferencia Ea: "))
dato3 = int(input("Ingrese las iteraciones que desea: "))

print(puntofijo(dato1,dato2,dato3))