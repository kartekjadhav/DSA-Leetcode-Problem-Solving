# 1. Depth First Search
#TC - O(N), SC - stack - O(logk), extra space - O(1)
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(node,depth,currDepth,val):
            if not node: return
            if currDepth==depth-1:
                leftnode = TreeNode(val,node.left,None)
                rightnode = TreeNode(val,None,node.right)
                node.left = leftnode
                node.right = rightnode
                return
            helper(node.left,depth,currDepth+1,val)
            helper(node.right,depth,currDepth+1,val)

        
        if depth==1:
            node = TreeNode(val,root)
            return  node
        helper(root,depth,1,val)
        return root


# 2. Breadth First Search
#TC - O(N), SC - Extra - O(K)
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root,None)
        
        q = deque()
        q.append(root)
        currdepth = 1
        while q:
            size = len(q)
            for i in range(size):
                res = q.popleft()
                if currdepth==depth-1:
                    res.left = TreeNode(val,res.left,None)
                    res.right = TreeNode(val,None,res.right)
                else:    
                    if res.left: q.append(res.left)
                    if res.right: q.append(res.right)
            if currdepth==depth-1: break
            currdepth+=1
        
        return root