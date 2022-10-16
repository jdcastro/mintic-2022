# dado un número decir si es primo o no. 
# Ayuda: 
# Un número primo es un entero que solamente es divisible por él mismo 
# (positivo y negativo) y por la unidad (positiva y negativa).

numero = int(input("Ingrese un numero: "))
if numero == 1:
    print("No es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")

