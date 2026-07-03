class node:
    def __init__(Self,item):
        Self.info=item
        Self.next=None
class clinkedlist:
    def __init__(self):
        self.start=None
    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            nd.next=self.start
            print("item insertion successful")
            return
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        temp.next=nd
        nd.next=self.start
        print("item insertion successful")
    def insert_at_beg(self,item):
        nd=node(item)
        if self.start== None:
            self.start=nd
            nd.next=nd
        temp=self.start
        while(temp.next!= self.start):
            temp=temp.next
        nd.next=self.start
        temp.next=nd
        self.start=nd
    def display(self):
        if self.start is None:
            print("empty")
            return
        
        temp=self.start
        while True:
            print(temp.info,end="->")
            temp=temp.next
            if temp== self.start:
                break
    def insert_at_position(self,item,pos):
            nd=node(item)
            if self.start ==None:
                self.start=nd
                nd.next=nd
                print("item insertion succesfull")
                return
            if pos==1:
                self.insert_at_beg(item)
                return
            temp=self.start
            i=1
            while temp==self.start or i<pos:
                temp=temp.next
                i+=1
            nd.next=temp.next
            temp.next=nd
    

sl=clinkedlist()
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