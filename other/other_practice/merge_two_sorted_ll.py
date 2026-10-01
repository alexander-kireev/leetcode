class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode()
    cur = dummy

    for value in values:
        cur.next = ListNode(value)
        cur = cur.next

    return dummy.next


def print_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)






def merge_two_lists(h1, h2):
    dummy = ListNode()
    cur = dummy

    while h1 and h2:
        if h1.val < h2.val:
            cur.next = h1
            h1 = h1.next
            cur = cur.next
        else:
            cur.next = h2
            h2 = h2.next
            cur = cur.next
        
    cur.next = h1 if h1 else h2

    return dummy.next



list1 = build_list([1, 2, 4])
list2 = build_list([1, 3, 4])

merged = merge_two_lists(list1, list2)
print_list(merged)