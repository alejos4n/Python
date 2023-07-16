#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

#cuando dos objetos ejecutan el mismo metodo

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("yo hago guau")

class Pez(Animales):
    def hablar(self):
        print("yo no hablo")

#creo el objeto perro herdado de la clase Perro
perro = Perro("Guauuuu")
#imprime "yo hago guau", porque viene de la clase Perro y no de Animale
perro.hablar()

animal = Animales("miauuu")
animal.hablar()

pez = Pez("nada")
pez.hablar()
