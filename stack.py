class stack():
    def __init__(self):
        self.stk=[0]*8
        self.top=-1
        self.size=len(self.stk)
    def push(self,item):
        if self.top== self.size-1:
            print("overflow")
            return
        self.top=self.top+1
        self.stk[self.top]=item
        print(item,"pushed")
        return
    def pop(self):
        if self.top ==-1:
            print("underflow")
            return
        item= self.stk[self.top]
        self.top-=1
        print(item,"poped")
        return
    def display(self):
        for i in range(0,self.top+1):
            print(self.stk[i],end=' ')
a=stack()
while(1):
    p=int(input("press 1 for push 2 for pop and 3 for display the stack 4 to end "))
    if (p==1):
        b=int(input("enter item: "))
        a.push(b)
    elif(p==2):
        a.pop()
    elif(p==3):
        a.display()
    elif(p==4):
        break
    else:
        print("invalid input")


