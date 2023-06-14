#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:37:11 2021

@author: alejo
"""
class FabricaCel():
    #cuando se usa * es tupla, ** diccionario
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaCel("Nokia", "Azul", "rojo", "verde", m1 = 500, m2 = 100)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
