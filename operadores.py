#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 00:52:31 2021

@author: alejo
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
num4 = int(input("Ingresa el cuarto número: "))
a = 50
b = 150

print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 != num2)
print(num3 != num4)

print(a > b or b < a)
print(a < b or b > a)
print(a == b or a >= b)
print(a > b and a > b) 
print(a != b and b > a)
print(not a < b)