#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
give the size of the array and the elements of the array and print the array
"""

vector_size = int(input("Digite el tamaño del vector: "))

# method 1:
vector = [int(input("Ingrese un número:")) for i in range(vector_size)]

# method 2:
# vector = []
# for i in range(vector_size):
#     vector.append(int(input("Ingrese un número:")))

print("vector:", vector)

# change the type elements of the vector using the method "map"
flotante = map(float, vector)
print("vector flotante:", list(flotante))