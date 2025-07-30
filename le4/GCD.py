n1 = int(input())
n2 = int(input())
for i in range(1,min(n1,n2)+1):
    if n1 % i == 0 and n2 % i == 0:
        x = i
        i = max(i,x)
print(x)

