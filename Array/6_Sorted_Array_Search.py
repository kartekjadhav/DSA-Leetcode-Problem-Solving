class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        start, end = 0, N-1
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid]==K: return 1
            if arr[mid]<K: 
                start = mid+1
            else:
                end = mid-1
        return -1