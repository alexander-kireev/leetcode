class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def get_levels(root):
    dummy = TreeNode(left=root)

    values = []
    traverse(dummy.left, values)
    traverse(dummy.right, values)
    return values


def traverse(root, values):
    if root is None:
        return values
    
    values.append([root.right, root.left])
    traverse(root.left, values)
    traverse(root.right, values)
    




