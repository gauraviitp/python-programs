class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def intersetPoint(head1, head2):

    def len(head):
        n = 0

        while head:
            n += 1
            head = head.next

        return n

    len1 = len(head1)
    len2 = len(head2)

    while len1 < len2:
        head2 = head2.next
        len2 -= 1

    while len2 < len1:
        head1 = head1.next
        len1 -= 1

    while head1 and head2:
        if head1 == head2:
            return head1.data

        head1 = head1.next
        head2 = head2.next

    return -1
