class node:
    def __init__(self,item):
        self.item=item
        self.next=None

class circularlinkedlist:
    def __init__(self):
        self.start=None

    def insert_at_last(self,item):
        nd=node(item)

        if self.start==None:
            self.start=nd
            nd.next=self.start
            print(f"{item} inserted at last")
            return

        temp=self.start
        while(temp.next!=self.start):
            temp=temp.next

        temp.next=nd
        nd.next=self.start
        print(f"{item} inserted at last")

    def insert_at_beg(self,item):
        nd=node(item)

        if self.start==None:
            self.start=nd
            nd.next=self.start
            print(f"{item} inserted at first")
            return

        temp=self.start
        while(temp.next!=self.start):
            temp=temp.next

        nd.next=self.start
        temp.next=nd
        self.start=nd

        print(f"{item} inserted at first")

    def insert_after_spec_item(self,item,sitem):
        nd=node(item)

        if self.start==None:
            self.insert_at_beg(item)
            return

        temp=self.start

        while(True):
            if temp.item==sitem:
                break
            temp=temp.next
            if temp==self.start:
                print("item not found")
                return

        nd.next=temp.next
        temp.next=nd

        print(f"{item} inserted after {sitem}")

    def delete_from_beg(self):
        if self.start==None:
            print("list is empty")
            return

        if self.start.next==self.start:
            del self.start
            self.start=None
            print("deleted beginning item")
            return

        temp=self.start

        while(temp.next!=self.start):
            temp=temp.next

        temp.next=self.start.next

        t=self.start
        self.start=self.start.next

        del t

        print("deleted beginning item")

    def delete_at_last(self):
        if self.start==None:
            print("list is empty")
            return

        if self.start.next==self.start:
            del self.start
            self.start=None
            print("deleted last item")
            return

        temp=self.start

        while(temp.next!=self.start):
            prev=temp
            temp=temp.next

        prev.next=self.start

        del temp

        print("deleted last item")

    def delete_spec_item(self,item):
        if self.start==None:
            print("list is empty")
            return

        if self.start.item==item:
            self.delete_from_beg()
            return

        prev=self.start
        temp=self.start.next

        while(temp!=self.start and temp.item!=item):
            prev=temp
            temp=temp.next

        if temp==self.start:
            print("item does not exist")
            return

        prev.next=temp.next

        del temp

        print(item,"deleted")

    def display(self):
        if self.start==None:
            print("list is empty")
            return

        temp=self.start

        while(temp.next!=self.start):
            print(temp.item,end=" -> ")
            temp=temp.next

        print(temp.item)


c1=circularlinkedlist()

c1.insert_at_last("b")
c1.insert_at_last("c")
c1.insert_at_beg("a")
c1.insert_after_spec_item("d","c")

c1.display()

c1.delete_from_beg()
c1.display()

c1.delete_at_last()
c1.display()

c1.delete_spec_item("b")
c1.display()