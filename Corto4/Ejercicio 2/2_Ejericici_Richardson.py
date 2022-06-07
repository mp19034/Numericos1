import numpy as np
import sympy as sym

x=sym.symbols ('x')

def richardson( f, x0, n ,h ):
    d=np.array( [[0] * (n + 1)]*(n+1),float)
    for i in range (n+1):
        d[i,0]=0.5*(f(x0+h)-f(x0-h))/h

        pd4=1
        for j in range (1,i+1):
            pd4=4*pd4
            d[i,j]=d[i,j-1]+(d[i,j-1]-d[i-1,j-1])/(pd4-1)

        h=0.5*h
    return d

x0=0.9
h=0.15
n=4

def fn(x):
  return ((sym.tan(3*x)) * 1/3)
def fprima(x):
  return sym.diff(fn(x),x)

Derivativedef=sym.lambdify((x),fprima(x),"numpy")
print(fprima(x))

d=richardson(fn,x0,n,h)

er=abs((d[n,n]-Derivativedef(x0))/Derivativedef(x0))
print(d)
print("Aproximacion de la derivacion \n f'({})={}".format(x0,d[n,n]))
print("Valor exacto de la derivada \n f'({})={}".format(x0,Derivativedef(x0)))
print("El error relativo es {}".format(er))