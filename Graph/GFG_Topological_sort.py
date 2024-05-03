#TC - O(V) + O(V+E), SC - stack - O(V), extra - O(V)

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        def dfs(node):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            stack.append(node)
        
        visited = [False]*V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans