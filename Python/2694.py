rep = int(input())
while(rep):
    error = input()
    num1 = int(error[2:4])
    num2 = int(error[5:8])
    num3 = int(error[11:13])
    print(num1+num2+num3)
    rep-=1
