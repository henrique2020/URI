#Método zoado
'''
print('I=1 J=7')
print('I=1 J=6')
print('I=1 J=5')
print('I=3 J=9')
print('I=3 J=8')
print('I=3 J=7')
print('I=5 J=11')
print('I=5 J=10')
print('I=5 J=9')
print('I=7 J=13')
print('I=7 J=12')
print('I=7 J=11')
print('I=9 J=15')
print('I=9 J=14')
print('I=9 J=13')
'''


#Método certo
for i in range(1, 10, 2):
    for s in range(6, 3, -1):
        print('I=%d J=%d' % (i, i+s))
