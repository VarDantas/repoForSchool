for N in range(1,1000):
    n=N
    r = ''
    while n > 0:
        r = str(n%3) + r
        n //= 3
    if N % 2 == 0:
        r  = '2' + r + r[len(r)-1]*2
    else:
        r = r[0]*2 + r + '2'
    if int(r, 3) > 100:
        print(int(r,3))
        break
    