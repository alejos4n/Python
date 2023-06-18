#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
    
    #al usa el valor @property no evitamos usar el () al llamar el metodo
    @property
    def cuenta(self):
        return self._cuenta
    
    #usamos set
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, contador):
        return self._contador

a = A()
#mostramos el valor del atributo
print(a.cuenta)
#seteamos un nuevo valor
a.cuenta = 20
print(a.cuenta)
print(a.contador)


