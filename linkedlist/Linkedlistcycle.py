# Given a linked list, determine if it has a cycle in it.

#Example
#Given -21->10->4->5, tail connects to node index 1, return true    
#Procedure Using: Set
#Time Complexity: O(n)
#Space Complexity: O(n)
#Procedure:
#   1. Create a set
#   2. Traverse the linked list
#   3. If the node is in the set, return True
#   4. Else, add the node to the set
#   5. Return False
#Code:
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Solution 1
        s=set()
        
        while head:
            if head in s:
                return True
            else:
                s.add(head)
                head=head.next
                
        return False
    

    def hascycle2(self,head,pos):
        # Solution 2
        # Using if statement checking if pos is None
        # If pos is None, return False
        # Else, return True

        # Challange: How to check if the linked list is valid?
        # If the linked list is valid, return True
        # Some case when pos is -1 still returns True and it is not valid
        # Else, return False
        # Valid means:
        #   1. head is not None
        
        if not head:
            return False
        if not head.next:
            return False
        if pos is None:
            return False
        else:
            if pos<0:
                return False
            return True
    def hascyle3(self,head):
        # Floyd's Cycle Detection Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Procedure:
        #   1. Create two pointers, slow and fast
        #   2. Slow pointer moves one step at a time    
        #   3. Fast pointer moves two steps at a time
        #   4. If slow pointer and fast pointer meet, return True
        #   5. Else, return False
        #   6. If fast pointer or fast pointer.next is None, return False

        if not head:
            return False
        if not head.next:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True



   