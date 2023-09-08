# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        current=head
        val_arr=[]

        while current:
            val_arr.append(current.val)
            current = current.next
        # l,r=0,len(val_arr)-1
        if len(val_arr)==1:
            return True
        for i in range(len(val_arr)//2):
            right=len(val_arr)-i-1
            left=i

            if val_arr[left] !=val_arr[right]:
                return False
        return True




        