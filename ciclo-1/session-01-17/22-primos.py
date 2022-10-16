#!/usr/bin/env python

# evalua si un numero es primo o no
# Un número primo es un entero que solamente es divisible por él mismo y la unidad. 

# algoritmo ineficiente.

num = int(input("Ingrese un numero: "))
i = 1
cont = 0

while (i <= num):
    if num % i == 0:
        cont += 1
    i += 1

if cont == 2:
    print("Es primo")
else:
    print("No es primo")
