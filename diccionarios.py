#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 21:55:00 2021

@author: alejo
"""

diccionario = {1: "Alejo lop", 2: "Luisa", 3: "andrés"}
print(diccionario)
print(type(diccionario))
print(diccionario[3])
print (2 in diccionario)


paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

valor = input("ingrese un pais: ")
inicial = valor.capitalize() in paises

if inicial == True:
    print(paises[valor.capitalize()])
else:
    print("El pais no está en la lista")

#jugarodres

jugador = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

valor = int(input("ingrese un numero: "))
print(jugador[valor])
