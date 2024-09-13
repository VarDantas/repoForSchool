f = open("17_17680.txt")
arr = [int(x) for x in f]
maxSum = -200001
count = 0
arr41 = [x for x in arr if ((x > 0) and (x % 41 == 0))]
min41 = min(arr41)
for i in range(1, len(arr)):
    if (arr[i] != arr[i-1]) and (abs(arr[i] - arr[i-1]) % min41 == 0):
        count += 1
        maxSum = max(maxSum, arr[i]+arr[i-1])
print(count, maxSum)
