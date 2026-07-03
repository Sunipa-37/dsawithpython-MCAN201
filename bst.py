class node:
    def __init__(self,item):
        self.info=item
        self.left =None
        self.right=None
class binarystree:
    def __init__(self):
        self.root=None
    def insert(self,item):
        nd=node(item)
        if self.isempty():
            self.root=nd
            print(" e inserted")
            return
        temp=self.root
        while temp!=None:
            if item<temp.info:
                par=temp
                temp=temp.left
            else:
                par=temp
                temp=temp.right
        if item <par.info:
            par.left=nd
        else:
            par.right=nd
    def isempty(self):
        if self.root==None:
            return 1
        else:
            return 0
    def search(self,item):
        temp=self.root
        par=temp
        while temp!=None:
            if item==temp.info:
                print(item," found")
                return par,temp
            elif item<temp.info:
                par=temp
                temp=temp.left
            else:
                par=temp
                temp=temp.right
        if temp==None:
            print(item," not found")
            return par, temp
    def delete_node_with_zero_child(self,par,temp):
        if self.isempty() ==0:
            if temp.left is None and temp.right is None:
                if temp==self.root:
                    self.root=None
                    del temp
                    return
                if par.left==temp:
                    par.left=None
                else:
                    par.right==None
                del temp 
                return 


def in_order(nd):
    if nd!=None:
        in_order(nd.left)
        print(nd.info, end=" ")
        in_order(nd.right)
    
def pre_order(nd):
    if nd!=None:
        print(nd.info, end=" ")
        pre_order(nd.left)
        pre_order(nd.right)
def post_order(nd):
    if nd!=None:
        post_order(nd.left)
        post_order(nd.right)
        print(nd.info,end=" ")
b1=binarystree()
b1.insert("F")
b1.insert("D")
b1.insert("H")
b1.insert("B")
b1.insert("E")
b1.insert("G")
b1.insert("I")
in_order(b1.root)
print()
pre_order(b1.root)
print()
post_order(b1.root)
par,temp=b1.search("G")
b1.delete_node_with_zero_child(par,temp)
in_order(b1.root)
