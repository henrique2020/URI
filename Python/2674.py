def primo(n):
    if (n%2 == 0 and n>2) or n<2:
        return False
    return all(n%i for i in range(3,int((n**0.5)+1), 2))
while True:
    try:
        num = input()
        if primo(int(num)):
            superP = True
            for e in num:
                if primo(int(e)):
                    pass
                else:
                    superP = False
                    break
                
            if superP: 
                print("Super")
            else: 
                print("Primo")
        else: 
            print("Nada")
    except:
        break
