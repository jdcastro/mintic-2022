import numpy as np # Importamos la libreria numpy para poder usar el metodo np.arange()
for i in np.arange(1,11,3.6):
    print(i)
   
n = int(input("Cantidad de notas: "))
sum = 0
for c in range(n):
    nota = float(input("Ingrese nota: "))
    sum += nota

promedio = sum / n
print("Promedio: ", promedio)