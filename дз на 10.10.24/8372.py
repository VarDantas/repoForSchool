def F(n):
    if n < 2:
        return n
    if n >= 2:
        return F(n//2)*10+n%2
for n in range(1500000):
    if F(n) == 100000100001000100101:
        print(n)
