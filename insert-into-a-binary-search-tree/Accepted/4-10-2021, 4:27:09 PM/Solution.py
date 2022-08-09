// https://leetcode.com/problems/insert-into-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        flag = 0
        node =root
        while node:
            if val<node.val:
                if node.left:
                    node = node.left
                else:
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    flag=1
                    break
        if flag:
            node.right = TreeNode(val)
        else:
            node.left  = TreeNode(val)
        return root