from datetime import date
year = 2016
natal = date(year, 12, 25)

while True:
    try: month, day = map(int, input().split())
    except: break

    dif = natal - date(year, month, day)
    dif = dif.days
    if(dif < 0): print("Ja passou!")
    elif(dif == 0): print("E natal!")
    elif(dif == 1): print("E vespera de natal!")
    else: print("Faltam {} dias para o natal!".format(dif))
