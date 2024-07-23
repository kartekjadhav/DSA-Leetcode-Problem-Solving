#TC - O(N*M), SC - O(N*M)
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,m-1,0,n-1
        ans = []

        while top<=bottom and left<=right:
            #insert top row
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top+=1
            if top>bottom: break

            #insert right col
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1
            if right<left: break

            #insert bottom row
            for j in range(right, left-1, -1):
                ans.append(matrix[bottom][j])
            bottom-=1
            if bottom<top: break

            #insert left col
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left+=1
            if left>right: break
        
        return ans
