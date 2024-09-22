f = open('17_9704.txt')
minEl = 100001
count = 0
arr = [int(x) for x in f]
arrSum2 = []
for i in range(1, len(arr)):
    if (len(str(arr[i])) == 2 and len(str(arr[i-1])) != 2) or (len(str(arr[i-1])) == 2 and len(str(arr[i])) != 2):
        arrSum2.append(arr[i]+arr[i-1])
for i in arr:
    if i > max(arrSum2):
        count += 1
        minEl = min(minEl, i)
print(count, minEl)
