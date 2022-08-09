// https://leetcode.com/problems/maximum-width-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.d = defaultdict(list)
        def f(l, p, r):
            if r:
                self.d[l].append(p)
                f(l + 1, 2 * p, r.left)
                f(l + 1, 2 * p + 1, r.right)
        f(0, 0, root)
        return max(max(value) - min(value) + 1 for value in self.d.values())