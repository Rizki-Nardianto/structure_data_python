def createQueue():
    q=[]
    return (q)
def enqueue (q, data):
    q.insert(0,data)
    return (q)
def dequeue(q):
    data=q.top()
    return(data)
def isEmpty(q):
    return (q==[])
def size(q):
    return(len(q))
#contoh     1
q=createQueue()
enqueue(q, 'matk')
enqueue(q, 'strukdat')
enqueue(q, 'bahasa inggris')
enqueue(q, "pemrograman web")
print(q)

#contoh 2
temp=dequeue(q)
print(q)
print(temp)

#program 4
p=['pemrograman web','bahsa inggris','struktur data']
enqueue(p, dequeue(p))
print(q)

