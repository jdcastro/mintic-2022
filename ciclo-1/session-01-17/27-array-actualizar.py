#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
actualice the array
"""
# method 1:
vector = [7, 5, 2, 3, 6, 5, 6]
print(vector)
posicion = vector.index(6)
vector[posicion] = 10
print(vector)

# method simplifyed:
vector[vector.index(6)] = 10
print(vector)

# method 2:
vector2 = [7, 5, 2, 3, 6, 5]
print (vector2)
c = vector2.index(6)
vector2.pop(c)
vector2.insert(c, 10)
print (vector2)
