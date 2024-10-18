f = open("24-s1.txt")
k = 0
for stroka in f:
    if stroka.count("K")>stroka.count("U"):
        k += 1
print(k)
