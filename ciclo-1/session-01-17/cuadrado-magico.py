"""
Ejercicio clase 13, 
********************
* Cuadrado Mágico: *
********************
Solicitar un número impar y devolver una matriz con la propiedad de cuadrado mágico.
"""
n = int(input("Tamaño de la matriz cuadrada?: "))
while n <3 or n%2==0:
    n = int(input("debe ser un numero impar positivo: "))  

matriz = [[0]*n for _ in range(n)]
pi = 0        #posicion inicial de la fila
pj = int(n/2) #posicion inicial de la columna
matriz[pi][pj] = 1
for i in range(2,n**2+1):
    pip =   pi
    pjp =   pj
    pi -= 1
    pj += 1
    if pi <0:
         pi = n-1
    if pj >n-1:
        pj = 0
    if matriz[pi][pj] != 0:
        pi = pip +1
        pj = pjp
    matriz[pi][pj] = i

for i in matriz:
    print(i)

"""
verificacion:
Sumar las filas, las columnas y las diagonales, el resultado debe ser igual en todos los casos. 
*** retirar comentarios para verificar
"""
# suma_diagonales = 0
# suma_diagonales_inv = 0
# for i in range(n):
#     print("suma de fila", i, "=", sum(matriz[i]))
#     print("suma de columna", i, "=", sum([matriz[j][i] for j in range(n)]))
#     suma_diagonales += matriz[i][i]
#     suma_diagonales_inv += matriz[i][n-i-1]
# print("suma diagonales: ", suma_diagonales)
# print("suma diagonales inversas: ", suma_diagonales_inv)