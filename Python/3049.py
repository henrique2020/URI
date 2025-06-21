metade = (70*160) / 2
corte = (70 * (int(input()) + int(input()))) / 2
print(1 if corte > metade else 
      2 if corte < metade else 0)