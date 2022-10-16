#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio:
# Dado un número num, listar los n primeros números primos 

def primos(num):
    contador_primos = 0     # contador de numeros primos
    listado_primos  = ""    # lista de numeros primos
    # generamos un ciclo para evaluar los numeros

    i = 1
    while contador_primos < num:
        i += 1

        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                break
        else:
            contador_primos += 1
            listado_primos += str(i) + " "

    print("Los primeros", num, "numeros primos son: ", listado_primos)

numero             = int(input("Ingrese la cantidad de numeros primos que quiere listar: "))
primos(numero)
