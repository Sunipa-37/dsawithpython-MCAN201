class node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.start=None
    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            print(f"{item} inserted last")
            return
        temp=self.start
        while(temp.next!=None):
            temp=temp.next
        temp.next=nd
        nd.prev=temp
        print(f"{item} inserted at last")
    def insert_at_beg(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            print(f"{item} inserted at first")
            return
        self.start.prev=nd
        nd.next=self.start
        self.start=nd
        print(f"{item} inserted at first")
    def insert_after_spec_pos(self,item,pos):
        nd=node(item)
        if self.start==None:
            self.insert_at_beg(item)
        temp=self.start
        i=1
        while(temp.next!=None)and(i<pos):
            temp=temp.next
            i+=1
        nd.next=temp.next
        nd.prev=temp
        if temp.next is not None:
            temp.next.prev=nd
            temp.next=nd
    def insert_after_spec_item(self,item,sitem):
        nd=node(item)
        if self.start==None:
            self.insert_at_beg(item)
            return
        temp=self.start
        while(temp.next!=None)and(temp.item!=sitem):
            temp=temp.next
        if(temp.item!=sitem):
            print("item not found")
            return
        nd.next=temp.next
        nd.prev=temp
        if temp.next is not None:
            temp.next.prev=nd
        temp.next=nd
        print(f"{item} inserted after {sitem}")
    def delete_from_beg(self):
        temp=self.start
        temp.next.prev=None
        self.start=temp.next
        if self.start is not None:
            self.start.prev=None
        del temp
        print("deleted begging item")
    def delete_at_last(self):
        if self.start is None:
            print("list is empty")
            return
        if self.start.next is None:
            del self.start
            self.start =None
            print("deleted last item")
            return
        temp=self.start
        while(temp.next!=None):
            prev=temp
            temp=temp.next
        prev.next=None
        del temp
        print("deleted last item")
    def delete_spec_pos(self,pos):
        if(pos ==1):
            self.delete_from_beg()
            return
        temp=self.start
        i=1
        while(temp.next!=None)and(i<pos):
            prev=temp
            temp=temp.next
            i+=1
        if(i<pos):
            print("position doesnot exsist")
            return
        prev.next=temp.next
        if temp.next is not None:
            temp.next.prev=temp.prev
        del temp
        print(f"{pos} item deleted")
    def delete_spec_item(self,item):
        if self.start is None:
            print("list is empty")
            return
        
        if self.start.item==item:
            self.delete_from_beg()
            return
        temp=self.start
        while(temp.next!=None)and(temp.item!=item):
            # prev=temp
            temp=temp.next
        if(temp.item!=item):
            print("item does not exsist")
            return
        if temp.prev is not None:
            temp.prev.next=temp.next
        if temp.next is not None:
            temp.next.prev=temp.prev
        del temp
        print(item,"deleted")
    
    def display(self):
        temp=self.start
        while(temp.next!=None):
            print(temp.item,end="-> ")
            temp=temp.next
        print(temp.item)
d1=doublelinkedlist()
d1.insert_at_last("b")
d1.insert_at_last("d")
d1.insert_at_beg("a")
d1.insert_after_spec_pos("c",2)
d1.insert_after_spec_item("e","d")
d1.display()
d1.delete_from_beg()
d1.display()
d1.delete_at_last()
d1.display()
d1.delete_spec_pos(2)
d1.display()
d1.delete_spec_item("2")
d1.display()
d1.delete_spec_item("d")
d1.display()