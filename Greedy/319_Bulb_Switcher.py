#TC - O(LOGN)
#SC - O(1)
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))