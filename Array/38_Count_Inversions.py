#TC - O(NlogN), SC - O(N)
class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(start, mid, end):
            count = 0
            i, j = start, mid+1
            temp = []
            while i<=mid and j<=end:
                if arr[i] > arr[j]:
                    count += mid - i +1
                    temp.append(arr[j])
                    j+=1
                else:
                    temp.append(arr[i])
                    i+=1
            while i<=mid:
                temp.append(arr[i])
                i+=1
            while j<=end:
                temp.append(arr[j])
                j+=1
            
            arr[start:end+1] = temp
            return count
            
        
        
        def divide(start, end):
            if start==end: return 0
            
            mid = start + (end-start)//2
            left = divide(start, mid)
            right = divide(mid+1, end)
            
            inversions = merge(start, mid, end)
            return left + right + inversions
        
        return divide(0,n-1)