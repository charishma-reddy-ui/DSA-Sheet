# ✏️ Question (Easy Level):

# You have a hash table with m = 5 slots.
# Insert the following keys using chaining (linked lists at each slot):

# Keys: 12, 15, 7, 22, 5, 32

# Hash function: h(k) = k mod m
# 🚀 What to do:

# ✅ Show the final hash table after inserting all keys.
# ✅ For each slot, show the linked list (order of insertion).
# 💡 Expected Steps:

#     Compute index: 12 mod 5 = 2 → slot 2

#     15 mod 5 = 0 → slot 0

#     7 mod 5 = 2 → slot 2 → chain

#     22 mod 5 = 2 → slot 2 → chain

#     5 mod 5 = 0 → slot 0 → chain

#     32 mod 5 = 2 → slot 2 → chain

class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        self.length = 0
        
    def insertion(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.next = None
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        
    def traverse(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
                print("Value find")
                return
            
            current = current.next
        print("Value not here ")
        return
    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.val)
            if temp.next is not None:
                res += "=>"
            temp = temp.next
        return res     
    
hashArr = [None]*10

def hashFun(val):
    return val % 10

def insertion(val):
    
    index = hashFun(val)
    print("Index", index)

    if hashArr[index] is None :
        Linked = Link()
   
        Linked.insertion(val)
        hashArr[index] = Linked
    else:
        hashArr[index].insertion(val)

        
def findVal(val):
    index = hashFun(val)
    print("Index",index)
    link = hashArr[index]
    link.traverse(val)
    # while link != None:
    #     if link.val == val: 
    #         print("Value is present")
    #     link = link.next
    # print("Value is not present")
# def 
    
insertion(10)
insertion(20)
insertion(30) 
insertion(40) 
insertion(44) 
insertion(45) 

findVal(50)
print(hashArr)     
    




    
   


