dI = input()
dI = int(dI[4:])
tempo = list(map(int, input().split(' : ')))
hI = tempo[0]
mI = tempo[1]
sI = tempo[2]

dF = input()
dF = int(dF[4:])
tempo = list(map(int, input().split(' : ')))
hF = tempo[0]
mF = tempo[1]
sF = tempo[2]

sD = sF - sI
dD = dF - dI
hD = hF - hI
mD = mF - mI

if sD < 0:
    sD+=60
    mD -= 1

if mD < 0:
    mD+=60
    hD -= 1

if hD < 0:
    hD+=24
    dD -= 1

print('%d dia(s)' % dD)
print('%d hora(s)' % hD)
print('%d minuto(s)' % mD)
print('%d segundo(s)' % sD)
