class node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None

class circulardoublelinkedlist:
    def __init__(self):
        self.start=None

    def insert_at_last(self,item):
        nd=node(item)

        if self.start==None:
            self.start=nd
            nd.next=nd
            nd.prev=nd
            print(f"{item} inserted at last")
            return

        last=self.start.prev

        last.next=nd
        nd.prev=last

        nd.next=self.start
        self.start.prev=nd

        print(f"{item} inserted at last")

    def insert_at_beg(self,item):
        nd=node(item)

        if self.start==None:
            self.start=nd
            nd.next=nd
            nd.prev=nd
            print(f"{item} inserted at first")
            return

        last=self.start.prev

        nd.next=self.start
        nd.prev=last

        last.next=nd
        self.start.prev=nd

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
        nd.prev=temp

        temp.next.prev=nd
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

        last=self.start.prev

        temp=self.start

        self.start=self.start.next

        self.start.prev=last
        last.next=self.start

        del temp

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

        last=self.start.prev
        newlast=last.prev

        newlast.next=self.start
        self.start.prev=newlast

        del last

        print("deleted last item")

    def delete_spec_item(self,item):
        if self.start==None:
            print("list is empty")
            return

        if self.start.item==item:
            self.delete_from_beg()
            return

        temp=self.start.next

        while(temp!=self.start and temp.item!=item):
            temp=temp.next

        if temp==self.start:
            print("item does not exist")
            return

        temp.prev.next=temp.next
        temp.next.prev=temp.prev

        del temp

        print(item,"deleted")

    def display(self):
        if self.start==None:
            print("list is empty")
            return

        temp=self.start

        while(temp.next!=self.start):
            print(temp.item,end=" <-> ")
            temp=temp.next

        print(temp.item)
d1=circulardoublelinkedlist()

d1.insert_at_last("b")
d1.insert_at_last("d")
d1.insert_at_beg("a")
d1.insert_after_spec_item("c","b")
d1.insert_after_spec_item("e","d")

d1.display()

d1.delete_from_beg()
d1.display()

d1.delete_at_last()
d1.display()

d1.delete_spec_item("c")
d1.display()

d1.delete_spec_item("d")
d1.display()