etnia = input()
etnia_test = True
if  etnia == "AFRODESCENDIENTE" or etnia == "afrodescendiente":
    reconocimiento_etnico = 4
elif etnia == "INDIGENA" or etnia == "indigena":
    reconocimiento_etnico = 5
elif etnia == "RAIZAL" or etnia == "raizal":
    reconocimiento_etnico = 6
elif etnia == "PALENQUERO" or etnia == "palenquero":
    reconocimiento_etnico = 7
elif etnia == "GITANO" or etnia == "gitano":
    reconocimiento_etnico = 8
else :
    reconocimiento_etnico = 0
    etnia_test = False

estrato = input()
estrato_test = True
if   estrato == "1":
    reconocimiento_estrato = 10
elif estrato == "2":
    reconocimiento_estrato = 8
elif estrato == "3":
    reconocimiento_estrato = 6
elif estrato == "4":
    reconocimiento_estrato = 2
elif estrato == "5":
    reconocimiento_estrato = 0
elif estrato == "6":
    reconocimiento_estrato = 0
else:
    reconocimiento_estrato = 0
    estrato_test = False

smmlv = 908526
ingreso = int(input())
if ingreso < smmlv:
    reconocimiento_ingreso = 15
elif ingreso == smmlv :
    reconocimiento_ingreso = 9
elif ingreso >= smmlv*2 and ingreso <= smmlv*3:
    reconocimiento_ingreso = 7
elif ingreso == smmlv*4:
    reconocimiento_ingreso = 4
elif ingreso >= smmlv*5:
    reconocimiento_ingreso = 0
else:
    reconocimiento_ingreso = 0

peso_etnia = 2
peso_estrato = 2
peso_ingreso = 4

resultado = (reconocimiento_etnico * peso_etnia + reconocimiento_estrato * peso_estrato + reconocimiento_ingreso * peso_ingreso)/(peso_etnia + peso_estrato + peso_ingreso)

if etnia_test and estrato_test == True:
    if resultado < 6:
        print("El candidato no continua en el proceso de seleccion")
    elif resultado >= 6:
        print("El candidato continua en el proceso de seleccion")
else:
    print("Se presento un error")
