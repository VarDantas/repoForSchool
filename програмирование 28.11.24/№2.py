from itertools import *
k = 0
for x in product('0123456789ABCDE', repeat = 5):
    s = ''.join(x)
    if (s.count('8')==1) and (s[0] != '0') and ((s.count('A')+s.count('B')+s.count('C')+s.count('D')+s.count('E')) >= 2):
        k += 1
print(k)