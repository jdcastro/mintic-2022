conp = 0 # variable para contar positivos 
conn = 0 # variable para contar negativos

for i in range(10):
    num = float(input("Ingrese un numero: "))
    if num < 0:
        conn = conn + 1    
    else:
        conp = conp + 1

print ("Cantidad de numeros negativos: ", conn)
print ("Cantidad de numeros positivos: ", conp)

