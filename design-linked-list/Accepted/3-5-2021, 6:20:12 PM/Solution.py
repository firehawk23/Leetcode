// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self,val,n=None):
        self.val = val
        self.nxt = n


class MyLinkedList:

    def __init__(self,head=None):
        """
        Initialize your data structure here.
        """
        self.head = head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ind =0
        curr = self.head
        while curr:
            if ind == index:
                return curr.val
            else:
                curr = curr.nxt
            ind = ind+1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val,self.head)
        self.head = new_node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        if self.head is not None:
            while curr.nxt is not None:
                curr = curr.nxt
            new_node = Node(val)
            curr.nxt = new_node
        else:
            new_node = Node(val,self.head)
            self.head = new_node
        self.size+=1
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index>self.size or index<0:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index==0:
                self.addAtHead(val)
            else:
                i = 0
                curr = self.head
                while i!=index-1:
                    curr =curr.nxt
                    i = i+1
                tmp = curr.nxt
                new_node = Node(val,curr.nxt)
                curr.nxt = new_node
                new_node.nxt = tmp
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = None
        index_count = 0
        current_node = self.head
        while current_node is not None:
            if index_count==index:
                if prev is not None:
                    prev.nxt = current_node.nxt
                else:
                    self.head = current_node.nxt
                self.size= self.size-1
            else:
                prev = current_node
                current_node = current_node.nxt
            index_count= index_count+1
        return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)