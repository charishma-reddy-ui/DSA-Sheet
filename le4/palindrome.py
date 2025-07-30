n = int(input("Enter a number: "))
x = n
rev = 0
while n>0:
    s= n%10
    n = n//10
    rev = (rev*10)+s
print(rev)
if rev != x:
    print("false")
else:
    print("true")
