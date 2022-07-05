import math
def primo(num):
    if num%2 == 0 and num>2:
        return False
    return all(num%i for i in range(3,int(math.sqrt(num))+1, 2))
rep = int(input())

for _ in range(rep):
    var = int(input())
    if (primo(var)):
        print('Prime')
    else:
        print('Not Prime')
