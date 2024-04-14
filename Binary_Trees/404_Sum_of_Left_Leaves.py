# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC - O(N), SC - O(logN)

from typing import Optional
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def inorder(node,isLeft):
            if not node: return 0
            temp = 0
            if isLeft and not node.left and not node.right:
                temp = node.val
            l = inorder(node.left,True)
            r = inorder(node.right,False)
            return l+r+temp

        return inorder(root,False)
