# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Givent the array swap the elements in this order:
        


        # Create a stack
        # Iterate through the linked list and append to the stack
        # Iterate through the stack and reorder the elements in the stack
        # The order should be:
        #  ln to point to l1, l1 to point to ln-1, ln-1 to point to l2, l2 to point to ln-2 and so on
        
        # Note:
        # The stack will contain both the elements and the pointers
        # The pointers will be used to point to the next element in the stack

        

        
        if head.next==None:
            return head
        if not head:
            return 
        
        stack=[]
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next

        for i in range(len(stack)//2):
            # J to start at last index of the array
            # Goal not to use multiple loops
            j=-i-1
            temp=stack[i].next
            stack[i].next=stack[j]
            stack[j].next=temp
        stack[len(stack)//2].next=None
    
        return head


# Sample test cases
# [1,2,3,4]
# [1,2,3,4,5]
# Output
# [1,4,2,3]
# [1,5,2,4,3]
       
        

        
            

            