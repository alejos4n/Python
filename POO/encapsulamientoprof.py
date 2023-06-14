#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

#atributo a usar dentro de la clase
#evita el desbordamiento de memoria
#no se puede acceder desde afuera
#por buenas prácticas se usa solo un guión bajo

class A():
    def __init__(self, contador, cuenta):
        self._contador = 0
    
    #cuando el contador sea iniciado se sumará 1
    def incrementar(self):
        self._contador += 1
    
    #me retorna el nuevo valor de contador
    def cuenta(self):
        return self.contador