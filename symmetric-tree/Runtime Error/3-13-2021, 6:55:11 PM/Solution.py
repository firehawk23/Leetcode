// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isym(root.left,root.right)
    
    def isym(self,root1: TreeNode,root2: TreeNode):
        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        if not root1 or not root2:
            return False
        return (self.isym(root1.left,root2.right) and self.isym(root1.right,root2.left))