// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head== Null :
            return head
        slow =  head
        fast = head.next
        while(fast !=Null and fast.next!=Null and slow!=Null):
            if(fast==slow):
                return True
            fast =fast.next.next
            slow = slow.next
        return False