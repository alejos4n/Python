#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:11:46 2021

@author: alejo
"""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print("El número uno,", num1,", es mayor que el número dos, ", num2)
else:
    print("el número dos, ", num2,", es mayor que el número uno,", num1)


#ejericicio

letra = input("Ingrese una letra: ")
#vocal = ["a", "e"] #", i, o, u"

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra =="u":
    print("Es vocal")
else:
    print("No es vocal")

#valor absoluto
absoluto = int(input("ingrese un número: "))

if absoluto > 0:
    print("el número absoluto de ", absoluto , "es ", absoluto)
else:
    abso = (absoluto *(-1))
    print("el valor absoluto es ", abso)

#elif
num5 = int(input("Ingrese el número: "))

if num5 == 1:
    print("El número es uno")
elif num5 == 2:
    print("El número es dos")
elif num5 == 3:
    print("El número es tres")
elif num5 == 4:
    print("El número es cuatro")
elif num5 == 5:
    print("el número es cinco")
else:
    print("el número no está entre el 1 y el 5")

#ejercicio

