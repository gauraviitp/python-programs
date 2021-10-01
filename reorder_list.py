class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def reorderList(self):
        if (self.head == None or self.head.next == None):
            return

        slow = fast = self.head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        back = slow.next
        slow.next = None

        back = reverse(back)
        front = self.head

        while front and back:
            next = front.next

            front.next = back

            front = back
            back = next

        return self.head


def reverse(head):

    pre = None

    while head:
        next = head.next

        head.next = pre

        pre = head
        head = next

    return pre
