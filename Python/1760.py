import math

while True:
    try: l = int(input())
    except: break

    area = pow(l, 2)*math.sqrt(3)/4
    calculo = 8*area/5 #Fórmula final para ter a Área total do Floco de Neve de Koch
    print('%.2f' % calculo)
