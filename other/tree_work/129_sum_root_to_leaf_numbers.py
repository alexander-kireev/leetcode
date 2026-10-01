# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, cur_sum):
            if root is None:
                return 0
            
            cur_sum = (cur_sum * 10) + root.val
            
            if root.left is None and root.right is None:
                return cur_sum
            
            return dfs(root.left, cur_sum) + dfs(root.right, cur_sum)

        return dfs(root, 0)




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
    (
        [1, 2, 3],
        25,      # 12 + 13
    ),
    (
        [4, 9, 0, 5, 1],
        1026,    # 495 + 491 + 40
    ),
    (
        [1],
        1,
    ),
    (
        [0, 1, 2],
        3,       # 01 + 02 = 1 + 2
    ),
    (
        [1, 2, None, 3, None, 4],
        1234,
    ),
    (
        [1, None, 2, None, 3, None, 4],
        1234,
    ),
    (
        [9, 9, 9, 9, None, None, 9],
        1998,    # 999 + 999
    ),
    (
        [1, 0, 5, 0, 1, None, 6],
        117,     # 100 + 101 + 156
    ),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    result = sol.sumNumbers(root)

    print(f"Input:    {values}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)