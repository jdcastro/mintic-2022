# dados 2 vectores v1 y v2 obtener un 3 vector ordenado sin unir v1 y v2 
# se declaran los dos vectores
v1 = [-1,8,-6,4]
v2 = [5,-2,1,0]

# metodo 1
v3 = []
# se recorren ambos vectores y se agregan al vector v3
for i in range(len(v1)):
    v3.append(v1[i])
for i in range(len(v2)):
    v3.append(v2[i])
# se llama al metodo ordenar y se imprime el vector
v3.sort()
print(v3)

# metodo 2
# se define una funcion que ordene los vectores
def ordenar_vector(vector):
    for i in range(len(vector)):
        for j in range(len(vector)):
            if vector[i] < vector[j]:
                vector[i], vector[j] = vector[j], vector[i]
    return vector
# se llama a la funcion y se imprime un nuevo vector
v4 = ordenar_vector(v1 + v2)
print(v4)
