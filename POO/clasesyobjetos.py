#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""
#creo una clase
class FabricaTelefono():
    #creo los atributos
    marca = "Xiaomi"
    color = "Negro"
    ram = 4
    alma = 64

    #creo el meotodo, metodo = funcion, solo cambia que esta en una clase
    def llamar(self, mensaje):
        return mensaje
    
    def escucharmusica(self):
        print("Estoy escuchando musica")

#Asigno la clase a una variable
telefono = FabricaTelefono()
#muestro un atributo, en este caso la marca
print(telefono.marca)
#imprimo el metodo llamar
print(telefono.llamar("Hola, mesanje desde el metodo llamar de la clase FabricateTelefono"))
#llamo el metodo escuchar musica
telefono.escucharmusica()