linha = input().split()
hI, mI, hF, mF = linha
hI = int(hI)
mI = int(mI)
hF = int(hF)
mF = int(mF)

if hI < hF:
	horas = hF - hI
elif hI == hF:
	horas = 24
else:
	horas = 24 - (hI - hF)

if mI < mF:
	minutos = mF - mI
elif mI == mF:
	minutos = 0
else:
	horas = horas-1
	minutos = 60 - (mI - mF)

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(horas, minutos))
