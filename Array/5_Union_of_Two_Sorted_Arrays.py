class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        
        i, j = 0, 0
        ans = []
        while i<n and j<m:
            while i<n-1 and arr1[i]==arr1[i+1]: i+=1
            while j<m-1 and arr2[j]==arr2[j+1]: j+=1
            if arr1[i]==arr2[j]:
                ans.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]>arr2[j]:
                ans.append(arr2[j])
                j+=1
            else:
                ans.append(arr1[i])
                i+=1
            
        while i<n:
            while i<n-1 and arr1[i]==arr1[i+1]: i+=1
            ans.append(arr1[i])
            i+=1
        
        while j<m:
            while j<m-1 and arr2[j]==arr2[j+1]: j+=1
            ans.append(arr2[j])
            j+=1
        
        return ans