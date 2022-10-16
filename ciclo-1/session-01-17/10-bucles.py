# """
# Mientras Que

# Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

# Por ejemplo:
# """


# i = 1
# while i < 6:
#     print(i)
#     i += 1



# print("actividad1")
# # Continuemos integrando los conceptos que hemos visto hasta el momento. 
# # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 
# n = int(input())
# for i in range(2, n):
#     if i%2 == 0:
#         print (i)
# # Comentar las instrucciones anteriores para ejecutar las siguientes


# print("actividad2")
# #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

# x = input()
# z=0
# for i in x:
#     z +=1
# print (z)
# Comentar las instrucciones anteriores para ejecutar las siguientes    
    


print("actividad3")
#Escribe el código que solicite números al usuario hasta que éste ingrese -1.
#Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

numero = float(input("Ingrese numeros:"))
promedio = 0
contador = 0
while numero !=-1:
    promedio += numero
    contador += 1
    numero = float(input("Ingrese numeros:"))

print("el promedio de los numeros es:", promedio/contador)

# Comentar las instrucciones anteriores para ejecutar las siguientes 