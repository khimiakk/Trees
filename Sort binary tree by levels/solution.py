"""
Sort binary tree by levels
"""

def tree_by_levels(node):
    """
    Returns the list with elements from tree sorted by levels
    """
    if node is None:
        return []

    queue = []
    result = []
    queue.append(node)

    while queue:

        for _ in range(len(queue)):
            node = queue.pop(0)
            result.append(node.value)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return result
