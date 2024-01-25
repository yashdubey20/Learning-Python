class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class List:
    def Linkedlist(self):
        self.root= None

    def insertleft(self,data):
        n=Node(data)
        if self.root==None: #no roo there
            self.root=n
        else:
            n.next=self.root #1
            self.root=n #2
            print("Added to List")
    
    def deleteleft(self):
        t=self.root
        self.root=self.root.next
        print(t.data,"Deleted")

    def insertright(self,data):
        n=Node(data)
        if self.root==None: #no roo there
            self.root=n
        else:
            t=self.root #1
            while t.next: #2
                t=t.next
                t.next=n #3
        print("Added to List")

        def deleteRight(self):
            if self.root==None:
                print("Empty List")
            else:
                t=t2=self.root#1
            while t.next!=None:#2
                t2=t
                t=t.next
            t2.next=None#3
            print(t.data,"Deleted")#4
        
        def printlist(self):
            if self.root==None:
                print("Empty List")
            else:
                t=self.root
                while t!=None:
                    print("[",t.data,"]->",end="")
                    t=t.next

obj=List()
obj.Linkedlist()
while True:
    print("1.Insert Left\n2.Delete Left\n3.Insert Right\n4.Delete Right\n5.Print\n:")
    ch=int(input("Enter:"))
    if ch==1:
        data=int(input("Enter data:"))
        obj.insertLeft(data)
    
    elif ch==2:
        obj.deleteLeft()
    
    elif ch==3:
        data=int(input("Enter data:"))
        obj.insertRight(data)
    
    elif ch==4:
        obj.deleteRight()
    
    elif ch==5:
        obj.printList()
        
    elif ch==0:
        print("devloped by amarpanchal.education")
        break
    else:
        print("Wrong input")