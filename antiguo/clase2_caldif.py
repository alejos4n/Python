#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:37:55 2020

@author: alejo
#función creada en la clase de cálculo.
#autor: Profesor Rafael Montoya.

"""

#función creada en la clase de cálculo.
#autor: Profesor Rafael Montoya.

#importamos numpy como np, el alias
#importamos malploit

import numpy as np
import matplotlib.pyplot as plt

#(0, 15, la grafica en eje x va de 0 a 15)
#100 los puntos

x = np.linspace(0, 15, 100)
y = np.sin(x)

plt.plot(x, y)

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x) = sin x")