#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 00:05:09 2021

@author: alejo
"""

#listas, array o vectores
lista1 = ['pan', 40, 45.5, 'hola']
print("Esto es una lista: ")
print (lista1)

#tupla, no se puede modificar, va en parentesis
print("Esto es una tupla: ")
tupla1 = ("hola", 45, 45.65, "chao")
print(tupla1)

#diccionario, tiene una clave y valor, va con llaves{}

print("Esto es un diccionario: ")
dicci = {"uno": 1, "dos": 2, "tres": 3}
print(dicci)

#
#listas

lista2 = ["tomate", "cebolla", "leche", "arroz"]
lista3 = [1, 2, 3, 4, 5]
lista4 = [6, 7, 8, 9, 10]
lista5 = ['d', 'f', 'a', 'b', 'e', 'c']

print(lista2)
print(lista3)
print(lista4)
print(lista2[1])
print(lista3[2])
print(lista4[3])
print(lista2[1:3])
print(lista3 + lista4)

nueva = lista4.count(8)
print(nueva)

#pide dos datos al usuario y reemplaza el valor 1 y 2 de las lista por los nuevos valores
listan = [20, 50, "curso", 'Python', 3.14]
print("la lista actual es: ", listan)
valor1 = input("ingrese el primer valor: ")
valor2 = input("ingrese el segundo valor: ")
listan[1] = valor1
listan[2] = valor2
print("la lista actual es: ", listan)

#multiplica los valores 4, 7 y 9 de la lista por 2
listab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listab[4] = 2*5
listab[7] = 2*8
listab[9] = 2*10
print(listab)





















