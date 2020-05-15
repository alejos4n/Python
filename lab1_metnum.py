# Este codigo ha sido generado por el modulo psexport 20180802-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	print("Ingrese los valores para A, B, C:")
	a = float(input())
	b = float(input())
	c = float(input())
	if b**2<4*a*c:
		print("La ecuacion no tiene valores reales")
	else:
		x = -sqrt(b**2-4*a*c)
		x1 = (-b+x)/(2*a)
		x2 = (-b-x)/(2*a)
		print("x1 = ",x1)
		print("x2 = ",x2)

