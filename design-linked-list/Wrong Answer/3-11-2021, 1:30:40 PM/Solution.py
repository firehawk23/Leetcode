// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_head = Node(0)
        self.d_tail = Node(0)
        self.d_tail.prev = self.d_head
        self.d_head.next = self.d_tail
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index>self.size:
            return -1
        curr = self.d_head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr = Node(val)
        curr.next = self.d_head.next
        curr.prev = self.d_head
        self.d_head.next.prev = curr 
        self.d_head.next = curr
        self.size+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = Node(val)
        curr.prev = self.d_tail.prev
        curr.next = self.d_tail
        self.d_tail.prev.next = curr
        self.d_tail.prev = curr
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<0 or index>self.size:
            return
        elif index==0:
            addAtHead(val)
        elif index==self.size:
            addAtTail(val)
        else:
            curr = self.d_head.next
            for i in range(index-1):
                curr = curr.next
            n = Node(val)
            n.next = curr.next
            n.prev = curr
            curr.next.prev =n
            curr.next = n
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index>self.size:
            return
        curr = self.d_head.next
        for i in range(index):
            curr = curr.next
        curr.next.next.prev = curr
        curr.next = curr.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)