class node:
    def __init__(self,item):
        self.info=item
        self.next=None
class slinkedlist:
    def __init__(self):
        self.start=None

    def insert_at_beg(self,item):
        nd=node(item)
        nd.next=self.start
        self.start=nd
        print("successfully inserted in begining")
    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            print("linked it was empty item inserted")
            return
        temp=self.start
        while(temp.next!=None):
            temp=temp.next
        temp.next=nd
        print("successfully inserted at last ")
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end=" ")
            temp=temp.next
    def insert_at_position(self,item,pos):
        if pos==1:
            self.insert_at_beg(item)
        else:
            nd =node(item)
            i=1
            temp=self.start
            while (temp.next!=None) and (i <pos-1):
                temp=temp.next
                i+=1
            if temp.next == None:
                temp.next =nd
                return
            nd.next=temp.next
            temp.next=nd
    def insert_after_specific_item(self,item,sitem):
        nd=node(item)
        temp=self.start
        while temp.info!=sitem and temp.next!=None:
            temp=temp.next
        nd.next=temp.next
        temp.next=nd
    def delete_start(self):
        temp=self.start
        self.start=temp.next
        del temp
    def delete_last_node(self):
        if self.start.next is None:
            self.start=None
            return
        temp=self.start
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        del temp
    def delete_spec_pos(self, pos):
        if pos == 1:
            self.delete_start()
            return
        temp = self.start
        i = 1
        while temp.next is not None and i < pos:
            prev = temp
            temp = temp.next
            i += 1
        if i < pos:
            print("Position does not exist")
            return
        prev.next = temp.next
        del temp
    def delete_spec_item(self,item):
        if self.start.info==item:
            self.start=self.start.next
            return
        temp=self.start
        while(temp.next!=None)and(temp.info!=item):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp
sl=slinkedlist()
print(" ")
while(1):

    p=int(input("press 1 for insert at beg \n 2 for insert at the end\n 3 for insert at a position\n 4 for insert after a specific item \n 5 for delete at begging \n 6 for delete from last \n 7 for delete specific position \n 8 for delete specific item \n 9 for display "))
    if (p==1):
        b=int(input("enter item: "))
        sl.insert_at_beg(b)
    elif(p==2):
        b=int(input("enter item: "))
        sl.insert_at_last(b)
    elif(p==3):
        b=int(input("enter the item:"))
        c=int(input("enter position"))
        sl.insert_at_position(b,c)
    elif(p==4):
        b=int(input("enter the item:"))
        c=int(input("enter after which item u want to insert: "))
        sl.insert_after_specific_item(b,c)
    elif(p==5):
        sl.delete_start()
    elif(p==6):
        sl.delete_last_node()
    elif(p==7):
        b=int(input("enter the position :"))
        sl.delete_spec_pos(b)
    elif(p==8):
        b=int(input("enter the item: "))
        sl.delete_spec_item(b)
    elif(p==9):
        sl.display()
    else:
        print("invalid input")
    print("")