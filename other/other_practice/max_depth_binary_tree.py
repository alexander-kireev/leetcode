class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    
    if root is None:
        return 0
    
    left = max_depth(root.left) + 1
    right = max_depth(root.right) + 1

    return max(left, right)






root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_depth(root))  # expected: 3


root = None
print(max_depth(root))  # expected: 0


root = TreeNode(1)
print(max_depth(root))  # expected: 1



root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(max_depth(root))  # expected: 4