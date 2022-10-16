#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022-06-14 15:24:00
# @Author  : Johnny A. De Castro
# @Link    : http://jdcastro.co
# @Version : 1.0

def rangos_presion(sistolica,diastolica):
    if sistolica < 91 and diastolica < 63:
        return True
    elif sistolica >= 91 and sistolica < 134 and diastolica >= 63 and diastolica < 77:
        return False
    elif sistolica >= 134 and sistolica < 162 and diastolica >= 77 and diastolica < 105:
        return False
    elif sistolica >= 162 and sistolica < 188 and diastolica >= 105 and diastolica < 119:
        return True
    elif sistolica >= 188 and sistolica < 201 and diastolica >= 119 and diastolica < 126:
        return True
    elif sistolica >= 201 and sistolica < 214 and diastolica >= 126 and diastolica < 146:
        return True
    elif sistolica >= 214 and diastolica >= 146:
        return True
    elif sistolica >= 152 and diastolica < 79:
        return True
    else:
        return "uncategorized"

n, k, m = map(int, input().split())
while n < 1 or k < 1:
    n, k, m = map(int, input().split())

sucursales = []
for i in range(n):
    sucursales.append(list(map(int, input().split())))
sucursales_prima = sucursales.copy()

pacientes = []
for i in range(m):
    pacientes.append(list(map(int, input().split())))

sucursales_prima = []
for i in range(len(sucursales)):
    sucursales_prima.append(sucursales[i].copy())

def comprobaciones(pacientes,a,b):
    for i in pacientes:
        if rangos_presion(i[3],i[4]) == "uncategorized" and i[0] > a and i[1] > b and i[2] < 0 :
            return False
        else:
            return True

pacientes_descuentan = [0]*n
for i in range(m):
        sucursalp = pacientes[i][0]
        tipo_medicamento = pacientes[i][1]
        cantidad_medicamento = pacientes[i][2]
        sistolica = pacientes[i][3]
        diastolica = pacientes[i][4]
        if comprobaciones(pacientes,n,k) == True:
            pacientes_descuentan[sucursalp-1] += 1
            if rangos_presion(sistolica,diastolica) == True:
                sucursales[sucursalp-1][tipo_medicamento-1] -= cantidad_medicamento

resta_sucursales = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        resta_sucursales[i][j] += sucursales_prima[i][j] - sucursales[i][j]

for i in range(n):
    sucursal = i+1
    print(sucursal)
    # cantidad minima en cada sucursal
    c_minima = min(sucursales[i])
    c_maxima = max(sucursales[i])
    index_minima = sucursales[i].index(c_minima)
    index_maxima = sucursales[i].index(c_maxima)
    cant_minima = sucursales[i][index_minima]
    cant_maxima = sucursales[i][index_maxima]
    print(index_minima+1, cant_minima)
    print(index_maxima+1, cant_maxima)
    if sum(sucursales_prima[i])-sum(sucursales[i]) == 0:
        promedio_programado = 0
        promedio_programadot = 0
    else:
        promedio_programado = (sum(sucursales_prima[i])-sum(sucursales[i]))/len(sucursales_prima[i])
        promedio_programadot = (sum(sucursales_prima[i])-sum(sucursales[i]))/pacientes_descuentan[i]
    print("{:.2f} {:.2f} {:.2f}".format(float(min(resta_sucursales[i])), float(promedio_programado), float(max(resta_sucursales[i]))))
    print("{:.2f}".format(float(promedio_programadot)))

medicamento_tipo_1 = [0]*n
for i in range(n):
    for j in range(k):
        medicamento_tipo_1[i]=resta_sucursales[i][0]

mt1_min = min(medicamento_tipo_1)
mt1_max = max(medicamento_tipo_1)
mt1_index_min = medicamento_tipo_1.index(mt1_min)
mt1_index_max = medicamento_tipo_1.index(mt1_max)
print(mt1_index_min+1, mt1_min)
print(mt1_index_max+1, mt1_max)
