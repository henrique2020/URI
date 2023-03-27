for _ in range(int(input())):
    fat = input();
    exc = fat.count('!')
    
    fat = int(fat.replace('!', ''))
    num = fat - exc
    
    calc_fat = fat
    while num > 1:
        calc_fat *= num
        num -= exc
        
    print(calc_fat)