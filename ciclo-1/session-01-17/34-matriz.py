#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado miércoles, 28 de junio de 2020

ddados dos matrices A y B, se pide:
hacer un algoritmo que calcule la suma de las matrices
"""
a = [[4, 7, 5], [-1, 2, 5], [3, -2, 5]]
b = [[2, -1, 5], [3, -2, 5], [4, 7, 5]]

# imprimir la matriz a  en forma de matriz
for i in range (len(a)):
    for j in range (len(a[i])):
        print(a[i][j], end =" ")
    print()

# suma de matrices A y B
c = [[],[],[]]
for i in range (len(a)):
    for j in range (len(a[i])):
        c[i].append(a[i][j] + b[i][j])

print (c)
