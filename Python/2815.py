texto = input().split()
texto_corrigido = []
for palavra in texto:
    if palavra[0:2] == palavra[2:4]:
        palavra = palavra[2:]
        
    texto_corrigido.append(palavra)

print(' '.join(texto_corrigido))