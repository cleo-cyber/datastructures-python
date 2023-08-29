class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,head=None):
        self.head=head
        def append(self,newnode):
            current=self.head
            if current:
                while current.next:
                    current=current.next
                current.next=newnode
            else:
                self.head=newnode
        def delete(self,value):
            current=self.head
            if current.value==value:
                self.head=current.next
            else:
                while current.next:
                    if current.next.value==value:
                        current.next=current.next.next
                        break
                    current=current.next
        def insert(self,newelement,position):
            current=self.head
            count=1
            if position==1:
                newelement.next=current
                self.head=newelement
            while current:
                 if count+1==position:
                        newelement.next=current.next
                        current.next=newelement
                        break
                 else:
                        current=current.next
                        count+=1
                        
                