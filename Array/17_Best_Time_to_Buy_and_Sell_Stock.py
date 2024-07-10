#TC - O(N), SC -O(1)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i]-mini)
            mini = min(mini, prices[i])
        return maxProfit