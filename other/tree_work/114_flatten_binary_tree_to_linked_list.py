# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def dfs(root):
            if root is None:
                return None
            
            nodes.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        for i in range(len(nodes)):
            nodes[i].left = None
            nodes[i].right = None
            if i + 1 < len(nodes):
                nodes[i].right = nodes[i + 1]
        



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


def flattened_to_list(root):
    result = []
    current = root

    while current:
        if current.left is not None:
            return "FAIL: left pointer not cleared"
        result.append(current.val)
        current = current.right

    return result


tests = [
    (
        [1, 2, 5, 3, 4, None, 6],
        [1, 2, 3, 4, 5, 6],
    ),
    (
        [],
        [],
    ),
    (
        [0],
        [0],
    ),
    (
        [1, 2, 3],
        [1, 2, 3],
    ),
    (
        [1, 2, None, 3, None, 4],
        [1, 2, 3, 4],
    ),
    (
        [1, None, 2, None, 3, None, 4],
        [1, 2, 3, 4],
    ),
    (
        [1, 2, 5, 3, None, None, 6, 4],
        [1, 2, 3, 4, 5, 6],
    ),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    sol.flatten(root)
    result = flattened_to_list(root)

    print(f"Input:    {values}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)