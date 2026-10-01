# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root











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


def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


tests = [
    ([], []),
    ([1], [1]),
    ([2, 1, 3], [2, 3, 1]),
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([1, 2, None, 3], [1, None, 2, None, 3]),
    ([1, None, 2, None, 3], [1, 2, None, 3]),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    inverted = sol.invertTree(root)
    result = tree_to_list(inverted)

    print(f"Input: {values}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)