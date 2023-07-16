#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        #heredamos el metodo init de la clase animales
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro("perrito", "guuau")
#traemos con print, se debe usar el método set
print(perro.sonido)
print(perro.nombre)