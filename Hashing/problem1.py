# 🔸 Problem 1:
# Insert the numbers: [20, 15, 25, 30, 35] into a hash table of size 5.
# Then search for 25 and 40.

# 🔸 Problem 2:
# Make a function that tells how many keys are at each index (i.e., length of the list at each index).

# 🔸 Problem 3:
# Modify the insert() function to not insert duplicate values.
import random
hasharray = [None]*10
def hashfunction(val):
    return val%10
def insertion(val):
    index = hashfunction(val)
    while hasharray[index] is not None:
        if index == len(hasharray)-1:
            index = 0
        index = index+1
    hasharray[index] = val
    return hasharray
def search(val):
    index = hashfunction(val)
    for i in range(0,len(hasharray)-1):
        if hasharray[i] == val:
            return i
        

insertion(20)
insertion(15)
insertion(25)
insertion(30)
insertion(35)
print(search(25))
print(hasharray)





