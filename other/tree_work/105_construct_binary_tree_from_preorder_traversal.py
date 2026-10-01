# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        val = preorder[0]
        mid = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root



from collections import deque

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
    (
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
        [3, 9, 20, None, None, 15, 7],
    ),
    (
        [-1],
        [-1],
        [-1],
    ),
    (
        [1, 2, 3],
        [2, 1, 3],
        [1, 2, 3],
    ),
    (
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 2, None, 3, None, 4],
    ),
    (
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, None, 2, None, 3, None, 4],
    ),
    (
        [8, 4, 2, 6, 12, 10, 14],
        [2, 4, 6, 8, 10, 12, 14],
        [8, 4, 12, 2, 6, 10, 14],
    ),
]

sol = Solution()

for preorder, inorder, expected in tests:
    root = sol.buildTree(preorder, inorder)
    result = tree_to_list(root)

    print(f"preorder: {preorder}")
    print(f"inorder:  {inorder}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)