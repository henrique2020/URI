def soma(n1, d1, n2, d2):
    dividendo = (n1*d2)+(n2*d1)
    divisor = d1*d2
    return (dividendo, divisor)

    
def subtracao(n1, d1, n2, d2):
    dividendo = (n1*d2)-(n2*d1)
    divisor = d1*d2
    return (dividendo, divisor)


def multiplicacao(n1, d1, n2, d2): 
    dividendo = n1*n2
    divisor = d1*d2
    return (dividendo, divisor)


def divisao(n1, d1, n2, d2):
    dividendo = n1*d2
    divisor = n2*d1
    return (dividendo, divisor)


def mdc(dividendo: int, divisor: int):
    while divisor != 0:
        r = dividendo % divisor
        dividendo = divisor
        divisor = r
        
    return dividendo


rep = int(input())
for x in range(rep):
    entradas = input().split()
    n1 = int(entradas[0])
    d1 = int(entradas[2])
    n2 = int(entradas[4])
    d2 = int(entradas[6])
    sinal = entradas[3]
    
    if sinal == '+': dividendo, divisor = soma(n1, d1, n2, d2);
    elif sinal == '-': dividendo, divisor = subtracao(n1, d1, n2, d2);
    elif sinal == '*': dividendo, divisor = multiplicacao(n1, d1, n2, d2);
    elif sinal == '/': dividendo, divisor = divisao(n1, d1, n2, d2);
    
    simplificador = mdc(dividendo, divisor)
    dividendo_simplificado = int(dividendo//simplificador)
    divisor_simplificado = int(divisor//simplificador)
    
    print(f'{dividendo}/{divisor} = {dividendo_simplificado}/{divisor_simplificado}')
    
