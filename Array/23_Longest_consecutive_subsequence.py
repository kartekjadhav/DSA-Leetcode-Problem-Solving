class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    #TC - O(NLOGN), SC - O(1)
    def findLongestConseqSubseq(self,arr, N):
        #code here
        arr.sort()
        maxlen = 1
        curr_len = 1
        for i in range(1, N):
            if arr[i]==1+arr[i-1]:
                curr_len +=1
                maxlen = max(maxlen, curr_len)
            elif arr[i]==arr[i-1]: continue
            else:
                curr_len = 1
        return maxlen
    
    #TC - O(N+K) where K is lenght of longest consecutive sequence, SC - O(N)
    def findLongestConseqSubseq(self,arr, N):
        #code here
        maxi = 1
        hashmap = {}
        for i in range(N): hashmap[arr[i]] = i
        for i in range(N):
            if arr[i]-1 not in hashmap:
                curr = 0
                temp = arr[i]
                while temp in hashmap: 
                    curr+=1
                    temp+=1
                maxi = max(maxi, curr)
        return maxi