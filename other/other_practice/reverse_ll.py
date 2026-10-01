class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def reverse(head):
    next_node = None
    prev = None
    cur = head

    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev


n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

print(reverse(n1).val)
