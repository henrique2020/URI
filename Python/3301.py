h, z, l = map(int, input().split())
if ((z < h < l) or (z > h > l)): print('huguinho')
elif ((h < z < l) or (h > z > l)): print('zezinho')
else: print('luisinho')
