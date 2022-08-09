// https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if key<root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        elif key>root.val:
            root.right = self.deleteNode(root.right,key)
            return root
        else:
            small = self.findSmall(root.right)
            if not small:
                return root.left
            small.left = root.left
            return root.right
            
    def findSmall(self,root):
        if not root:
            return
        while root:
            root = root.left
        return root