import math
print("\n")
print("\tBienvenido a la calculadora de Ecuaciones Cuadraticas y sus Equivalentes.")
print("Porfavor ingrese los valora de la cuadratica aX^2+bX+C=0 en su respectivo orden.\n")
a = float(input("Porfavor ingrese el valor de ax^2: "))
b = float(input("Porfavor ingrese el valor de bx: "))
c = float(input("Porfavor ingrese el valor de c: "))
if a==0:
    print("El coeficiente a no puede ser igual a cero")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante>=0 :
        if discriminante==0:
            print("Error raiz Unica")
        else:
            #Con esta formula estariamos calculando la cuadratica
            CuadraticaPos = ((-b)+math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
            CuadraticaNeg = round(((-b)-math.sqrt(pow(b,2)-(4*a*c)))/(2*a),5)
            #Con esta formula calculamos la Cuadratica Equivalente
            Equivalentex1 = round((-2*c)/(b+math.sqrt(pow(b,2)-(4*a*c))),5)
            Equivalentex2 = round((-2*c)/(b-math.sqrt(pow(b,2)-(4*a*c))),5)
            #Aqui vamos a dar las respuestas de nuestros calculos
            print("\n")
            print("Calculo de Ecuaciones Cuadraticas 5 con 5 decimales +X1 & -X2:")
            print(f'Su cuadratica positiva es: {CuadraticaPos}')
            print(f'Su cuadratica Negativa es: {CuadraticaNeg}')
            print("\n")
            print("Calculo de Ecuaciones Cuadraticas Equivalentes +X1 & -X2:")
            print(f'Su cuadratica Equivalente positiva es: {Equivalentex1}')
            print(f'Su cuadratica Equivalente Negativa es: {Equivalentex2}')
    else:
        print("Error la ecuacion tiene una raiz imaginaria")