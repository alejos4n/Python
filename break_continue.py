#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:44:12 2021

@author: alejo
"""

for i in range(1, 15):
    print(i)
    if i == 10:
        print("me detuve porque soy igual a 10")
        break

for i in range(1, 10):
    if i == 6:
        continue
    print(i)