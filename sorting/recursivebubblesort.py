arr = [13,46,24,52,20,9]
def func(i,j):
    if i >= len(arr)-1:
        return
    if j >= len(arr):
        func(i+1,i+2) 
        return
    if (arr[i] > arr[j]):
        arr[i],arr[j] = arr[j],arr[i]
    func(i,j+1)
func(0,1) 
print(arr)