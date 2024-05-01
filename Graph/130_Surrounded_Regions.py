#TC - O(N*M*4), SC - O(N*M)

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            canConvert[r][c] = False
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<=new_r<len(board) and 0<=new_c<len(board[0]) and board[new_r][new_c]=='O' and canConvert[new_r][new_c]:
                    dfs(new_r,new_c)
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m,n = len(board),len(board[0])
        canConvert = [[True]*n for _ in range(m)]

        #Traversing first and last row
        for j in range(n):
            if board[0][j]=='O' and canConvert[0][j]:
                dfs(0,j)

            if board[m-1][j]=='O' and canConvert[m-1][j]:
                dfs(m-1,j)

        #Traversing first and last col
        for i in range(m):
            if board[i][0]=='O' and canConvert[i][0]:
                dfs(i,0)

            if board[i][n-1]=='O' and canConvert[i][n-1]:
                dfs(i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and canConvert[i][j]:
                    board[i][j] = 'X'
        