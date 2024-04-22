#TC - O(V) + O(2*E)
#SC - O(N)
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, v: int, adj: List[List[int]]) -> List[int]:
        # code here
        visit = [0]*v
        visit[0] = 1
        q = Queue()
        q.put(0)
        ans = []
        
        while not q.empty():
            node = q.get()
            ans.append(node)
            for i in adj[node]:
                if not visit[i]:
                    visit[i] = 1
                    q.put(i)
        return ans