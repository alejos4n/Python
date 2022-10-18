#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:24:04 2020

@author: EduardAlejandro_SanchezLopera
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#comentario de prueba
#variable para el ancho de la piscina
a = sp.symbols('a')

#función para el volumen de la piscina
Va = a * (a + 2) * (10 - a)
print("imprimos la función")
print(Va, "\n")

#obtine la primera derivada
d1vda = sp.diff(Va, a)
print("Primera derivada")
print(d1vda, "\n")

#obtiene la segunda derivada
d2vda2 = sp.diff(d1vda, a)
print("segunda derivada")
print(d2vda2, "\n")

#encuentra las raíces de la primera derivada
sp.solve(d1vda, a)

#encuentra números críticos para d1vd = 0, a1= número crítico 1
a1 = float(8/3 - 2*np.sqrt(31)/3)
float(a1)
print("el primer número crítico de la función es:")
print(a1, "\n")

#segundo número crítico
a2 = 8/3 + 2*np.sqrt(31)/3
float(a2)
print("el segundo número crítico de la función es:")
print(a2, "\n")

#obtenemos el valor de la función en el punto crítico 1, fpc1
fpc1 = float(Va.subs(a, a1))
print("Valor de la función en el primer punto crítico")
print (fpc1, "\n")

#obtenemos el valor de la función en el punto crítico 2
fpc2 = float(Va.subs(a, a2))
print("Valor de la función en el segundo punto crítico")
print (fpc2, "\n")

#obtenemos el valor de la primera derivada en el punto crítico 1
fpc1d1 = float(d1vda.subs(a, a1))
print("Valor de la derivada uno en el punto crítico 1 es:")
print(fpc1d1, "\n")

#obtenemos el valor de la primera derivada en el número crítico 2
fpc2d1 = float(d1vda.subs(a, a2))
print("Valor de la derivada uno en el punto crítico 2:")
print(fpc2d1, "\n")

#obtenemos el valor de la segunda derivada en el número crítico 1
fpc1d2 = float(d2vda2.subs(a, a1))
print("Valor de la derivada dos en el punto crítico 1:")
print(fpc1d2, "\n")

#obtenemos el valor de la segunda derivada en el número crítico 2
fpc2d2 = float(d2vda2.subs(a, a2))
print("Valor de la derivada dos en el punto crítico 2:")
print(fpc2d2)

#graficamos
gra = np.linspace(-5, 10, 100)
Va = [i * (i + 2) * (10 - i) for i in gra]

plt.plot(gra, Va)
plt.grid()

plt.title("V(a) = a(a + 2)(10 - a)")
plt.xlabel("a [m]")
plt.ylabel("V(a) [m^3]")

plt.plot(a2, fpc2, "g.")