#Take Disjoint Set template from Disjoint_Set.py in this list

#TC - O(V+E) + O(V), SC - O(1)
from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsj = DisjointSet(n) # type: ignore 
        extra = 0
        for u,v in connections:
            if dsj.findPar(u)!=dsj.findPar(v):
                dsj.unionSize(u,v)
            else: extra+=1
        #Finding no. of components
        compCount = 0
        for i in range(n):
            if i==dsj.findPar(i):
                compCount+=1
        return compCount-1 if compCount-1<=extra else -1 