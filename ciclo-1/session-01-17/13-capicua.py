#!/usr/bin/env python

num = input("Digite un numero: ")

nnum = ""
n = len(num)
i = 1
while (i <= n):
    nnum = nnum + num[-i]
    i = i + 1

print(nnum)


# opcion 2 
nnum = ""
n = len(num)
while (n > 0):
    nnum = nnum + num[n-1]
    n = n - 1

print(nnum)

