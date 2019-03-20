class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def __add__(self, item):
        temp = Node (item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count=0
        while current!= None:
            count = count+1

            current=current.getNext()
        return count
    def display(self):
         current=self.head
        while current !=None:
            print(current.getData())
            current=current.getData()
    mylist.display()
    def remove (self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData()==item:
                found = True
            else :
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:




mylist=LinkedList()

mylist.add(45)
print(mylist.head)
print(mylist.head.data)

mylist.add(21)

