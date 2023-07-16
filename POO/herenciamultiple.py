#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

class A():
    def primera(self):
        return "esta es la clase A"

class B():
    def segunda(self):
        return "esta es la clase B"

class C(A, B):
    pass

c = C()
#imprimimos el return de la clase A, que viene del objeto c, el cual
#hereda el metodo de la clase A
print(c.primera())
