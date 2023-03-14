#https://www.beecrowd.com.br/judge/pt/problems/view/1100
sub = ord('a') - 1
pulos = {'31': {'l': 2, 'n': 1}, '13': {'l': 2, 'n': 1}}

while True:
    m1, m2 = input().split()
    l1 = ord(m1[0]) - sub
    l2 = ord(m2[0]) - sub

    n1 = int(m1[1])
    n2 = int(m2[1])
    
    rep = True
    mov = 0
    while rep:
        mov += 1
        if(abs(l1-l2) <= abs(n1-n2)): pulos = [2, 1]   
        else: pulos = [1, 2]
        
        print(f'{chr(l1+sub)}{n1} {chr(l2+sub)}{n2}')
        print(abs(l1-l2), abs(n1-n2), pulos)
        
        #print(l1, n1, l2, n2)
        if(l1 <= l2 and n1 <= n2):
            l1 += pulos[0]
            n1 += pulos[1]
            print('c1')
        elif(l1 > l2 and n1 <= n2):
            l1 -= pulos[0]
            n1 += pulos[1]
            print('c2')
        elif(l1 < l2 and n1 >= n2):
            l1 += pulos[0]
            n1 += pulos[1]
            print('c3')
        else:
            l1 -= pulos[0]
            n1 -= pulos[1]
            print('c4')
        #print(l1, n1, l2, n2)
        '''
        if(l1 > l2): l1 -= pulos[p]['l']
        elif(abs(l1-l2) < (n1-n2)): l1 -= pulos[p]['l']
        else: l1 += pulos[p]['l']
        
        if(n1 > n2): n1 -= pulos[p]['n']
        elif(abs(n1-n2) < (n1-n2)): n1 -= pulos[p]['n']
        else: n1 += pulos[p]['n']
        '''
        #print(f'{l1}{n1} {l2}{n2}')
        
        if(l1 == l2 and n1 == n2): rep = False
        input()
        
    
    print(f"To get from {m1} to {m2} takes {mov} knight moves.") 
    

'''
if(m1 == m2):
    mov = 0
else: mov = 999999

print()
print(f"To get from {m1} to {m2} takes {mov} knight moves.")
'''
