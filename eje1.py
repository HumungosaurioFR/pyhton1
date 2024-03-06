import os
os.system('cls')
total_km_recorrido = 0
etapasint = int(input('Ingrese la cantidad de etapas las cuales quiere recorrer: '))
for i in range(etapasint):
    kilometrosint = int(input('Ingrese la cantidad de kilometros'))
    total_km_recorrido += kilometrosint

print(' la cantidad de etapas es ', etapasint,'y la cantidad de km recorrido', total_km_recorrido)
