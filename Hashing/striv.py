arr = [10,5,3,4,3,5,6]
obj = {}#precomputation
for i in arr:
    if i not in obj:
        obj[i] = 1
    else:
        obj[i] = obj[i]+1
for keys,values in obj.items():
    if values == 2:
        print(keys)#obj.keys(),obj.values()
        break
print(obj)

# max = 0
# min = 0
# for k,v in items():
# A = [10,5,3,4,3,5,6]
# obj = {}=>10,5,3,4
# for i in A:
#     if i in obj:
#         print(i)
#         break
#     else:
#         obj[i] = i
        
    
    



        




    