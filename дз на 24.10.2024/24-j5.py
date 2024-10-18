f = open("24-j5.txt")
k = 0
for stroka in f:
    k += stroka.count("KOT")
print(k)
