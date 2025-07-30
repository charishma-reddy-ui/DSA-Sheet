def rev(arr,s,e):
    if s>=e:
        return e
    arr[s],arr[e] = arr[e],arr[s]
    rev(arr,s+1,e-1)
    return arr
    
    
arr = [1,2,3]
print(rev(arr,0,len(arr)-1))


##palindrome.py
def pal(arr,s,e):
    if s>=e:
        return True
    if arr[s]!=arr[e]:
        return False
    return pal(arr,s+1,e-1)
arr = "mom"
print(pal(arr,0,len(arr)-1))
##fibanocci
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    print(fib(n-1)+fib(n-2))
n = 5
fib(n)
    

