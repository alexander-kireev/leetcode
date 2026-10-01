class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_values(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # trim trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result








def invert_tree(root):
    
    if root is None:
        return None
    

    temp = root.right
    root.right = root.left
    root.left = temp

    invert_tree(root.right)
    invert_tree(root.left)

    return root




#        4
#      /   \
#     2     7
#    / \   / \
#   1   3 6   9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted = invert_tree(root)

print(level_order_values(inverted))
# expected: [4, 7, 2, 9, 6, 3, 1]