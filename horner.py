import math

def newtonhotner(n,x0,poli):
    ite=0
    tol=1e-20
    e=100
    pr=n
    lista1=poli
    lista2=poli
    j=1
    r=n

    for k in range(n):
        lista1=lista2
        lista2=[1]*r
        lista1[0]=poli[0]
        lista2[0]=poli[0]
        while e>tol:
            y=lista1
            z=lista1
            i=1
            while i<r:
                y=(x0*y)+lista1[i]
                lista2[j]=y
                j+=1
                z=(x0*z)+y
                i+=1
            y=(x0*y)+lista1[-1]
            xnuevo=x0-(y/z)
            e=abs((xnuevo-x0))
            x0=xnuevo
            ite+=1
            j=1
        r-=1
        print("La raiz ",k+1 ," es:",ite)
        print("")
        e=100
        ite=0

n= int(input("Ingrese el grado del polinomio: "))
polinomio=[1]*(n+1)#lista que guarda los coeficientes

i=0
while i<(n+1):
    print(("Ingrese e coeficiente :",i+1))
    polinomio[i]=float(input())
    i+=1
x0=complex(input("Ingrese el valor de x0 para la primera aproxiacion: "))


print(newtonhotner(n,x0,polinomio))