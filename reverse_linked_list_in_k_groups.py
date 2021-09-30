class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverse(self, head, k):
        # Code here

        resHead = cur = Node(0)

        while head:

            n = k

            pre = None
            tail = head
            while head and n > 0:
                next = head.next

                head.next = pre

                pre = head
                head = next
                n -= 1

            cur.next = pre
            cur = tail

        return resHead.next
