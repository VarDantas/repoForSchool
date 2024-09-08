file = open("data.txt")
k = 0
for line in file:
    arr = [int(x) for x in line.split(';')]
    s = set(arr)
    if (len(s) == 7) and ((sum(arr)/7)%11==0):
        k+=1
print(k)
