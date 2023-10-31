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
        # Deletion of a node
        else:
            print("Value already exists in the tree")
    def find(self,data):
        # Check if the root is None
        if self.root:
            # Call the private function to find the data
            is_found=self._find(data,self.root)
            # Return the result
            return is_found
        else:
            return None
        
    def _find(self,data,curr_node):
        # Check if the data is equal to the current node's data
        if data==curr_node.data:
            return True
        # Check if the data is less than the current node's data
        elif data<curr_node.data:
            # Check if the left child is None
            if curr_node.left==None:
                return False
            # Recursively call the _find function to find the data
            return self._find(data,curr_node.left)
        # Check if the data is greater than the current node's data
        elif data>curr_node.data:
            # Check if the right child is None
            if curr_node.right==None:
                return False
            # Recursively call the _find function to find the data
            return self._find(data,curr_node.right)
        
        # Delete a node
    def delete(self,data):
        # Check if the root is None
        if self.root:
            # Call the private function to delete the data
            self.root=self._delete(data,self.root)
        else:
            return None
        

    def _delete(self,data,curr_node):
        # Check if the data is less than the current node's data
        if data<curr_node.data:
            # Recursively call the _delete function to delete the data
            curr_node.left=self._delete(data,curr_node.left)
        # Check if the data is greater than the current node's data
        elif data>curr_node.data:
            # Recursively call the _delete function to delete the data
            curr_node.right=self._delete(data,curr_node.right)
        # Check if the data is equal to the current node's data
        else:
            # Check if the left child is None
            if curr_node.left==None and curr_node.right==None:
                # Delete the node here
                del curr_node
                return None
            # Check if the left child is None
            elif curr_node.left==None:
                # Delete the node here
                temp_node=curr_node.right
                del curr_node
                return temp_node
            # Check if the right child is None
            elif curr_node.right==None:
                # Delete the node here
                temp_node=curr_node.left
                del curr_node
                return temp_node
            # Check if the left and right children are not None
            else:
                # Find the minimum value in the right subtree
                min_value=self._find_min(curr_node.right)
                # Replace the current node's data with the minimum value
                curr_node.data=min_value
                # Delete the minimum value from the right subtree
                curr_node.right=self._delete(min_value,curr_node.right)
        return curr_node
    
    def _find_min(self,curr_node):
        # Check if the left child is None
        if curr_node.left==None:
            return curr_node.data
        # Recursively call the _find_min function to find the minimum value
        return self._find_min(curr_node.left)
        