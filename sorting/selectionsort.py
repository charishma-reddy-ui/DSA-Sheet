#selection Sort

arr = [13,46,24,52,20,9]
print(len(arr))
for i in range(0,len(arr)-1):
    min = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            arr[j],arr[min] = arr[min],arr[j]
print(arr)










