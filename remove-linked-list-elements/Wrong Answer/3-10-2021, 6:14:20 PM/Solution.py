// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        curr = ListNode(head)
        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr =curr.next
        return curr