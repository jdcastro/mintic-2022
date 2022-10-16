#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Punto de silla
dada una matriz A, encontrar los puntos de silla 
(que el punto mayor de la fila coincida con el menor de la columna)
"""
a = [[3, 4, 5, 3], 
     [2, 3, 2, 2], 
     [1, 2, 0, 1], 
     [4, 5, 1, 0]]

# encontrar el punto de silla
# 1. encontrar el mayor de cada fila

def punto_silla(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    mayor = 0
    mayor_fila = []
    mayores = []
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
        mayor_fila.append([mayor, i])
        mayor = 0
    for i in mayor_fila:
        mayores.append(i)
    # 2. encontrar el menor de cada columna
    minimos = []
    for i in range(columnas):
        minimos.append([min([fila[i] for fila in matriz]),i])
    return mayores, minimos

print(punto_silla(a))

# //To find the Saddle point of the given Matrix
## https://skillpundit.com/python/python-find-saddle-point-given-matrix.php#:~:text=Saddle%20point%20means%20minimum%20element,maximum%20element%20in%20its%20column.
# def findSaddlePoint(mat, n):
# for i in range(0,n):
# min_row = mat[i][0]
# col_ind = 0
# for j in range(1,n):
# if (min_row > mat[i][j]):
# min_row = mat[i][j]
# col_ind = j
# for k in range(0,n):
# if (min_row < mat[k][col_ind]):
# break
# if (k == n):
# print("Value of Saddle Point: ", min_row)
# return True
# return False
# mat= [[1, 2, 3],
# [4, 5, 6],
# [5,4, 6]]
# n = 3
# print("Given matrix is : ")
# print(mat)
# if (findSaddlePoint(mat, n) == False):
# print("No Saddle Point ")