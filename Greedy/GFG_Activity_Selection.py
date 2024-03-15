#TC - O(NLOGN)
#SC - O(N)

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        interval = [(start[i], end[i]) for i in range(n)]
        interval.sort(key=lambda x:x[1])
        count = 1
        prev = interval[0][1]
        i = 1
        while i<n:
            curr = interval[i][0]
            if prev < curr:
                count += 1
                prev = interval[i][1]
            i+=1
        return count