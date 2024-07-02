#Here you can include fee at selling time or at buying time as well. 
#TC - O(N), SC - extra space - O(2*2), stack space - O(1)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        prev = [0]*2
        curr = [0]*2

        for ind in range(n-1, -1, -1):
            #Buy
            curr[1] = max(-prices[ind] + prev[0], prev[1])
            #Sell
            curr[0] = max(prices[ind] - fee + prev[1], prev[0])
            prev = curr[:]                

        return prev[1]