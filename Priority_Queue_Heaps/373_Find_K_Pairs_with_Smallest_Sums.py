# Solution 1
# TC - m*nlog(K)
from ast import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hp = []
        for i in nums1:
            for j in nums2:
                total = i+j
                if len(hp)<k:
                    heapq.heappush(hp,(-total, [i,j]))
                elif len(hp)==k and -1*hp[0][0]>total:
                    heapq.heappop(hp)
                    heapq.heappush(hp,(-total,[i,j]))
                else:
                    break
        result = []
        while len(hp)>0:
            _,pair = heapq.heappop(hp)
            result.append(pair)
        return result


# Solution 2
# TC - Klog(m*n)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n = len(nums1), len(nums2)
        hp = [(nums1[0]+nums2[0],(0,0))]
        visited = {(0,0)}
        result = []
        while k>0 and hp:
            _ , pair = heapq.heappop(hp)
            i,j = pair
            result.append([nums1[i],nums2[j]])
            if i+1<m and j<n and (i+1,j) not in visited:
                total = nums1[i+1] + nums2[j]
                heapq.heappush(hp,(total,(i+1,j)))
                visited.add((i+1,j))
            if i<m and j+1<n and (i,j+1) not in visited:
                total = nums1[i] + nums2[j+1]
                heapq.heappush(hp,(total,(i,j+1)))
                visited.add((i,j+1))
            k-=1
        return result