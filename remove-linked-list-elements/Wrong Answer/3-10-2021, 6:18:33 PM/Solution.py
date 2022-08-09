// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = dum = ListNode(0)
        tmp.next = head
        while tmp.next:
            if tmp.next.val !=  val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return dum.next