# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

# Examples

# Example 1:
# Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
# Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

# Example 2:
# Input: 1,2,0,1,0,4,0
# Output: 1,2,1,4,0,0,0
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

arr = [0,1,0,3,12]
#i was trying to swap the zeroes
j = 0
def MoveallZeros(arr,j):
    if j == 0:
        return

    for i in range(0,len(arr)-1): 
        if arr[i] == 0:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    j = j-1
    
    MoveallZeros(arr,j)

MoveallZeros(arr,len(arr)-1)  
print(arr)





#the two pointer approach

j = -1


for i in range(0,len(arr)-1):
    if arr[i] == 0:
        j = i
        print(arr[j])
        break

    if j == -1:
        break


for i in range(j+1,len(arr)):
    if arr[i] != 0:
        arr[i] ,arr[j] = arr[j],arr[i]
        j = j+1






print(arr)


