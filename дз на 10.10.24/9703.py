k = 0
def F(n):
    if n < 2:
        return n
    if n >= 2:
        return F(n//2)+F(n%2)
for n in range(2**30):
    if F(n) == 27:
        k += 1
print(k)
