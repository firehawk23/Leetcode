// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==1:
            return self.reverseTill(head,right)
        head.next = self.reverseBetween(head.next,left-1,right-1)
        return head
        
    
    def reverseTill(self,head, n):
        if n==1:
            self.successor = head.next
            return head

        last = self.reverseTill(head.next,n-1)
        head.next.next =head
        head.next = self.successor
        
        return last