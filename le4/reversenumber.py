rev = 0
n = int(input())
x = abs(n)
while x>0:
    s = x%10
    x = x//10
    rev = (rev *10)+s
if n < 2147483647:
    print(-rev)
else:
    print(rev)
 
