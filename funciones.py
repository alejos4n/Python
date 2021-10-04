#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:37:11 2021

@author: alejo
"""

#funciones

def impirimir():
    print("imprimir desde la funcion")

print("imprimiendo desde el print")
impirimir()

def calculadora():
    num1 = 30
    num2 = 20
    resultado = num1 +num2
    print(resultado)

calculadora()

lista = []
num = 0

def pedir():
    i = 0
    while i < 5:
        num = int(input("Ingrese numero: "))
        lista.append(num)
        i += 1

def numeros():
    lista.sort()
    pares = []
    impar = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impar.append(i)
    print(pares)
    print(impar)

pedir()
numeros()
    
    
    
    
    
    
    
    
    
    
    
    
    