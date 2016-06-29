def rprint(n):
    if n == 0:
        print('')
    else:
        try:
            print(m - n + 2)
            rprint(n-1)
        except:
            global m
            m = n - 1
            print(m - n + 2)
            rprint(n-1)

rprint(100)