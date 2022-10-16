#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
give a 2 unidimensional array of integers and return:
addition
subtraction
intercept
"""

# method 1:
vector_1 = [8, 14, 35, 2, 2]
vector_2 = [2, 6, 15, 8, 0]
print("vector_1:", vector_1, "\nvector_2:", vector_2)
adicion = [vector_1[i] + vector_2[i] for i in range(5)]
sustraction = [vector_1[i] - vector_2[i] for i in range(5)]


print("addition:", adicion)
print("sustraction:", sustraction)

intercept = [k for k in vector_1 if k in vector_2]
# or the same as:
lista = []
for i in range(5):
    if vector_1[i] in vector_2:
        lista.append(vector_1[i])
print ("intercept:", lista)
print("intercept:", intercept)
lista = []
# test, ejercicio realizado en la clase. 
for l in vector_1:
    for m in vector_2:
        if l == m: 
            lista.append(m)
            break
print ("en clase: ", lista)


# method 2:
# make a random array of integers
import random
vector1 = [random.randint(0, 20) for i in range(5)]
vector2 = [random.randint(0, 20) for i in range(5)]
print("vector 1:", vector1, "\nvector 2:", vector2)

suma = list(map(lambda x, y: x + y, vector1, vector2))
sustraction = list(map(lambda x, y: x - y, vector1, vector2))
intercept = list(filter(lambda x: x in vector1 and x in vector2, vector1))

print("addition:", suma)
print("sustraction:", sustraction)
print("intercept:", intercept)


