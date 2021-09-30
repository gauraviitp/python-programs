class Solution:
    def isPalindrome(self, head):

        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        back = slow.next
        slow.next = None

        pre = None

        while back:
            next = back.next

            back.next = pre

            pre = back
            back = next

        front = head
        while front and pre:
            if front.data != pre.data:
                return False

            front = front.next
            pre = pre.next

        return True
