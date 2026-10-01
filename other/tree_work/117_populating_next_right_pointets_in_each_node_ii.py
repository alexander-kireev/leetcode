
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next





class Solution:
    def connect(self, root: 'Node') -> 'Node':

        queue = []
        if root:
            queue.append(root)
 
        while queue:
            new_queue = []
            prev = None

            for i in range(len(queue)):
                
                node = queue[i]

                if prev:
                    prev.next = node
                
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

                prev = node

            queue = new_queue

        return root
    



from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_tree(values):
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1

    return root


def serialize_next_pointers(root):
    if not root:
        return []

    result = []
    level_start = root

    while level_start:
        current = level_start
        next_level_start = None

        while current:
            result.append(current.val)

            if not next_level_start:
                if current.left:
                    next_level_start = current.left
                elif current.right:
                    next_level_start = current.right

            current = current.next

        result.append("#")
        level_start = next_level_start

    return result


tests = [
    (
        [],
        [],
    ),
    (
        [1],
        [1, "#"],
    ),
    (
        [1, 2, 3],
        [1, "#", 2, 3, "#"],
    ),
    (
        [1, 2, 3, 4, 5, None, 7],
        [1, "#", 2, 3, "#", 4, 5, 7, "#"],
    ),
    (
        [1, 2, 3, 4, None, None, 7],
        [1, "#", 2, 3, "#", 4, 7, "#"],
    ),
    (
        [1, None, 2, None, 3, None, 4],
        [1, "#", 2, "#", 3, "#", 4, "#"],
    ),
    (
        [1, 2, None, 3, None, 4, None],
        [1, "#", 2, "#", 3, "#", 4, "#"],
    ),
    (
        [1, 2, 3, None, 5, None, 7, 8, None, None, 9],
        [1, "#", 2, 3, "#", 5, 7, "#", 8, 9, "#"],
    ),
]

sol = Solution()

for values, expected in tests:
    root = build_tree(values)
    connected = sol.connect(root)
    result = serialize_next_pointers(connected)

    print(f"Input:    {values}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 40)