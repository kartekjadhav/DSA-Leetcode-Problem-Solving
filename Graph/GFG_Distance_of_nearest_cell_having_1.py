#BFS will oonly work here
#TC - O(N*M*4), SC - O(N*M)

from collections import deque

class Solution:
    # Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, matrix):
        # Code here
        m, n = len(matrix), len(matrix[0])
        distance = [[0] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    q.append((i, j, 0))
                    matrix[i][j] = -1
                    distance[i][j] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, dist = q.popleft()
            for a, b in directions:
                new_r, new_c = r + a, c + b
                if 0 <= new_r < m and 0 <= new_c < n and matrix[new_r][new_c] != -1:
                    q.append((new_r, new_c, dist + 1))
                    matrix[new_r][new_c] = -1
                    distance[new_r][new_c] = dist + 1
        
        return distance

        
'''
Using `deque` from the `collections` module is often more efficient than using `Queue` from the `queue` module in Python for several reasons:

1. **Implementation:** `deque` is implemented in C as a doubly-linked list, which makes it more efficient for operations like appending and popping elements from both ends. On the other hand, `Queue` from the `queue` module is implemented using a synchronized queue, which adds overhead for synchronization in multi-threaded environments.

2. **Performance:** `deque` operations such as `append` and `popleft` have O(1) time complexity, making them efficient for FIFO operations. In contrast, `Queue` operations such as `put` and `get` are thread-safe and have a higher overhead due to locking mechanisms, which can degrade performance, especially in single-threaded applications.

3. **Flexibility:** `deque` provides additional functionalities beyond what `Queue` offers. For example, you can use methods like `extend` and `rotate` with `deque`, which can be useful in various scenarios. `Queue` is specifically designed for multi-threaded applications and lacks these additional functionalities.

4. **Simplicity:** `deque` is simpler to use for basic FIFO operations compared to `Queue`, as it doesn't require importing a separate module (`collections` is part of the Python standard library).

Overall, if you're working in a single-threaded environment and don't require synchronization, `deque` is often the preferred choice due to its efficiency and simplicity. However, if you're working in a multi-threaded environment where synchronization is necessary, `Queue` provides the necessary thread-safety guarantees.
'''