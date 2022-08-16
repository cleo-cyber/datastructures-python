# Represents individual member in the list
from itertools import count
from typing import Iterator


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        iterator = self.head
        list_string = ''
        while iterator:
            list_string += str(iterator.data)+'--->'
            iterator = iterator.next  # Following the link of the list
        print(list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        # Iterate as long as the head has a next
        Iterator = self.head
        while Iterator.next:
            Iterator = Iterator.next
        Iterator.next = Node(data, None)

    # Insert values on an empty linked list
    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    # get length of linked list

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    # Remeove list element

    def remove_At(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        # make the head be the next element to the node being removed
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            # stop at the previous element to the element to be removed and modify its link to the next
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_At(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                # Insert where the previous elements next is the insert element next
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        if itr.data == data_after:
            itr.next = Node(data_to_insert, itr.next)
            return
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    def removed_by_value(self,data):
        if self.head is None:
            return
        if self.head.data==0:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
        itr=itr.next

link = LinkedList()

# link.insert_values([1, 3, 4, 5, 56, 67, 786])
# link.remove_At(5)
# link.insert_At(5,7)
# link.insert_after_value(56, 2)
# link.removed_by_value(3)
# link.insert_At(1,45)
# link.print()
