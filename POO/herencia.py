#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

class Animales():
    def habla(self):
        print("Yo soy un animal")
    
    def descripcion(self):
        print("yo soy un {}".format(self.animal))

class Perro(Animales):
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.habla()
perro = Perro()
perro.habla()
abeja = Abeja("Abeja")
abeja.descripcion()
