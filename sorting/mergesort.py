arr =[13,15,16,14,21]


def merge_sort(arr, low , high):
    temp_arr = []
    if low == high: 
        temp_arr.append(low)
        return
    
    mid = (low + high )//2
    # print("low",low)
    # print("high",high)
    # print("mid",mid)
        
    # temp_arr.append(arr[high])
    # print(temp_arr)

    
     
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    # merge(arr,low,mid, high)
    return temp_arr


print(merge_sort(arr, 0, len(arr) - 1))
    
