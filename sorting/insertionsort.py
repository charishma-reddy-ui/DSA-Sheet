

arr = [13,46,24,52,20,9]
# for insertion sort
print("Length", len(arr))

for i in range(0,len(arr)):
    j = i

    # print("IIII",i)
    #second loop will do the real swap thing
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j = j-1
print(arr)
    

    # j = i + 1
    # if j == len(arr):
    #     break
    # if j == len(arr): j = len(arr) - 1 
    # for x in range(j,-1):
    #     # print("JJJ",arr[j])
    #     if arr[x] < arr[x+1]:
    #         arr[x] ,arr[x+1] = arr[x+1],arr[x]



# print(arr)
