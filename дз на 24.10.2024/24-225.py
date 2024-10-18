import fnmatch
maxel = -100000000000
f = open("24-225.txt")
for stroka in f:
    p = stroka.split("CC")
    for part in p:
        if part.isdigit():
            if fnmatch.fnmatch(part, "234???57???8"):
                maxel = max(int(part), maxel)

proiz = 1
for i in str(maxel):
    if int(i)%2!=0:
        proiz *= int(i)
print(maxel, proiz)
