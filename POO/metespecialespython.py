#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:37:11 2021

@author: alejo
"""

class FabricaTelefono():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("el objeto {} ha sido creado".format(self.marca))
    
    #destruimos los datos una vez se ejecuten
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefono("Nokia", "Verde")
print(telefono.marca)