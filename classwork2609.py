#11.148
arr = [100, 0, 150, 80, 1 , 0, 100,70, 35, 100, 0 , 3, 40, 100, 0, 160, 120, 0, 0, 0, 110, 100, 90, 80, 20, 0 ,0, 0,20, 30]
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
        k = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = k
print(arr[len(arr)-1])

#11.29
arr = [100, 0, 150, 80, 1 , 0, 100,70, 35, 100, 0 , 3, 40, 100, 0, 160, 120, 0, 0, 0, 110, 100, 90, 80, 20, 0 ,0, 0,20, 30]
arrData = []
for i in range(0, len(arr)):
    if not(arr[i]):
        arrData.append(i+1)
print(arrData)

#11.30       
arr = [4, 5, 2, 10, 12, 5,6, 10, 17, 8, 9 ,12, 4, 5, 6, 3, 7, 0, 9, 2]
arrNum=[]
for i in range(0, len(arr)):
    if arr[i] < 3:
        arrNum.append(i+1)
print(arrNum)
