class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            # Create a private function to insert a node in the BST
            self._insert(data,self.root)
    def _insert(self,data,curr_node):
        # Check if the data is less than the current node's data
        if data<curr_node.data:
            # Check if the left child is None
            if curr_node.left==None:
                # Insert the data here
                curr_node.left=Node(data)
            else:
                # Recursively call the _insert function to insert the data
                self._insert(data,curr_node.left)
        # Check if the data is greater than the current node's data
        elif data>curr_node.data:
            # Check if the right child is None
            if curr_node.right==None:
                # Insert the data here
                curr_node.right=Node(data)
            else:
                # Recursively call the _insert function to insert the data
                self._insert(data,curr_node.right)