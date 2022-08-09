// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q =[root]
        level = []
        while q:
            l,bfs = [],[]
            for i in q:
                l.append(i.val)
                if i.left:
                    bfs.append(i.left)
                if i.right:
                    bfs.append(i.right)
            q=bfs
            level.append(l)
        return level
                    
        
        