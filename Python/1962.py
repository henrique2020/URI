for x in range(int(input())):
    ano = int(input())
    if ano > 2014:
        print(f'{ano-2014} A.C.')
    else:
        print(f'{2015-ano} D.C.')
