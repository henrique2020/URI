l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

compativel = True
for p in range(5):
    if (l1[p] + l2[p]) != 1:
        compativel = False
        break
    
if compativel: print("Y")
else: print("N")
