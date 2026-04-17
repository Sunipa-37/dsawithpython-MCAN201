class queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.que=[0]*4
        self.size=len(self.que)
    def insert(self,item):
        if self.front==self.size-1:
            print("overflow")
            return
        self.front+=1
        self.que[self.front]=item
        if self.rear==-1:
            self.rear=0
        print(item,"pushed")
    def delete(self):
        if self.rear==-1 and self.front==-1:
            print("underflow")
            return
        item=self.que[self.rear]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.rear+=1
        print(item,"poped")
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements: ")
            for i in range(self.rear, self.front + 1):  # rear se front tak
                print(self.que[i])


a=queue()
while(1):
    p=int(input("press 1 for push 2 for pop and 3 for display the stack 4 to end "))
    if (p==1):
        b=int(input("enter item: "))
        a.insert(b)
    elif(p==2):
        a.delete()
    elif(p==3):
        a.display()
    elif(p==4):
        break
    else:
        print("invalid input")