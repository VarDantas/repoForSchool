f = open("17_17873.txt")
arr = [int(x) for x in f]
maxSum = -200001
minNum = min(arr)
count = 0
for i in range(1, len(arr)):
    if (arr[i] % 16 == minNum) or (arr[i-1] % 16 == minNum):
        count += 1
        maxSum = max(maxSum, arr[i]+arr[i-1])
print(count, maxSum)