#Note - Use DisjointSet template from DisjointSet.py file in this list
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxr,maxc = 0,0
        for r,c in stones:
            maxr = max(maxr,r)
            maxc = max(maxc,c)
        stoneSet = set()
        dsj = DisjointSet(maxr + maxc + 1) # type: ignore
        for r,c in stones:
            new_c = maxr+1 + c
            rPar,cPar = dsj.findPar(r),dsj.findPar(new_c)
            stoneSet.add(r)
            stoneSet.add(new_c)
            if rPar!=cPar:
                dsj.unionSize(rPar,cPar)
        
        count = 0
        for node in stoneSet:
            if node==dsj.findPar(node):
                count+=1
        
        return len(stones) - count