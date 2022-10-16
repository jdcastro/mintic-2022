
def rangos_presion(sistolica,diastolica):
    if sistolica < 91 and diastolica < 63:
        return 1
    elif sistolica >= 91 and sistolica <= 134 and diastolica >= 63 and diastolica <= 77:
        return 2
    elif sistolica >= 134 and sistolica <= 162 and diastolica >= 77 and diastolica <= 105:
        return 3
    elif sistolica >= 162 and sistolica <= 188 and diastolica >= 105 and diastolica <= 119:
        return 4
    elif sistolica >= 188 and sistolica <= 201 and diastolica >= 119 and diastolica <= 126:
        return 5
    elif sistolica >= 201 and sistolica <= 214 and diastolica >= 126 and diastolica <= 146:
        return 6
    elif sistolica >= 214 and diastolica >= 146:
        return 7
    elif sistolica >= 152 and diastolica < 79:
        return 8
    else:
        return 0

def categorias(rangos):
    if rangos == 1:
        return [1, 12]
    elif rangos == 2:
        return [0, 0]
    elif rangos == 3:
        return [0, 0]
    elif rangos == 4:
        return [1, 1]
    elif rangos == 5:
        return [1, 8]
    elif rangos == 6:
        return [1, 12]
    elif rangos == 7:
        return [1, 32]
    elif rangos == 8:
        return [1, 20]
    elif rangos == 0:
        return [0, 0]

def porcentaje(vector1,vector2):
    vector1 = [float(i) for i in vector1]
    vector2 = [float(i) for i in vector2]
    porcentaje = []
    for j in range(len(vector1)):
        porcentaje.append((vector1[j]-vector2[j])*100/vector1[j])
    return porcentaje

entrada = input().split()
n = int(entrada[0]) 
m = int(entrada[1]) 
if n < 1:
    while n < 1:
        entrada = input().split()
        n = int(entrada[0])
        m = int(entrada[1])

existencias_all = []

for i in range(n):
    existencias = int(input())
    if existencias < 1:
        while existencias < 1:
            existencias = int(input())
    existencias_all.append(existencias)

existencias_all_copy = existencias_all.copy()


for i in range(m):
    paciente_datos = input().split()
    paciente_sucursal = int(paciente_datos[0])
    paciente_sistolica = int(paciente_datos[1])
    paciente_diastolica = int(paciente_datos[2])
    categoria = rangos_presion(paciente_sistolica,paciente_diastolica)
    dato_medicamentos = categorias(categoria)
    tipo_medicamento = dato_medicamentos[0]
    cantidad_medicamento = dato_medicamentos[1]
    if categoria != 0 and paciente_sucursal <= n:
        existencias_all[paciente_sucursal - 1] -= cantidad_medicamento

porcentaje_existencias = porcentaje(existencias_all_copy,existencias_all)
sucursal_min = min(existencias_all)
sucursal_max = max(existencias_all)
sucursal_min_index = existencias_all.index(sucursal_min)
sucursal_max_index = existencias_all.index(sucursal_max)

print(sucursal_min_index+1, sucursal_min)
print(sucursal_max_index+1, sucursal_max)
for i in range(n):
    print("{} {:.2f}%".format((i+1), porcentaje_existencias[i]))
