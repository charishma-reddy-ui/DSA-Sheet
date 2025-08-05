# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Examples:

# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.
 
# left rotate
arr = [1,2,3,4,5,6,7]
j = 0
def Ktimes(j,k,arr):

    #base condition
    if j >= k:
        return
    
    #for looping
    for i in range(0, len(arr)-1):
        if i == len(arr)-1:
            break
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]

    #for increasing the counter      
    j = j+1
    
    Ktimes(j,k,arr)
        
        
Ktimes(j,3,arr)
print(arr)


     

     




