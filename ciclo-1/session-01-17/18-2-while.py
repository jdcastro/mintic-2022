num = int(input("Ingrese un numero entre 1 y 10: "))
sw = True
while sw:
    intento = int(input("Trata de adivinar el numero: "))
    if intento == num:
        print("Felicidades, adivinaste el numero")
        sw = False
    else:
        if intento > num:
            print("Te pasaste")
        else:
            print("Te falta")

print("ganaste")
