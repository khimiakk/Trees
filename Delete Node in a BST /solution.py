"""
Given a root node reference of a BST and a key, 
delete the node with the given key in the BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    Search for a node to remove.
    If the node is found, delete the node.
    """

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                new = root.right
            while new.left:
                new = new.left
            root.val = new.val
            root.right = self.deleteNode(root.right, new.val)

        return root
