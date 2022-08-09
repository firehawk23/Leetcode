// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (not head or head.next == None):
            return False
        tmp = head
        hsh = set({})
        while(tmp):
            if tmp in hsh:
                return True
            hsh.add(tmp)
            tmp = tmp.next
        return False
            