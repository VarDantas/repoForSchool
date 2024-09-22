f = open('17_11481.txt')
count = 0
minSum = 300001
arr = [ int(x) for x in f]
arr8 = [ x for x in arr if str(x)[0] == '8']
max8 = max(arr8)
for i in range(1, len(arr)-1):
    arr6 = [x for x in [arr[i], arr[i-1], arr[i+1]] if str(x)[0] == '6']
    if (len(arr6) <= 1) and (arr[i] + arr[i-1] + arr[i+1] >= max8):
        count += 1
        minSum = min(minSum, arr[i] + arr[i-1] + arr[i+1])
print(count, minSum)
