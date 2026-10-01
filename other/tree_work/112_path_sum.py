# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, cur_sum):
            if root is None:
                return False
            
            cur_sum += root.val
            if root.left is None and root.right is None:
                return cur_sum == targetSum
            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        
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
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        22,
        True,
    ),
    (
        [1, 2, 3],
        5,
        False,
    ),
    (
        [],
        0,
        False,
    ),
    (
        [1],
        1,
        True,
    ),
    (
        [1],
        2,
        False,
    ),
    (
        [1, 2],
        1,
        False,   # important: root alone is not a path unless it is also a leaf
    ),
    (
        [1, 2],
        3,
        True,
    ),
    (
        [1, -2, -3, 1, 3, -2, None, -1],
        -1,
        True,
    ),
    (
        [1, 2, 3, 4, 5],
        8,
        True,    # 1 -> 2 -> 5
    ),
    (
        [1, 2, 3, 4, 5],
        7,
        True,    # 1 -> 2 -> 4
    ),
]

sol = Solution()

for values, targetSum, expected in tests:
    root = build_tree(values)
    result = sol.hasPathSum(root, targetSum)

    print(f"Input: root = {values}, targetSum = {targetSum}")
    print(f"Expected: {expected}, Got: {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)