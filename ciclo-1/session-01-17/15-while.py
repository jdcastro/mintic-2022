#!/usr/bin/env python

color = input("Ingrese un color: ")
while not (color == "rojo" or color == "verde" or color == "azul"):
        color = input("Fuera del rango (rojo, verde o azul), ingrese color valído: ")
print("El color es: ", color)

