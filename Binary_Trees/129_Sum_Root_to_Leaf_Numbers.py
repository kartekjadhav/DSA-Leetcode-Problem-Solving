# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC - O(N)
#SC - stack space - O(logN), extra space - O(1)

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node,val):
            if not node: return 0
            res = val*10 + node.val
            l = helper(node.left,res)
            r = helper(node.right,res)
            ans = l+r
            if not node.left and not node.right:
                ans += res
            return  ans
        
        return helper(root,0)