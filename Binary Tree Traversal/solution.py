"""
Three functions that will print the tree in pre-order, in-order, and post-order.
"""

class Node:
    """
    Class representing a node
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def pre_order(node):
    """
    Visit the root, traverse the left subtree, traverse the right subtree.
    """

    preorder = []
    if node is None:
        return []
    preorder.append(node.data)
    preorder += pre_order(node.left)
    preorder += pre_order(node.right)

    return preorder

# In-order traversal
def in_order(node):
    """
    Traverse the left subtree, visit the root, traverse the right subtree.
    """
    inorder = []
    if node is None:
        return []
    inorder += in_order(node.left)
    inorder.append(node.data)
    inorder += in_order(node.right)

    return inorder

# Post-order traversal
def post_order(node):
    """"
    Traverse the left subtree, traverse the right subtree, visit the root.
    """

    postorder = []
    if node is None:
        return []
    postorder += post_order(node.left)
    postorder += post_order(node.right)
    postorder.append(node.data)

    return postorder
