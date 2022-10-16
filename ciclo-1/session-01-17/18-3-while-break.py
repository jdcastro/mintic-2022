num = int(input("Ingrese un numero entre 1 y 10: "))

while True:
    intento = int(input("Trata de adivinar el numero: "))
    if intento == num:
        print("Felicidades, adivinaste el numero")
        break
    else:
        if intento > num:
            print("Te pasaste")
        else:
            print("Te falta")

print("ganaste")
