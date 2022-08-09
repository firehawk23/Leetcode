// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder = []
        self.inOrder(root)
        for i in range(1,len(self.inorder)):
            if self.inorder[i-1]>=self.inorder[i]:
                return False
        return True
        
    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        self.inorder.append(root.val)
        self.inOrder(root.right)