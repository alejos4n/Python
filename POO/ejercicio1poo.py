#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

class Alumno():
    #inicializamos los atributos
    def __init__(self, nombrealumno, nota):
        self.nombrealunmo = nombrealumno
        self.nota = nota
    
    def imprimir(self):
        print("Nombre: {} \n Nota: {}".format(self.nombrealunmo, self.nota))
    
    def resultados(self):
        if self.nota < 7:
            print("Has reprobado")
        else:
            print("has aprobado")

estudiante1 = Alumno("alejo", 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Alumno("eduard", 9)
estudiante2.imprimir()
estudiante2.resultados()
    