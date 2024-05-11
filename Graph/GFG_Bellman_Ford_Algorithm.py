#TC - O(V*E), SC - O(V)
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        maxi = 10**8
        distance = [maxi]*V
        distance[S] = 0
        for i in range(V-1):
            for start,end,wt in edges:
                if distance[start]!=maxi and distance[start] + wt < distance[end]:
                    distance[end] = distance[start] + wt
        
        #Negative Cycle Detection
        for start,end,wt in edges:
            if distance[start]!=maxi and distance[start] + wt < distance[end]:
                return [-1]

        return  distance