class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print('Empty linked list')
            return
        itr = self.head
        pfstr = ''
        while itr:
            pfstr = str(itr.data)+'--->'
            itr = itr.next
        print(pfstr)

    def get_last_node(self):
        if self.head is None:
            return
        itr=self.head

        while itr:
            itr=itr.next

        return itr


    def print_backward(self):
        if self.head is None:
            raise Exception('List is Empty')
        last_node=self.get_last_node()
        itr=last_node
        plstr=''
        while itr:
            plstr+=str(itr.data)+'--->'
            itr=itr.prev
        print(plstr)

    def get_length(self):
        if self.head is None:
            return
        itr= self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_At_beginning(self,data):
        if self.head is None:
            node=Node(data,self.head,None)
            self.head=node
        else:
            node=Node(data,self.head,None)
            self.head.prev=node

