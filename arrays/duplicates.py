# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place 
# such that each unique element appears only once. The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, then the first k elements of the array should hold the
#  final result. It does not matter what you leave beyond the first k elements.
# arr = [1,2,4,7,7,5,5,6,6,6,7,8,9]
# newArr = []
# arr = obj.cop


# # print(obj[4])
# # obj = {}*None

# l = len(arr) -1
# for i in arr:
#     if i in obj:
#         obj[i] = obj[i] + 1
#     else:
#         obj[i] = 1      


# for key in obj.keys():
#     newArr.append(key)
# for key,values in obj.items():
#     if values >= 2:
#         arr.remove(key) 
        
# print(obj)
# print(arr)

arr = [1,1,1,2,2,2,3,3,4,4,5,5,5,5]
arr2 = []

for i in range(0, len(arr)-1):
    if arr[i] in arr2:
        continue
    else: 
        arr2.append(arr[i])

print(arr2)




    



