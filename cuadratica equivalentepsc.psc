Algoritmo sin_titulo
	Escribir 'ingrese el valor a'
	Leer a
	Escribir 'ingrese el valor b'
	Leer b
	Escribir 'ingrese el valor c'
	Leer c
	Si a==0 Entonces
		Escribir 'el coeficiente no puede ser igual a cero'
	SiNo
		discriminante <- b^2-4*a*c
		Si discriminante>=0 Entonces
			Si discriminante==0 Entonces
				Escribir 'Error raiz Unica'
			SiNo
				cuadraticaPos <- ((-b)+raiz((b^2)-(4*a*c)))/(2*a)
				cuadraticaNeg <- ((-b)-raiz((b^2)-(4*a*c)))/(2*a)
				Equivalentex1 <- redon((-2*c)/((b)+raiz((b^2)-(4*a*c))))
				Equivalentex2 <- ((-2*c)/((b)-raiz((b^2)-(4*a*c))))
				Escribir 'Calculo de Ecuaciones Cuadraticas +X1 & -X2:\n'
				Escribir 'Su cuadratica positiva es:',cuadraticaPos
				Escribir 'Su cuadratica negativa es:',cuadraticaNeg
				Escribir ''
				Escribir 'Calculo de Ecuaciones Cuadraticas Equivalentes +X1 & -X2:\n'
				Escribir 'Su cuadratica Equivalente positiva es:',Equivalentex1
				Escribir 'Su cuadratica Equivalente negativa es:',Equivalentex2
			FinSi
		SiNo
			Escribir 'Error la ecuaciion tiene una raiz imaginaria'
		FinSi
	FinSi
FinAlgoritmo
