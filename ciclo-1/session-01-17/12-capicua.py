#!/usr/bin/env python

# opción 1 utilizando el string y reordenandolo (invertirlo)
numero = input("Ingrese un número: ")
num = numero [::-1]
if numero == num:
    print("Es capicua")
else:
    print("No es capicua")
    
# opción 2, utilizando módulo de números 

num2 = int(numero)
invertido = ""
while num2 > 0:
    num3 = num2 % 10 
    num2 = num2 // 10
    invertido = invertido + str(num3)
print(invertido)

if invertido == numero:
    print(" la variable invertido "+str(invertido)+" es capicua")
else:
    print("No es capicua")
    
