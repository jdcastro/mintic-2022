#/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Johnny De Castro
# @Date:   2022-06-17 09:10:00
import csv
def entrega_rangos_presion(sistolica,diastolica):
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
    elif sistolica >= 152 and diastolica < 77:
        return True
    else:
        return "uncategorized"

def leer_base_de_datos(archivo,sucursal):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        contador_total = 0
        contador_hombres = 0
        contador_mujeres = 0
        ubicacion = ''
        total_medicamentos = 0
        for row in reader:
            if row[5] == str(sucursal) and entrega_rangos_presion(int(row[8]),int(row[9])) == True:
                if row[2] == "m":
                    contador_hombres += 1
                elif row[2] == "f":
                    contador_mujeres += 1
                contador_total += 1
                total_medicamentos += int(row[7])
                ubicacion = row[3] + " " + row[4]
                
    return contador_total, contador_hombres, contador_mujeres, ubicacion, total_medicamentos


def main():
    # 1. 
    entrada = int(input())
    while entrada < 1 or entrada > 32: # validacion de entrada
        entrada = int(input())
    archivo = 'data.csv'
    contador_total, contador_hombres, contador_mujeres, ubicacion, total_medicamentos = leer_base_de_datos(archivo,entrada)
    # salidas
    print(f"{entrada} {ubicacion}")
    print("scheduled patients")
    print(f'male {contador_hombres}')
    print(f'female {contador_mujeres}')
    print(f'total {contador_total}')
    print('scheduled medicine quantity')
    print('mean {:.2f}'.format(float(total_medicamentos)/float(contador_total)))
    print(f'total {total_medicamentos}')

if __name__ == '__main__':
    main()
