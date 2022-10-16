def doblar(num,num2):
    return num*num2
    

numeros = [2, 5, 10, 23, 50, 33]
nros = [7, 8, 9, 10, 11, 12]

a = map(doblar, numeros, nros )
print (list(a))