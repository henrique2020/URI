while True:
    try: soma = input()
    except: break
    
    n1, soma = soma.split('+')
    n2, r = soma.split('=')
    
    valor_letra = None
    if not n1.isnumeric():
        valor_letra = int(r) - int(n2)
    elif not n2.isnumeric():
        valor_letra = int(r) - int(n1)
    else:
        valor_letra = int(n1) + int(n2)
        
    print(valor_letra)
