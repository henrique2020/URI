for x in range(int(input())):
    entrada = input()
    cod1 = ''
    for x in entrada:
        if(x.isalpha()):
            cod1+=chr(ord(x)+3)
        else:
            cod1+=x
    cod2 = cod1[::-1]
    cod3 = cod2[:int(len(cod2)/2)]
    for x in range(int(len(cod2)/2), len(cod2)):
        cod3+=chr(ord(cod2[x])-1)
    
    print(cod3)