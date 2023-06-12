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
    
    #creo un metodo para "reemplazar" el valor de marca
    # y para poder llamar desde afuera de la clase uso la convencion self
    #este va antes del atributo y como parametro del metodo
    def CrearMotorola(self):
        self.marca = "Motorola"

#Creo el objeto telefono
telefono = FabricaTelefono()
#muestro un atributo, en este caso la marca
print(telefono.marca)
#imprimo el metodo llamar
print(telefono.llamar("Hola, mesanje desde el metodo llamar de la clase FabricateTelefono"))
#llamo el metodo escuchar musica
telefono.escucharmusica()
#llamo el metodo nuevo
telefono.CrearMotorola()
print(telefono.marca)


#Para evitar el procedimiento anterior para llamar un atributo
#uso el valor __init__

class FabricaCelulares():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

#cambia la forma en que paso los valores a los atibutos
celular = FabricaCelulares("Iphone", "Azul")
print(celular.marca)
print(celular.color)
