import math
import  numpy as np
import sympy as sym

#Calculamos el polinomio de hermite por medio de las derivadas por posicion
                #Creamos las listas que vamos a utilizar
data = []
xi = []
fi = []
fk = []
lx = []
derivada = []
evaluado = []
expresionElevada = []
Hn = []
Kn = []
#Creamos un lista con los nombres de los titulos
titulo = ["k", "Xk", "f(Xk)", "f'(k)"]
#Declaramos la variable a utilizar
x = sym.Symbol('x')
y = 0
num = 1
denom = 1
polinomio = 0
#Pedimos al usuario que ingrese la cantidad de datos
nDatos = int(input("Ingrese la cantidad de datos "))
#Solicitamos que ingrese la cantidad de derivadas
nDerivada = int(input("Ingrese la cantidad de derivada "))
for i in range(nDatos):
    #Pedimos al usuario que ingrese los datos y los almacenamos en las listas
    datoXi = float(input("Ingrese el dato numero x{}: ".format(i)))
    xi.append(datoXi)
    datoFi = float(input("Ingrese el dato numero y{}: ".format(i)))
    fi.append(datoFi)
    datoFk = float(input("Ingrese el dato numero f'{}: ".format(i)))
    fk.append(datoFk)
    data.append([i, datoXi, datoFi, datoFk])
#print(tabulate(data, headers=titulo, tablefmt="pretty"))
# Utilizando el metodo de lagrange
for y in range(0, nDatos, 1):
    num = 1
    denom = 1
    for j in range(0, nDatos, 1):
        if y != j:
            num = num * (x - xi[j])
            denom = denom * (xi[y] - xi[j])
        term = (num / denom)
    lx.append(term)
    polinomio = polinomio + term

# Imprimiendo los datos de L + calculando su derivada
print("\n------ Encontrado el valor de L(n,j) ------")
for z in range(len(lx)):
    #Imprimimoso el valor de L al usuario
    print("L{}: ".format(z), lx[z])
    y = lx[z]
    deri = y.diff(x)
    derivada.append(deri)
    print("L'{}: ".format(z), derivada[z])

print("\n------ Evaluando los valores de x en derivada ------")
# Evaluando los valores de x en derivada
for t in range(len(lx)):
    exp = derivada[t]
    x = xi[t]
    evaluacion = eval(str(exp))
    evaluado.append(evaluacion)
    #imprimimos el valor de L
    print("L'{}(".format(z), x, "): ", evaluacion)
# Encontramos los valores de L
print("\n------ El valor de ln ------")
for u in range(len(lx)):
    lCuadrado = (lx[u]) ** 2
    elevado = lCuadrado.expand()
    expresionElevada.append(elevado)

    print("(L{})^2:".format(u), expresionElevada[u])
# Encontramos los valor de H
print("\n------ Los valores H(n,j) ------")
for q in range(len(lx)):
    #definimos nuestra variable
    x = sym.Symbol('x')
    lCuadrado = expresionElevada[q]
    lEvaluado = evaluado[q]
    formu = (1 - 2 * (lEvaluado) * (x - xi[q]))
    poly = (lCuadrado * formu)
    expre = poly.expand()
    Hn.append(expre)
    #imprimimos los valores de H(n,j)
    print("H{}(x)=".format(q), Hn[q])

# Encontramos los valores de K
print("\n------ Encontrado los valores Kn ------")
for r in range(len(lx)):
    x = sym.Symbol('x')
    lCuadrado = expresionElevada[r]
    formu = ((x - xi[r]))
    poly = (lCuadrado * formu)
    expre = poly.expand()
    Kn.append(expre)
    #Imprimimos los valores de K
    print("K{}(x)=".format(r), Kn[r])

#Una ves teniendo todos los valores
print("\n------ Calculando el polinomio ------")
termino = 1
pol = 0
for g in range(len(lx)):
    primerTermino = (fi[g] * Hn[g])
    segundoTermino = (fk[g] * Kn[g])
    print(primerTermino)
    print(segundoTermino)
    formu = primerTermino + segundoTermino
    print("formula: ", formu)
    termino = termino + formu
pol = pol + termino
poliSim = sym.expand(pol)
funcion = " ", poliSim
print("polinomio: \n", polinomio)
print("\npolinomio Simple: \n", poliSim)

opcion = input("****  ¿Desea evaluar algun punto en X?\n1. Si \n2. No\n")
if opcion == '1':
    x = float(input("Ingrese el valor de x \t"))
    px = eval(str(poliSim))
    print("valor evaluado es: ", px-1)
if opcion == 2:
    print("Programa finalizado")
