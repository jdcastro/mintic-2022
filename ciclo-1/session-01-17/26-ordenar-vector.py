#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dado un vector de numeros enteros digitados por el usuario, ordenar el vector
# 
lista_usuario = [int(input("Ingrese un número:")) for i in range(int(input("Digite el tamaño del vector: ")))]
for i in range(len(lista_usuario)):
    for j in range(len(lista_usuario)):
        if lista_usuario[i] < lista_usuario[j]:
            lista_usuario[i], lista_usuario[j] = lista_usuario[j], lista_usuario[i]

print("lista ordenada:", lista_usuario)

# print the minimum value in the list
print("El valor mínimo es:", min(lista_usuario))
# print the maximum value in the list
print("El valor máximo es:", max(lista_usuario))


def ordenar_vector(vector):   
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
    return vector