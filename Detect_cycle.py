# User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''


class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):

        if not head or not head.next:
            return False

        slow = head.next

        fast = head.next.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return slow == fast
