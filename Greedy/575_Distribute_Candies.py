#TC - O(N)
#SC - O(N)

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hashset = set()
        for candy in candyType:
            hashset.add(candy)
        k = len(candyType)//2
        return  min(k, len(hashset))
            