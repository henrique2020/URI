t = input()
if t.count('X') != 2: print('?')
elif(t[0] == t[1] or t[1] == t[2]): print('Alice')
else: print('*')
