# Given an array of N integers, left rotate the array by one place.

# Examples

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 2,3,4,5,1
# Explanation: 
# Since all the elements in array will be shifted 
# toward left by one so ‘2’ will now become the 
# first index and and ‘1’ which was present at 
# first index will be shifted at last.


# Example 2:
# Input: N = 1, array[] = {3}
# Output: 3
# Explanation: Here only element is present and so 
# the element at first index will be shifted to 
# last index which is also by the way the first index.

# left rotate
arr = [1,2,3,4,5,6,7]

for i in range(0, len(arr)-1):
    if i == len(arr)-1:
        break
    else:
        arr[i], arr[i-1] = arr[i-1], arr[i]
print(arr)



# RIGHT ROTATE


arr = [1,2,3,4,5,6,7]


#loop form the last

for i in range(len(arr)-1, -1, -1):
    if i == 0:
        break
    # print(arr[i])
    arr[i],arr[i-1] = arr[i-1],arr[i]
     
print(arr)








