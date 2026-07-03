# class stack():
#     def __init__(self,size):
#         self.stk=[0]*size
#         self.top=-1
#         self.size=len(self.stk)
#     def push(self,item):
#         if self.top== self.size-1:
#             print("overflow")
#             return
#         self.top=self.top+1
#         self.stk[self.top]=item
#         print(item,"pushed")
#         return
#     def pop(self):
#         if self.top ==-1:
#             print("underflow")
#             return
#         item= self.stk[self.top]
#         self.top-=1
#         print(item,"poped")
#         return
#     def display(self):
#         for i in range(self.top+1):
#             print(self.stk[i],end=' ')
# a=stack()
# while(1):
#     p=int(input("press 1 for push 2 for pop and 3 for display the stack 4 to end "))
#     if (p==1):
#         b=int(input("enter item: "))
#         a.push(b)
#     elif(p==2):
#         a.pop()
#     elif(p==3):
#         a.display()
#     elif(p==4):
#         break
#     else:
#         print("invalid input")

class stack:
    def __init__(self,size):
        self.top=-1
        self.stk=[None]*size
        self.size=size
    def push(self,item):
        if self.top==self.size-1:
            print("overflow")
            return  
        self.top+=1
        self.stk[self.top]=item
        print(f"{item} inserted")
    def pop(self):
        if self.top==-1:
            print("underflow")
            return
        item=self.stk[self.top]
        self.top-=1
        print(f"\n{item } deleted ")
    def display(self):
        print("[",end=" ")
        for i in range(self.top+1):
            print(self.stk[i], end=" ")
    def top(self):
        print(self.stk[self.top])
        return 
    def isEmpty(self):
        if self.top ==-1:
            return True
    def isFull(self):
        if self.top==self.size-1:
            return True
a=stack(3)
a.push(8)
a.push(7)
a.push(7)
a.push(7)
a.display()
a.pop()
a.display()