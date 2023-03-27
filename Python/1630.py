import math
while True:
    try: l1, l2 = map(int, input().split())
    except: break
    
    mdc = math.gcd(l1, l2)  #Máximo divisor comum
    l1 = l1 // mdc
    l2 = l2 // mdc
        
    print(2 * (l1 + l2))