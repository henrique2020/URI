while True:
    try: eHora, eMin = map(int, input().split(':'))
    except: break
    
    if (eHora < 7) or (eHora == 7 and eMin == 0): atraso = 0
    else: 
        atraso = 60 + eMin 
        if(eHora < 8): atraso -= (8 - eHora)*60
        else: atraso += (eHora - 8)*60
        
    print('Atraso maximo: {}'.format(atraso))
