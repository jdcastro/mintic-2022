# dado n decir si es primo o no.

n = int(input("Ingrese un numero: "))
for i in range(2, n):
    if n % i == 0:
        print("No es primo")
        break
else:
    print("Es primo")