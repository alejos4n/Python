#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:37:11 2021

@author: alejo
"""

#parametro: variable a utilizar cuando se crea la funcion
#argumento: valor que se le asigna a un parametro

#creo la funcion suma
def suma():
    num1 = 20
    num2 = 30
    suma = num1 + num2
    return suma

print(suma())

#en le codigo anterior cada vez que llamo la funcion suma(), viene con esas variables
#haciendo que la suma siempre sea 50

#ahora creo la funcion suma con los parametros
def suma1(num1, num2):
    suma1 = num1 + num2
    return suma1

#afuera de la funcion hago un print pasando los argumentos
#asi la variable num1 y num2 tendran valores
print(suma1(10, 20))

#solicitamos al usuario valores para con esos valores dar arguemntos a suma1

a = int(input("ingresa un numero: "))
b = int(input("ingresa otro numero mas: "))
print(suma1(a,b))