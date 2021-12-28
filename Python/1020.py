linha = int(input())

ano = linha/365
mes = (linha%365)/30
dia = (linha%365)%30

print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dia)