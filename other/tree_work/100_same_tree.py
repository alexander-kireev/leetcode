# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))










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
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([], [], True),
    ([], [1], False),
    ([1], [], False),
    ([1], [1], True),
    ([1], [2], False),
    ([1, 2, 3, 4], [1, 2, 3, 4], True),
    ([1, 2, 3, None, 4], [1, 2, 3, 4, None], False),
]

sol = Solution()

for p_values, q_values, expected in tests:
    p = build_tree(p_values)
    q = build_tree(q_values)

    result = sol.isSameTree(p, q)

    print(f"p: {p_values}")
    print(f"q: {q_values}")
    print(f"Expected: {expected}, Got: {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)