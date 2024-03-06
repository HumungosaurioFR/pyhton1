import os
os.system('cls')
riego_papa = 0
riego_yuca = 0
riego_zanahoria = 0

opcionint = int(input('ingre la planta que desea regar\n\n1. Papa\n2. Yuca\n3. Zanahoria\n\n->'))

if opcionint == 1:
    for i in range(3):
        litrosint = int(input('Cuantos litros gastasto hoy'))
        riego_papa += litrosint
    print('la cantidad de litros gastados esta semana fueron: ',riego_papa)

if opcionint == 2:
    for i in range(2):
        litrosint = int(input('Cuantos litros gastasto hoy'))
        riego_yuca += litrosint
    print('la cantidad de litros gastados esta semana fueron: ',riego_yuca)

if opcionint == 3:
    for i in range(2):
        litrosint = int(input('Cuantos litros gastasto hoy'))
        riego_zanahoria += litrosint
    print('la cantidad de litros gastados esta semana fueron: ',riego_zanahoria)