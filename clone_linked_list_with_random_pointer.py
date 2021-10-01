'''        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb = None


class Solution:
    # Function to clone a linked list with next and random pointer.

    def copyList(self, head):

        cur = head
        while cur:
            next = cur.next

            cur.next = Node(cur.data)
            cur.next.next = next

            cur = next

        cur = head
        while cur:
            arb = None
            if cur.arb:
                arb = cur.arb.next

            cur.next.arb = arb

            cur = cur.next.next

        cloneHead = cloneCur = Node(0)

        cur = head
        while cur:
            cloneNext = cur.next
            next = cur.next.next

            cloneCur.next = cloneNext
            cloneCur = cloneCur.next

            cur.next = next

            cur = next

        return cloneHead.next
