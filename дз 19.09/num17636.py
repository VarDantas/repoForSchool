f = open("17_17636.txt")
arr = [int(x) for x in f]
maxSum = -300001
count = 0
arrMax3 = [x for x in arr if ((abs(x)%10==3)and(len(str(abs(x))))==3)]
max3 = max(arrMax3)
for i in range(1, len(arr)-1):
    arr3 = [x for x in [arr[i-1], arr[i], arr[i+1]] if ((abs(x)%10==3)and(len(str(abs(x))))==3)]
    if (len(arr3) > 0) and (arr[i-1]+arr[i]+arr[i+1] < max3):
        count += 1
        maxSum = max(maxSum, arr[i]+arr[i-1]+arr[i+1])
print(count, maxSum)
