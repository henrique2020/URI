while True:
    try: string = input().lower()
    except: break

    m = True    #Especifica se a letra precisa ser maiúscula
    for l in string:
        if 'a' <= l <= 'z':
            if(m):
                l = l.upper()
                m = False
            else:
                m = True;
        
        print(l, end='')

    print();