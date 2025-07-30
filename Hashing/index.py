# fruits = ["Apple", "Banana", "Cherry", "Grapes", "Orange"]
def hashfunction(val):
    return ord(val[0]) % 10

hasharray = [None]*10

def insertion(key,value):
    index = hashfunction(value)

    while hasharray[index] is not None:
        if index == len(hasharray): 
            index = 0
        index = index + 1
        
    
    hasharray[index] = value
    return hasharray

def retrieve(val):
    index = hashfunction(val)
    return hasharray[index]


def deletekey(key):
    while hasharray[key] is not None:
        hasharray.remove(key)


print(insertion(3,"value"))
print("Hash Array", hasharray)
insertion(3,"Apple")
print(retrieve("Apple"))


    


        
