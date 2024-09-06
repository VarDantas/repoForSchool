file = open("data.txt")
k = 0
for line in file:
    flag = 1
    arr = [int(x) for x in line.split(';')]
    for i in range(7):
        for j in range(7):
            if arr[i]==arr[j]:
                flag = 0
    if (flag == 0) and ((sum(arr)/7)%11==0):
        k+=1
print(k)
    
