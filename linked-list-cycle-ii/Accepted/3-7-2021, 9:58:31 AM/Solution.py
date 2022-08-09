// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None :
            return head
        slow =  head
        l=[]
        while slow :
            l.append(slow)
            slow= slow.next
            if slow in l:
                return slow
        return