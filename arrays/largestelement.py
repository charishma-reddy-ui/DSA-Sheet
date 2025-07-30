arr = [3,4,8,2,1]
for i in range(0,len(arr)-1):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i+1] = arr[i+1],arr[i]
    
print(arr[len(arr) - 1])
print(arr)

