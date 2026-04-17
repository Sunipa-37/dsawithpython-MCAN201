class cir_que:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.que=[0]*5
        self.size=len(self.que)
    def insert(self,item):
        if self.front==(self.rear+1)%self.size:
            print("overflow")
            return
        self.rear=(self.rear+1)%self.size
        self.que[self.rear]=item
        if self.front==-1:
            self.front=0
        print(item,"inserted")
    def delete(self):
        if self.front== -1 and self.rear ==-1:
            print("underflow")
            return
        item=self.que[self.front]
        if self.front== self.rear:
            self.front =-1
            self.rear =-1
        else:
            self.front=(self.front+1)%self.size
        print(item,"deleted")
    def display(self):
        i = self.front
        while (True):
            print(self.que[i])
            if (i == self.rear):
                break
            i = (i + 1) %self.size
a=cir_que()
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