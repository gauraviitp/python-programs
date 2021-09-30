class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def getNthFromLast(head, n):
    # code here

    dummy = Node(-1)

    dummy.next = head

    cur = dummy
    while n > 0 and cur:
        cur = cur.next

        n -= 1

    while cur:
        cur = cur.next

        dummy = dummy.next

    return dummy.data
