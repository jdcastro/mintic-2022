#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dado un vector de numeros enteros digitados por el usuario, 
# crear otro vector con cada número elevado al cuadrado.
# 
# lista_usuario = input("Ingrese una lista de números: "
tanamo_vector = int(input("Digite el tamaño del vector: "))
lista_usuario = [input("Ingrese un número:") for i in range(tanamo_vector)]
lista_cuadrado = [int(i) ** 2 for i in lista_usuario]
print("los numeros ingresados:   ", lista_usuario)
print("lista elevada al cuadrado:", lista_cuadrado)
for i in lista_cuadrado: 
    print(i)