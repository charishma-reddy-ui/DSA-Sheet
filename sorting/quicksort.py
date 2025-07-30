arr = [6,3,9,4,7,1,8,5,2]


def swap(i,j):
    arr[i],arr[j] = arr[j],arr[i]

def pivot(getArr, low , high):
    
    i = low
    j = high
    pivotVal = low
 #first while loop
    while (i < j):
        
    #two while loops
    
    # ?for the high value
        while( getArr[pivotVal] >= arr[i] and i <= high-1):
            i += 1
        # check the value is low
        while(getArr[pivotVal] < arr[j] and j > low):
            j -= 1
        if i < j: 
            swap(i,j)  

    swap(j,pivotVal)
    return j


def quick(arr,low,high):
    if low >= high:
        return
    #calling pivot function
    val =  pivot(arr,low,high)
    
   #calling recursively 
    quick(arr, low, val - 1)
    quick(arr, val+1, high)


# print(arr[7:len(arr)])
quick(arr,0,len(arr)-1)
# print(pivot(arr, 0, len(arr) - 1))
print(arr)
#function




