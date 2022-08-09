// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp =ListNode(None,head)
        s=f = tmp
        for i in range(n+1):
            f = f.next
        while f:
            f = f.next
            s = s.next
        s.next = s.next.next
        return tmp.next