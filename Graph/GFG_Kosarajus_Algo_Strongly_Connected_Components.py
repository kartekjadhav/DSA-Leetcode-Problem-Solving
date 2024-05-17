#TC - O(V+E), SC - O(V+E) (for new_adj)

class Solution:
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        def dfs(node):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            stack.append(node)
            
        def dfs3(node):
            visited[node] = True
            for neighbour in new_adj[node]:
                if not visited[neighbour]:
                    dfs3(neighbour)
            
        visited = [False]*V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        new_adj = [[] for _ in range(V)]
        for i in range(V):
            for node in adj[i]:
                new_adj[node].append(i)
        
        sccCount = 0
        visited = [False]*V
        while stack:
            node = stack.pop()
            if not visited[node]:
                sccCount+=1
                dfs3(node)
        
        return sccCount