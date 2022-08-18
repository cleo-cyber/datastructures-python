class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_At_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data)+'--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head

        # while node has next element keep iteration else add a node
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('assertion error')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('assertion error')
        if index == 0:
            self.insert_At_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after(self, data_after, data_to_insert):
        if self.head is None:
            return
        count=0
        itr=self.head
        if itr.data==data_after:
            itr.next=Node(data_to_insert,itr.next)
            return
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            count+=1
            itr=itr.next
    def remove_by_value(self,data):
        if self.head==0:
            return
        if self.head.data==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
        count+=1
        itr=itr.next

# d = LinkedList()
# d.insert_At_beginning(5)
# d.insert_At_beginning(4)
# d.insert_At_beginning(10)
# d.insert_at_end(7)
# d.insert_values([3, 4, 5, 6, 7, 8, 9])
# d.remove_at(3)
# d.insert_at(0,54)
# d.insert_after(3,7)
# d.remove_by_value(4)
# d.print()
# print(d.get_length())
