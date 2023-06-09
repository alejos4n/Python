#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

for i in range(1, 11):
    print(i)

num1 = int(input("ingresa la primera cifra: "))
num2 = int(input("ingresa la segunda cifra: "))

for i in range(num1, num2):
    print(i)

print("ejercicio continue: ")

num1 = int(input("ingresa la primera cifra: "))
num2 = int(input("ingresa la segunda cifra: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        continue
    print(i)

