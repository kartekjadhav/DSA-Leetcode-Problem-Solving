#TC - O(NLOGN)
#SC - O(1)

class Solution:
    def assignMiceHoles(self, n , m , h):
        # code here
        mice = sorted(m)
        hole = sorted(h)
        minutes ,max_time = 0,0
        
        for i in range(n):
            minutes = abs(hole[i] - mice[i])
            max_time = max(max_time, minutes)
            
        return max_time