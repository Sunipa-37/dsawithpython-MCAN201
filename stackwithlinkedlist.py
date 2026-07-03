class node:
    def __init__(self,item):
        self.item=item
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def push(self,item):
        nd=node(item)
        nd.next=self.top
        self.top=nd
        print(nd.item, "inserted")
    def pop(self):
        if self.top==None:
            print("underflow")
            return
        item=self.top.item
        self.top=self.top.next
        print(item," deleted")
    def display(self):
        if self.top==None:
            print("]")
            return
        temp=self.top
        while(temp!=None):
            print(temp.item, end =" ")
            temp=temp.next
        print("]")
        
a=stack()
a.push(8)
a.display()
a.push(9)
a.display()
a.push(12) 
a.display()
a.pop()
a.display()
a.pop()
a.display()
a.pop()
a.display()
a.pop()
a.display()