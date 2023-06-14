#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

#atributo a usar dentro de la clase
#evita el desbordamiento de memoria
#no se puede acceder desde afuera

class A():
    def __init__(self):
        self.contador = 0
    
    #cuando el contador sea iniciado se sumará 1
    def incrementar(self):
        self.contador += 1
    
    #me retorna el nuevo valor de contador
    def cuenta(self):
        return self.contador

a = A()
print("muestro la cuenta en 0")
print(a.cuenta())
#llamo a contador para que se incremente 1
print("llamo al contador")
a.incrementar()
#vuelvo a mostrar la cuenta
print("muestro nuevamente la cuenta")
print(a.cuenta())
#llamo el contador directamente
print(a.contador)

#repito el proceso con la clase B
class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador

print("ahora muestro la clase B()")
a = B()
print("muestro la cuenta en 0")
print(a.cuenta())
#llamo a contador para que se incremente 1
print("llamo al contador")
a.incrementar()
#vuelvo a mostrar la cuenta
print("muestro nuevamente la cuenta")
print(a.cuenta())
#llamo el contador directamente
#al ejecutar me da error porque los dos guiones bajos __ quieren decir encapsulamiento
print(a.__contador)