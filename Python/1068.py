def pC(): print('correct')
def pI(): print('incorrect')

while True:
    try: entrada = input()
    except: break
    
    if(entrada.count('(') != entrada.count(')')): pI()
    else: 
        parenteses = list(filter(lambda c: c in ['(', ')'], entrada))
        parenteses_abertos = 0
        for c in parenteses:
            if c == '(': parenteses_abertos += 1
            else: parenteses_abertos -= 1
            
            if parenteses_abertos < 0:
                break
        
        if parenteses_abertos != 0: pI()
        else: pC()
