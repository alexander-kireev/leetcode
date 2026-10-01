from math import inf



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    return dfs(root, -inf, inf)







def dfs(node, low, high):
    if node is None:
        return True
    
    if node.val <= low or node.val >= high:
        return False
    
    left = dfs(node.left, low, node.val)
    right = dfs(node.right, node.val, high)

    return left and right


# #     2
# #    / \
# #   1   3

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# print(is_valid_bst(root))  # expected: True

# #     5
# #    / \
# #   1   4
# #      / \
# #     3   6

# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)

# print(is_valid_bst(root))  # expected: False


#      10
#     /  \
#    5    15
#        /  \
#       6    20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print(is_valid_bst(root))  # expected: False

# root = TreeNode(1)

# print(is_valid_bst(root))  # expected: True

# root = None

# print(is_valid_bst(root))  # expected: True

#     2
#    / \
#   2   3

# root = TreeNode(2)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# print(is_valid_bst(root))  # expected: False