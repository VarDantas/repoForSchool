def f(s,c,n):
    if s+c >= 65 or n > 4:
        return n == 2 or n == 4
    if n % 2 == 0:
        return f(s+1,c,n+1) and f(s,c+1,n+1) and f(s*3,c,n+1) and f(s,c*3,n+1)
    return f(s+1,c,n+1) or f(s,c+1,n+1) or f(s*3,c,n+1) or f(s,c*3,n+1)

for s in range(2, 58):
    if f(s,6,0):
        print(s)
    