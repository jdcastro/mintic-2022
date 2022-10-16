participantes = int(input())
peso_etnia = 2
peso_estrato = 2
peso_ingreso = 4
continuan = 0
sin_reconocimiento = 0
afro = 0
indio = 0 
raiz = 0
palen = 0 
gitan = 0
estrato_test = True
etnia_test = True

for i in range (participantes):

    etnia = input()
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
    elif etnia == "sin reconocimiento":
        reconocimiento_etnico = 0
    else :
        etnia_test = False

    estrato = input()
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
    elif ingreso >= smmlv and ingreso < smmlv * 2:
        reconocimiento_ingreso = 9
    elif ingreso >= smmlv*2 and ingreso < smmlv*4:
        reconocimiento_ingreso = 7
    elif ingreso >= smmlv*4 and ingreso < smmlv*5:
        reconocimiento_ingreso = 4
    elif ingreso >= smmlv*5:
        reconocimiento_ingreso = 0

    resultado = (reconocimiento_etnico * peso_etnia + reconocimiento_estrato * peso_estrato + reconocimiento_ingreso * peso_ingreso)/(peso_etnia + peso_estrato + peso_ingreso)
    if etnia_test and estrato_test == True:
        if resultado >= 6:
            continuan = continuan + 1
        if etnia == "SIN RECONOCIMIENTO" or etnia == "sin reconocimiento": sin_reconocimiento = sin_reconocimiento + 1
        elif etnia == "AFRODESCENDIENTE" or etnia == "afrodescendiente": afro = afro + 1
        elif etnia == "INDIGENA" or etnia == "indigena": indio = indio + 1
        elif etnia == "RAIZAL" or etnia == "raizal": raiz = raiz + 1
        elif etnia == "PALENQUERO" or etnia == "palenquero": palen = palen + 1
        elif etnia == "GITANO" or etnia == "gitano": gitan = gitan + 1
    else :
        break

print (continuan)
print ("sin reconocimiento", sin_reconocimiento)
print ("afrodescendiente", afro)
print ("indigena", indio)
print ("raizal", raiz)
print ("palenquero", palen)
print ("gitano", gitan)