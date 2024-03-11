#TC - N*logN
#SC - O(1)

class Solution:    
    def minimumPlatform(self,n,arr,dep):
        sarr = sorted(arr)
        sdep = sorted(dep)
        
        i,j = 0,0
        count,ans = 0,0
        
        while i<n and j<n:
            if sarr[i] <= sdep[j]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            ans = max(count,ans)
        return ans