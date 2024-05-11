#TC - 10^5 * N, SC - 10^5
from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        if start==end: return 0
        q = deque()
        #steps,curr_value
        q.append((0,start))
        distance = [float("inf") for _ in range(100000)]
        distance[start] = 0
        while q:
            steps,curr_value = q.popleft()
            for i in arr:
                temp = (i*curr_value) % 100000
                if temp==end: return steps+1
                if distance[temp]>steps+1:
                    distance[temp] = steps+1
                    q.append((steps+1,temp))
        return -1