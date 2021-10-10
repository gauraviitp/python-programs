# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        p = 11
        mod = 10**7

        hashList = 0

        lenList = 0
        while head:
            hashList = (hashList * p + head.val) % mod
            lenList += 1

            head = head.next

        pPow = 11**(lenList-1)

        def recurse(node, hashPath, listPath):
            if not node:
                return hashPath == hashList

            if len(listPath) >= lenList:
                hashPath = (hashPath - listPath[-lenList] * pPow) % mod

            hashPath = (hashPath * p + node.val) % mod

            if hashPath == hashList:
                return True

            listPath.append(node.val)
            ret = recurse(node.left, hashPath, listPath) or recurse(
                node.right, hashPath, listPath)
            listPath.pop()

            return ret

        return recurse(root, 0, [])
