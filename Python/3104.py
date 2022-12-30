'''
  Time limit exceeded
'''
#Case 1:
dividendo = int(input())
divisao = int(input())
#print(dividendo%divisao)
print(divmod(dividendo, divisao)[1])

#Case 2:
def magicMod(dividendo, divisor):
    vec = []
    mod = 0
 
    for i in range(0,len(dividendo),1):
        digit = ord(dividendo[i]) - ord('0')
 
        # Update modulo by concatenating
        # current digit.
        mod = mod * 10 + digit
 
        # Update quotient
        quo = int(mod / divisor)
        vec.append(quo)
 
        # Update mod for next iteration.
        mod = mod % divisor    
     
    print(mod)
    
dividendo = input()
divisor = int(input())
magicMod(dividendo, divisor)

'''
  Runtime error
'''
#Case 3:
from math import remainder
dividendo = int(input())
divisao = int(input())
print(remainder(dividendo, divisao))
