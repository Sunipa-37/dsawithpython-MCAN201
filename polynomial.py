class node:
    def __init__(self,co,expo):
        self.co=co
        self.expo=expo
        self.next=None
class polynomial:
    def __init__(self):
        self.start=None
    def insert(self,co,expo):
        nd=node(co,expo)
        if self.start==None:
            self.start=nd
            print("first done")
            return
        if expo>self.start.expo:
            nd.next=self.start
            self.start=nd
            return
        temp=self.start
        while (temp.next!=None) and (temp.next.expo>nd.expo):
            temp=temp.next
        nd.next=temp.next
        temp.next=nd
        print("item inserted")
    def display(self):
        temp=self.start
        while(temp!=None):
            print(f"{temp.co}x^{temp.expo}",end=" ")
            if temp.next!=None:
                print("+",end="")
            temp=temp.next
        print()
p=polynomial()
p.insert(34,6)
p.insert(456,2)
p.display()