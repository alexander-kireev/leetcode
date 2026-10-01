# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)

from collections import deque

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


tests = [
    ([1], True),
    ([1, 2, 2], True),
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([1, 2, 2, 3, None, None, 3], True),
    ([1, 2, 2, None, 3, 3, None], True),
    ([1, 2, 2, 3, None, 3, None], False),
    ([1, 2, 2, 2, None, 2], False),
    ([1, 2, 2, 3, 4, 4, 3, 5, None, None, 6, 6, None, None, 5], True),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    result = sol.isSymmetric(root)

    print(f"Input: {values}")
    print(f"Expected: {expected}, Got: {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)