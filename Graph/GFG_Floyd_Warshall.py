#TC - O(N^3), SC - O(1)
class Solution:
    def shortest_distance(self, matrix):
        # Code here
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i == j:
                    matrix[i][j] = 0

        for tr in range(n):
            for i in range(n):
                for j in range(n):
                    if i == tr or j == tr or i == j:
                        continue
                    matrix[i][j] = min(matrix[i][j], matrix[i][tr] + matrix[tr][j])

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1

        return matrix