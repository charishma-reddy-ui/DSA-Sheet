n = 164
rev = 0
while n>0:
    s = n%10
    n = n//10
    rev = (rev)+s**3
print(rev)
