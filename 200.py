from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.bfs(i, j, grid)
                    cnt += 1
        return cnt
    def bfs(self, i, j, grid):
        q = deque([(i, j)])
        while q:
            I, J = q.popleft()
            for i, j in [I+1, J], [I, J+1], [I-1, J], [I, J-1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    q.append((i, j))

sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = sol.numIslands(grid)
print(result)