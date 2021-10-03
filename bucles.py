#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

#while

i = 0
while i < 5:
    i += 1
    print("Estoy iterando, voy por el salto: {}".format(i))


#for

numeros = ["uno", "dos", "tres", "cuatro", "cinco"]

for i in numeros:
    print(i)

nombres = ["Alejandro", "Andres", "Luisa", "Silvia"]
for i in nombres:
    print("Feliz día ", i)