from fnmatch import *
for i in range(0, 10**12, 98591):
    s = str(i)
    if fnmatch(s, '12?3*456??9'):
        print(i, i //98591)
