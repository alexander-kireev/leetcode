class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False



n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)


print(has_cycle(n1))