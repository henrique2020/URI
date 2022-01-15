teste = 1
while True:
    etapas = int(input())
    if etapas == -1:
        break
    print('Experiment %d: %d full cycle(s)' % (teste, int(etapas/2)))
    teste+=1