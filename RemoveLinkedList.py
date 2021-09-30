
# node class:

class Node:
    def __init__(self, val):
        self.next = None
        self.data = val


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes

        if not head or not head.next:
            return head

        dummy = Node(0)
        dummy.next = head

        slow = dummy.next
        fast = dummy.next.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return dummy.next

        pre = None
        fast = dummy

        while fast != slow:
            pre = slow
            slow = slow.next
            fast = fast.next

        pre.next = None

        return dummy.next

    def printList(self, head):
        while head:
            print(head.data)
            head = head.next


sol = Solution()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = one

head = sol.removeLoop(one)
sol.printList(head)
