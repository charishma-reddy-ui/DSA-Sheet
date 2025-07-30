class Node:
    def __init__(self,value):
        self.next = None
        self.val = value
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,val):
        n = Node(val)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
            
        self.length +=1
    def __str__(self):
        # in this method it will only concatinate the strings so need to convert the value into temp
        temp = self.head
        result = ""
        while temp is not None:
            result +=str(temp.val)
            if temp.next is not None:
                result += "=>" 
            temp = temp.next     
        return result
    
linkedList1 = linkedlist()
linkedList1.append(3)
linkedList1.append(2)
linkedList1.append(1)
print(linkedList1)
            

        