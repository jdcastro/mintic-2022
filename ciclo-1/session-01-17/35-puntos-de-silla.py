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
