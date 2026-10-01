
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)




tests = [
    ([], 0),
    ([1], 1),
    ([1, None, 2], 2),
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, 2, 3, 4, 5, None, 6, 7], 4),
    ([1, 2, None, 3, None, 4, None, 5], 5),
]


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
    ([], 0),
    ([1], 1),
    ([1, None, 2], 2),
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, 2, 3, 4, 5, None, 6, 7], 4),
    ([1, 2, None, 3, None, 4, None, 5], 5),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    result = sol.maxDepth(root)
    print(f"Input: {values}")
    print(f"Expected: {expected}, Got: {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)