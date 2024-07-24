class Solution:
    #TC - O(N), SC - O(N)
    def findTwoElement( self,arr, n): 
        # code here
        hashmap = {i:0 for i in range(1, n+1)}
        for val in arr:
            hashmap[val] += 1
        
        ans = [0,0]
        
        for key,value in hashmap.items():
            if value==0:
                ans[1] = key
            if value==2:
                ans[0] = key
        return ans


    #TC - O(N), SC - O(1)
    def findTwoElement( self,arr, n): 
        # code here
        xor = 0
        for i in range(n):
            xor ^= (i+1)
            xor ^= arr[i]
        
        setbit = xor & ~(xor-1)
        
        A, B = 0, 0
        for i in range(n):
            if arr[i] & setbit:
                A ^= arr[i]
            else:
                B ^= arr[i]
            
            if (i+1) & setbit:
                A ^= (i+1)
            else:
                B ^= (i+1)
        
        flag = False
        for i in arr:
            if i==A:
                flag = True
                break
        
        return [A,B] if flag else [B,A]
        