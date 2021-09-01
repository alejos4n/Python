#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:32:16 2021

@author: alejo
"""

#ingresamos los datos de la materia y del alumno
materia = input("Ingresa el nombre de la materia: ")
nombrealm = input("Ingresa el nombre del alumno: ")

#obtenemos las notas
pp1 = int(input("Ingrese la nota 1: "))
pp2 = float(input("Ingrese la nota 2: "))
pp3 = float(input("Ingrese la nota 3: "))
ep = float(input("Ingrese el promedio del parcial: "))
ef = float(input("Ingrese la nota del examen final: "))

#calculamos el promedio de las practicas y promedio final
practicas = (pp1 + pp2 + pp3)/ 3
prom = (practicas + 2*ep + 3*ef) /6

#Mostramos los resultados
print("Hola", nombrealm ,"la materia ", materia,"tiene la siguiente nota: ")
print("El promedio final es: ", prom)


variable1 = int(input("Ingresa el primer número: "))

variable2 = int(input("Ingresa el segundo número: "))

resultado = variable1 * variable2

print("El resultado de multiplicacion de ambos numeros es de: {}".format(resultado))