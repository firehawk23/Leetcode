// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        e_head = head.next
        while even and even.next:
            odd.next=odd=even.next
            even.next=even = odd.next
        odd.next = e_head
        return head