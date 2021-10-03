#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:53:40 2021

@author: alejo
"""

"""
Escribir un programa que pida un numero al usuario y muestre 
las tablas de multiplicar de ese numero
"""

numero = int(input("ingrese un numero: "))
i=0
while i < 10:
    i += 1
    multi = i * numero
    print("Estoy iterando, voy por el salto:", numero ,"x ", i ," = {}".format(multi))

#edad usuario

edad = int(input("ingrese su edad: "))
i = 0
while i < edad:
    i += 1
    print("La edad año a año: {}".format(i))


#ejercicio de for

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    print(i)

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

for i in range(num1, num2 + 1):
    print(i)


































    
