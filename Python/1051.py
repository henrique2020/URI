renda = float(input())
if renda <= 2000:
    print('Isento')
else:
    imposto = 0
    percentual_2k = 0.08     #8% => 8/100 = 0.08
    percentual_3k = 0.18    #18% => 18/100 = 0.18
    percentual_4k = 0.28    #28% => 28/100 = 0.28
    if renda >= 4500:
        imposto += 1000*percentual_2k + 1500*percentual_3k + (renda-4500)*percentual_4k #1000->2K + 1500->3K + (renda-4.5K[2K+1K+1.5K])->+4K
    elif(renda <= 4500 and renda > 3000):
        imposto += 1000*percentual_2k + (renda-3000)*percentual_3k #1000->2K + (renda-3K[2K+1K])->3K
    else:
        imposto += (renda-2000)*percentual_2k   #(renda-2K)->2K

    print('R$ %.2f' % imposto)