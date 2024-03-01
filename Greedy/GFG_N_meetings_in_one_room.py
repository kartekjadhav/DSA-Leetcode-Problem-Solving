class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        intervals = [[end[i],start[i]] for i in range(n)]
        intervals.sort()
        prev, curr, count = 0, 1, 1
        
        while curr<n:
            if intervals[curr][1] > intervals[prev][0]: 
                count+=1
                prev = curr
                curr += 1
            else:
                curr+=1
        return count