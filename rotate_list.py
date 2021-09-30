
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def rotate(self, head, k):
        # code here

        dummy = Node(-1)
        dummy.next = head

        tail = dummy
        while tail.next:
            tail = tail.next

        cur = dummy
        while k > 0:
            cur = cur.next
            k -= 1

        tail.next = dummy.next
        head = cur.next
        cur.next = None

        return head


sol = Solution()

# create nodes
one = Node(2)
two = Node(4)
three = Node(7)
four = Node(8)
five = Node(9)

# link them
one.next = two
two.next = three
three.next = four
four.next = five

sol.rotate(one, 5)
