import cmath
import math
import sympy as Sympy
import sympy as sp
x, e, y, z = Sympy.symbols('x e y z')

def Calculo_Ea(xr, xrAnterior):#Calcula el Error absoluto
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):#Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "Error"

def metodoFalsaPosicion(x1, x2, func, cifr):
    funcion = func
    cifSig = cifr
    es = (10 ** (2 - cifSig)) / 2
    ea = 0
    Solucion_Listado = []
    Solucion_Listado.append(
        ["Iteracion", "X1", "X2", "F(x1)", "F(x2)", "Xr", "F(xr)", "F(x1)*F(Xr)", "Ea"])

    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1

    while salida == 0:
        if contador == 0:
            contador += 1
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
            xr = x1-(fx1*(x1-x2)/(fx1-fx2))
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1*fxr
            if fx1Porfxr == 0:
                Solucion_Listado.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
                print("\n")
            else:
                if fx1Porfxr > 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x1 = xr
                    print("\n")
                else:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x2 = xr
                    print("\n")
        else:
            iteracion += 1
            fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
            fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)
            xr = x1 - (fx1 * (x1 - x2) / (fx1 - fx2))
            fxr = Sustituir_y_Evaluar_Funcion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            ea = Calculo_Ea(xr, valorAnterior)
            print("\n")
            if ea <= es:
                Solucion_Listado.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
                print("\n")
            else:
                if fx1Porfxr == 0:
                    Solucion_Listado.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    salida = 1
                    print("\n")
                else:
                    if fx1Porfxr > 0:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x1 = xr
                        print("\n")
                    else:
                        Solucion_Listado.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x2 = xr
                        print("\n")


    return Solucion_Listado

def factorizarCubicas(a, b, c, soloReal):

    Solucion_Listado = []

    p = ((3*b)-(a**2))/3
    q = (2*(a**3)-(9*a*b)+(27*c))/27

    descriminante = ((q/2)**2)+((p/3)**3)

    if(descriminante == 0):
        if(p == 0 and q == 0):
            x1 = "%.2f" % float(-a/3)
            if soloReal == 1:
                Solucion_Listado.append(x1)
            else:
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
        elif((p*q) != 0):
            x1 = "%.2f" % float((-(3*q)/(2*p))-(a/3))
            x2 = "%.2f" % float((((-4*(p**2))/9*q)-(a/3)))
            if soloReal == 1:
                Solucion_Listado.append(x1)
            else:
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x1)
                Solucion_Listado.append(x2)

    if(descriminante > 0):
        x01 = ((-q/2+(descriminante)**(0.5)))
        x02 = ((-q/2-(descriminante)**(0.5)))

        if x01 < 0:
            x01 = (x01*-1)**(1/3)*(-1)
        else:
            x01 = x01**(1/3)

        if x02 < 0:
            x02 = (x02*-1)**(1/3)*(-1)
        else:
            x02 = x02**(1/3)

        x1 = "%.5f" % float(x01+x02-(a/3))

        # solo devolvemos la raiz real para el metodo de factorizar cuarticas
        if soloReal == 1:
            Solucion_Listado.append(x1)
        else:
            u = (-q/2)+((descriminante)**(0.5))
            v = (-q/2)-((descriminante)**(0.5))

            if u < 0:
                u = (u*-1)**(1/3)*(-1)
            else:
                u = u**(1/3)

            if v < 0:
                v = (v*-1)**(1/3)*(-1)
            else:
                v = v**(1/3)

            x2 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"+" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"
            x3 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"-" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"

            Solucion_Listado.append(x1)
            Solucion_Listado.append(x2)
            Solucion_Listado.append(x3)

    if(descriminante < 0):

        teta = math.acos((-q/2)/(-(p/3)**3)**(1/2))
        x1 = 2*((-p/3)**(1/2))*math.cos((teta+2*0*math.pi)/3)-(a/3)
        x2 = 2*((-p/3)**(1/2))*math.cos((teta+2*1*math.pi)/3)-(a/3)
        x3 = 2*((-p/3)**(1/2))*math.cos((teta+2*2*math.pi)/3)-(a/3)

        if soloReal == 1:
            Solucion_Listado.append(x1)
        else:
            Solucion_Listado.append(x1)
            Solucion_Listado.append(x2)
            Solucion_Listado.append(x3)

    return Solucion_Listado


def factorizarCuarticas(a, b, c, d):
    Solucion_Listado = []
    p = ((8*b)-(3*a**2))/8
    q = ((8*c)-(4*a*b)+a**3)/8
    r = ((256*d)-(64*a*c)+(16*(a**2)*b)-(3*a**4))/256

    # Ahora vamos a resolver la ecuacion cubica : U^3-(p/2)*U^2-R*U + (4pR-Q^2)/8 = 0
    #       (p/2) = aa
    #           R = bb
    # (4pR-Q^2)/8 = cc

    aa = -p/2
    bb = -r
    cc = ((4*p*r)-q**2)/8

    u = factorizarCubicas(aa, bb, cc, 1)
    uu = float(u[0])

    v = ((2*uu)-p)**0.5
    w = (q)/(-2*v)

    # primero calcularemos si no nos dara imaginarias o si

    primerTermino = v**2-4*(uu-w)
    segundoTermino = v**2-4*(uu+w)

    if primerTermino < 0:
        primerTermino = primerTermino*-1
        x1 = str(v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x2 = str(v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x1 = (((v/2)+(primerTermino**0.5)/2))-(a/4)
        x1 = "%.2f" % float(x1)
        x2 = (((v/2)-(primerTermino**0.5)/2))-(a/4)
        x2 = "%.2f" % float(x2)

    if segundoTermino < 0:
        segundoTermino = segundoTermino*-1
        x3 = str(-v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x4 = str(-v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x3 = (((-v/2)+(segundoTermino**0.5)/2))-(a/4)
        x3 = "%.2f" % float(x3)
        x4 = (((-v/2)-(segundoTermino**0.5)/2))-(a/4)
        x4 = "%.2f" % float(x4)

    Solucion_Listado.append(x1)
    Solucion_Listado.append(x2)
    Solucion_Listado.append(x3)
    Solucion_Listado.append(x4)

    return Solucion_Listado


#print (factorizarCuarticas(4,1,-16,-12))

print (metodoFalsaPosicion(0, 1, (e**-x)-x , 3))