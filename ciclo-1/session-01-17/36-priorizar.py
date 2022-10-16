#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Dado una lista de acreedores ACREEDORES cada uno con 
# NOMBRE, MONTO_TOTAL, MONTO_MENSUAL y PRIORIDAD
# prioridades definidas y cuota mensual definida, priorizar pagos según los recursos disponibles.
# 
# Ejemplo:
# ACREEDORES = [['A', 500000, 100000, 1], ['B', 800000, 200000, 3], ['C', 700000, 300000, 2]]
# RECURSOS = 500000
# 
# Resultado:
# [['A', 400000, 0, 1], ['B', 700000, 100000, 3], ['C', 400000, 0, 2]]

def arrange_array(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][3] < matrix[j][3]:
                matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix

def prioritize(calculate_payments, means):
    for i in range(len(calculate_payments)):
        means_p = means
        means -= calculate_payments[i][2]
        if means > 0:
            calculate_payments[i][2] = 0
        else:
            calculate_payments[i][2] = calculate_payments[i][2] - means_p
            break
    return calculate_payments, means

def main():
    # data:
    acreedores = [['Deus', 500000, 100000, 1], ['B', 800000, 200000, 3], ['H', 700000, 450000, 2], ['C', 700000, 500000, 8], ['D', 700000, 300000, 4]]
    means = 500000
    priorizar = arrange_array(acreedores)
    response, means = prioritize(priorizar, means)
    print(response)
    print(means)

if __name__ == '__main__':
    main()


# transito de sogamoso. $2.500.000
# empresa de mudanza intermunicipales. $2.000.000
# -> guia de mudanza -> empresa de mudanza
# notificacion de incidente 
