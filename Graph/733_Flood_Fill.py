#X - N*M
#DFS - TC - O(X) + O(X*4), SC - stack space - O(X)
#BFS - TC - O(X) + O(X*4), SC - extra space - O(X)
from typing import List
from queue import Queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(r,c,color,prevColor):
            if image[r][c]==color: return
            image[r][c] = color
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for a,b in directions:
                new_r,new_c = r+a,c+b
                if 0<= new_r <len(image) and 0<= new_c <len(image[0]) and image[new_r][new_c]==prevColor:
                    dfs(new_r,new_c,color,prevColor)
    
        def bfs(r,c,color,prevColor):
            if image[r][c]==color: return
            q = Queue()
            q.put((r,c))
            image[r][c] = color
            while not q.empty():
                i,j = q.get()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for a,b in directions:
                    new_r,new_c = i+a,j+b
                    if 0<= new_r <len(image) and 0<= new_c <len(image[0]) and image[new_r][new_c]==prevColor:
                        image[new_r][new_c] = color
                        q.put((new_r,new_c))
        
        bfs(sr,sc,color,image[sr][sc])
        return image