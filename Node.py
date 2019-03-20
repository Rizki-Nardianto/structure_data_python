class Node:
    def __init__(self, init_data):
        self.data= init_data
        self.next= None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data= newdata
    def setNext(self, new_next):
        self.next=new_next

a= Node(93)
b= Node(20)
c= Node(45)
print(a.getNext())
print(b.getNext())
#
print(b.getNext())
a.setNext(b)
print(a.getNext())
print(b.getData())
print(b.setNext(c))


