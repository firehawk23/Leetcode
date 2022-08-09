// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def dfs(node):
            if node is None:
                return 0
            d1 = dfs(node.left)
            d2 = dfs(node.right)
            
            if abs(d1-d2)>1:
                self.flag = False
                return float('inf')
            return max(d1,d2)+1
        dfs(root)
        return self.flag