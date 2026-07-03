class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        nd = Node(item)
        if self.front is None:          # empty queue
            self.front = nd
            self.rear = nd
            nd.next = self.front        # point to itself (circular!)
        else:
            nd.next = self.front        # new node → front
            self.rear.next = nd         # old rear → new node
            self.rear = nd              # advance rear
        print(self.rear.item, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Underflow")
            return
        if self.front == self.rear:     # single element
            print(self.front.item, "deleted")
            self.front = None
            self.rear = None
            return
        item = self.front.item
        self.front = self.front.next    # move front forward
        self.rear.next = self.front     # keep circular link intact ✅
        print(item, "deleted")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while True:
            print(temp.item, end=" -> ")
            temp = temp.next
            if temp == self.front:      # stop when we loop back
                break
        print("(back to front)")


a = CircularQueue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.display()
a.dequeue()
a.display()