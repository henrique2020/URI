while True:
    try: n = int(input())
    except: break
	
    for i in range(1, n+1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
	
    print(" " * ((n - 1) // 2) + "*")
    print(" " * ((n - 2) // 2) + "***")
    print("")
