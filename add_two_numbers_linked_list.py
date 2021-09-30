class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list

        def reverse(head):

            pre = None

            while head:
                next = head.next

                head.next = pre

                pre = head
                head = next

            return pre

        first = reverse(first)
        second = reverse(second)

        head = cur = Node(0)
        carry = 0

        while first or second or carry:
            s = carry

            if first:
                s += first.data
                first = first.next
            if second:
                s += second.data
                second = second.next

            cur.next = Node(s % 10)
            cur = cur.next

            carry = s//10

        return reverse(head.next)
