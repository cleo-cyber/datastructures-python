# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Compare the val root node
        # Decide on direction 
        # Repeat the process till val is found 
        # If val.right and .left is none return node.
        # If tree is empty return null
        # If length of tree is empty return null
        # If tree has child nodes return left then right
        # If val is root  return root

        while root:
            if root.val==val:
                # arr.append(root)
                return root
            elif root.val<val:
                root=root.right
            elif root.val>val:
                root=root.left
            # if root.val==val and root.left is None and root.right is None:
            #     arr.append(root.val)
            else:
                return None
        return None



