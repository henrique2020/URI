# Problema: 1255 - Frequência de Letras | Resposta: Accepted
# Linguagem: Python 3.11 [+1s]          | Tempo: 0.204s

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']
for _ in range(int(input())):
    text = input().lower()
    
    maior_repeticao = 0
    maior_repeticao_letra = '';
    for letra in alfabeto:
        qtde = text.count(letra)
        if qtde > maior_repeticao:
            maior_repeticao = qtde
            maior_repeticao_letra = letra
        elif qtde == maior_repeticao:
            maior_repeticao_letra += letra
    
    print(maior_repeticao_letra)