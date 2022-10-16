#!/usr/bin/env python
import math
# dado un número decir si es primo o no. 
# Ayuda: 
# Un número primo es un entero que solamente es divisible por él mismo 
# (positivo y negativo) y por la unidad (positiva y negativa).

# ej. 
# N = 5
# COMPROBACIÓN
# 5%1 = 0 --> 5 es primo*
# 5%2 = 1
# 5%3 = 5
# 5%4 = 5
# 5%5 = 0 --> 5 es primo*

numero = int(input("Ingrese un numero: "))
i = 2 #se empieza en 2 porque no es necesario verificar el 1*
if numero == 1:
    print("No es primo")
else:
                # (numero/2+1): # en aras de hacer eficiente el algoritmo, se verifica hasta la mitad del número + 1
                # numero**(1/2) + 1: # se verifica hasta la raiz cuadrada del número + 1
    while i < math.sqrt(numero) + 1:
        if numero % i == 0: # 
            print("No es primo, es divisible por", i)
            break # se rompe el ciclo while si se cumple la condición ya que el modulo es igual 0, es decir es divisible por i, entonces no es primo.
        else:
            i += 1
    else:
        print("Es primo")
