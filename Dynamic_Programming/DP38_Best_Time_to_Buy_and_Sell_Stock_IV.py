#This question is same as DP37_Best_Time_to_Buy_and_Sell_Stock_III.py
#TC - O(N*2*K), SC - extra space - O(2*2*K) stack space - O(1)
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        prev = [0]*(2*k+1)
        curr = [0]*(2*k+1)

        for ind in range(n-1, -1, -1):
            for transaction in range(2*k):
                profit = 0
                #Sell
                if transaction%2:
                    profit = max(prices[ind] + prev[transaction+1], prev[transaction])
                #Buy
                else:
                    profit = max(-prices[ind] + prev[transaction+1], prev[transaction])
                
                curr[transaction] = profit
            prev = curr[:]

        return prev[0]