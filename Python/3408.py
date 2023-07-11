desvio = 0
for _ in range(int(input())):
    desvio_sl = ''.join(filter(str.isdigit, input()))
    desvio += int(desvio_sl)
    
print(desvio)