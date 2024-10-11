line = input("строка: ")
e1 = ''
e2 = ''
maxColvo1 = 0
maxColvo2 = 0
for e in line:
    if line.count(e) > maxColvo1:
        maxColvo2 = maxColvo1
        e2 = e1
        maxColvo1 = line.count(e)
        e1 = e
    if line.count(e) > maxColvo2 and line.count(e) < maxColvo1:
        maxColvo2 = line.count(e)
        e2 = e
print(e1, e2)
