risada = ''
for l in input():
    if l in "aeiou": risada += l
    
if(risada == risada[::-1]): print("S")
else: print("N")