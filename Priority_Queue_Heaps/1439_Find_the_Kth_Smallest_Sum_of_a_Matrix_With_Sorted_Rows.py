#TC - K*log(m * n^m) 
from ast import List
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m,n = len(mat), len(mat[0])
        temp = [0]*m
        total = sum([mat[i][0] for i in range(m)])
        hp = [(total,temp)]
        ans = 0
        visited = set()
        while k>0 and hp:
            ans, col = heapq.heappop(hp)
            for i in range(m):
                res = col[:]
                if res[i]+1<n: 
                    res[i]+=1
                    new_sum = ans - mat[i][col[i]] + mat[i][res[i]]
                    if tuple(res) not in visited:
                        heapq.heappush(hp,(new_sum,res))
                        visited.add(tuple(res))
            k-=1
        return ans