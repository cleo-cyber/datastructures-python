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
        l,r=0,len(val_arr)-1
        if len(val_arr)==1:
            return True
        while l<r:
            if val_arr[l]!=val_arr[r]:
                return False
            l+=1
            r-=1
        return True





        