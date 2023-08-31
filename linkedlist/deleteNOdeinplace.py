# There is a singly-linked list head and we want to delete a node node in it.

# You are given the node to be deleted node. You will not be given access to the first node of head.

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input:  node
# Output: List with node deleted
# Example: 1->2->3->4, node = 3
#          1->2->4

# Approach: Copy the value of the next node to the node to be deleted and delete the next node.
# Reason: We can't delete the current node because we don't have access to the previous node.
#         We can't make the current node point to the next node because we don't have access to the previous node.
#         So, we copy the value of the next node to the current node and delete the next node.
#         This is possible because we are given that the node to be deleted is not the last node in the linked list.


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr=node.next
        node.val=curr.val
        node.next=curr.next



            

# Time Complexity: O(1)
# Space Complexity: O(1)